import hashlib
import json
from dataclasses import dataclass
from uuid import UUID

from chapchap_customer_ai.contracts.models import (
    ConsultationSummaryAccepted,
    ConsultationSummaryCompleted,
    ConsultationSummaryFailed,
    ConsultationSummaryFailureCode,
    ConsultationSummaryRequest,
)
from chapchap_customer_ai.observability.models import DiagnosticEvent, DiagnosticEventType
from chapchap_customer_ai.observability.ports import DiagnosticSink
from chapchap_customer_ai.observability.sinks import NoOpDiagnosticSink, emit_safely
from chapchap_customer_ai.summary.guardrails import SummaryGuardrails
from chapchap_customer_ai.summary.models import (
    RETRYABLE_FAILURES,
    SummaryComposerError,
    SummaryRequestError,
)
from chapchap_customer_ai.summary.ports import (
    SummaryComposer,
    SummaryJobRegistry,
    SummaryJobScheduler,
    SummaryResultPublisher,
)


@dataclass(frozen=True, slots=True)
class ConsultationSummaryService:
    registry: SummaryJobRegistry
    scheduler: SummaryJobScheduler
    composer: SummaryComposer
    result_publisher: SummaryResultPublisher
    guardrails: SummaryGuardrails = SummaryGuardrails()
    compose_timeout_seconds: float = 8.0
    diagnostics: DiagnosticSink = NoOpDiagnosticSink()

    def __post_init__(self) -> None:
        if self.compose_timeout_seconds <= 0:
            raise ValueError("summary compose timeout must be positive")

    def accept(
        self,
        request: ConsultationSummaryRequest,
        *,
        request_id: UUID,
        idempotency_key: str,
    ) -> ConsultationSummaryAccepted:
        if not idempotency_key.strip():
            raise SummaryRequestError("Idempotency-Key must not be blank.")
        registration = self.registry.register(
            idempotency_key,
            request.summary_job_id,
            self._fingerprint(request),
        )
        if registration.should_schedule:
            try:
                record = getattr(self.registry, "record_request", None)
                if record is not None:
                    record(idempotency_key, request_id, request)
                self.scheduler.submit(
                    lambda: self._run_registered(idempotency_key, request, request_id)
                )
            except Exception:
                self.registry.release(idempotency_key, request.summary_job_id)
                raise SummaryRequestError(
                    "Consultation summary processing is temporarily unavailable.",
                    status_code=503,
                ) from None
        return ConsultationSummaryAccepted(
            schema_version="1.0",
            summary_job_id=request.summary_job_id,
            consultation_id=request.consultation_id,
            status="ACCEPTED",
        )

    def _run_registered(self, key, request, request_id):
        try:
            result = self._process(request, request_id)
        except Exception:
            self.registry.release(key, request.summary_job_id)
            raise
        if isinstance(result, ConsultationSummaryFailed):
            failed = getattr(self.registry, "complete_failure", self.registry.release)
            failed(key, request.summary_job_id)
            return
        complete = getattr(self.registry, "complete", None)
        if complete is not None:
            complete(key, request.summary_job_id)

    def _process(self, request: ConsultationSummaryRequest, request_id: UUID):
        try:
            safe_messages, excluded = self.guardrails.prepare(request.messages)
            note = "일부 메시지는 안전 검토를 위해 요약에서 제외했습니다. 원문을 확인해 주세요."
            limit = min(500, self.guardrails.max_summary_characters)
            if not safe_messages:
                result = ConsultationSummaryCompleted(
                    schema_version="1.0", summary_job_id=request.summary_job_id,
                    consultation_id=request.consultation_id, status="COMPLETED",
                    summary=("안전하게 요약할 수 있는 대화가 없습니다. " + note)[:limit],
                )
            else:
                draft = self.composer.summarize(
                    safe_messages,
                    timeout_seconds=self.compose_timeout_seconds,
                )
                if not self.guardrails.output_is_safe(draft.text):
                    result = self._failed(
                        request,
                        ConsultationSummaryFailureCode.SUMMARY_GENERATION_FAILED,
                    )
                else:
                    result = ConsultationSummaryCompleted(
                        schema_version="1.0",
                        summary_job_id=request.summary_job_id,
                        consultation_id=request.consultation_id,
                        status="COMPLETED",
                        summary=(draft.text[:max(0, limit - len(note) - 2)] + "\n\n" + note)[:limit]
                        if excluded else draft.text,
                    )
        except TimeoutError:
            result = self._failed(request, ConsultationSummaryFailureCode.PROCESSING_TIMEOUT)
        except SummaryComposerError:
            result = self._failed(request, ConsultationSummaryFailureCode.LLM_UNAVAILABLE)
        except (TypeError, ValueError, AttributeError):
            result = self._failed(request, ConsultationSummaryFailureCode.SUMMARY_GENERATION_FAILED)
        except Exception:
            result = self._failed(request, ConsultationSummaryFailureCode.CUSTOMER_AI_UNAVAILABLE)
        if isinstance(result, ConsultationSummaryCompleted):
            event = DiagnosticEvent(
                event_type=DiagnosticEventType.SUMMARY_COMPLETED,
                request_id=request_id,
                consultation_id=request.consultation_id,
            )
        else:
            event = DiagnosticEvent(
                event_type=DiagnosticEventType.SUMMARY_FAILED,
                request_id=request_id,
                consultation_id=request.consultation_id,
                failure_code=result.failure_code,
                retryable=result.retryable,
            )
        emit_safely(self.diagnostics, event)
        self.result_publisher.publish(result, request_id)
        return result

    @staticmethod
    def _failed(
        request: ConsultationSummaryRequest,
        failure_code: ConsultationSummaryFailureCode,
    ) -> ConsultationSummaryFailed:
        return ConsultationSummaryFailed(
            schema_version="1.0",
            summary_job_id=request.summary_job_id,
            consultation_id=request.consultation_id,
            status="FAILED",
            failure_code=failure_code,
            retryable=failure_code in RETRYABLE_FAILURES,
        )

    @staticmethod
    def _fingerprint(request: ConsultationSummaryRequest) -> str:
        canonical = json.dumps(
            request.model_dump(by_alias=True, mode="json"),
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
        return hashlib.sha256(canonical).hexdigest()
