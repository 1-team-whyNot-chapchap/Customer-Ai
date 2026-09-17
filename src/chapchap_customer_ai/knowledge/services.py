import hashlib
import json
import logging
from dataclasses import dataclass
from uuid import UUID

from chapchap_customer_ai.contracts.models import (
    KnowledgeProcessingAccepted,
    KnowledgeProcessingCompleted,
    KnowledgeProcessingFailed,
    KnowledgeProcessingFailureCode,
    KnowledgeProcessingRequest,
)
from chapchap_customer_ai.knowledge.models import (
    RETRYABLE_FAILURES,
    KnowledgeRequestError,
    SourceFetchError,
)
from chapchap_customer_ai.knowledge.ports import (
    JobScheduler,
    KnowledgeIndexer,
    KnowledgeJobRegistry,
    KnowledgeResultPublisher,
    KnowledgeSourceFetcher,
    RagChunkBuilder,
)
from chapchap_customer_ai.observability.models import (
    DiagnosticEvent,
    DiagnosticEventType,
)
from chapchap_customer_ai.observability.ports import DiagnosticSink
from chapchap_customer_ai.observability.sinks import NoOpDiagnosticSink, emit_safely
from chapchap_customer_ai.rag.models import (
    KnowledgeContext,
    RagCoreError,
    RagFailureCode,
)


_LOGGER = logging.getLogger(__name__)
# Only static reason codes are emitted. Never log source URLs, tokens or document text.
_SOURCE_FAILURE_REASONS = {
    "The knowledge source is not allowed.": "SOURCE_NOT_ALLOWED",
    "The knowledge source could not be fetched.": "FETCH_UNAVAILABLE",
    "The knowledge source content type does not match.": "CONTENT_TYPE_MISMATCH",
    "The knowledge source size does not match.": "SIZE_MISMATCH",
    "The knowledge source exceeds the allowed size.": "SIZE_LIMIT_EXCEEDED",
    "The knowledge source size is invalid.": "INVALID_SIZE",
}


@dataclass(frozen=True, slots=True)
class KnowledgeProcessingService:
    registry: KnowledgeJobRegistry
    scheduler: JobScheduler
    source_fetcher: KnowledgeSourceFetcher
    chunk_builder: RagChunkBuilder
    indexer: KnowledgeIndexer
    result_publisher: KnowledgeResultPublisher
    diagnostics: DiagnosticSink = NoOpDiagnosticSink()

    def accept(
        self,
        request: KnowledgeProcessingRequest,
        *,
        request_id: UUID,
        idempotency_key: str,
    ) -> KnowledgeProcessingAccepted:
        logical_key = f"{request.knowledge_version_id}:{request.chunk_profile}"
        if idempotency_key != logical_key:
            raise KnowledgeRequestError(
                "Idempotency-Key must match knowledgeVersionId and chunkProfile."
            )
        registration = self.registry.register(
            logical_key, self._immutable_fingerprint(request), request.attempt
        )
        if registration.should_schedule:
            try:
                record = getattr(self.registry, "record_request", None)
                if record is not None:
                    record(logical_key, request_id, request)
                self.scheduler.submit(
                    lambda: self._run_registered(
                        logical_key, registration.processing_id, request_id, request
                    )
                )
            except Exception:
                self.registry.release_attempt(logical_key, request.attempt)
                raise KnowledgeRequestError(
                    "Knowledge processing is temporarily unavailable.", status_code=503
                ) from None
        return KnowledgeProcessingAccepted(
            schema_version="1.0",
            processing_id=registration.processing_id,
            knowledge_version_id=request.knowledge_version_id,
            status="ACCEPTED",
        )

    def _run_registered(self, key, processing_id, request_id, request):
        try:
            self._process(processing_id, request_id, request)
        except Exception:
            self.registry.release_attempt(key, request.attempt)
            raise
        complete = getattr(self.registry, "complete_attempt", None)
        if complete is not None:
            complete(key, request.attempt)

    def _process(
        self, processing_id: int, request_id: UUID, request: KnowledgeProcessingRequest
    ) -> None:
        stage = "SOURCE_FETCH"
        try:
            content = self.source_fetcher.fetch(request.source)
            stage = "CHUNK_BUILD"
            context = KnowledgeContext(
                request.knowledge_version_id,
                request.chunk_profile,
                request.metadata.document_key,
                request.metadata.category,
                request.metadata.version,
                request.metadata.effective_from,
            )
            chunks = tuple(
                self.chunk_builder.build_chunks(context, content, request.source.content_type)
            )
            stage = "EMBEDDING_AND_STORE"
            chunk_count = self.indexer.index(chunks)
            if chunk_count < 1 or chunk_count != len(chunks):
                raise RagCoreError(
                    RagFailureCode.VECTOR_STORE_UNAVAILABLE,
                    "Not all knowledge chunks were stored.",
                )
            result = KnowledgeProcessingCompleted(
                schema_version="1.0",
                processing_id=processing_id,
                knowledge_version_id=request.knowledge_version_id,
                status="COMPLETED",
                chunk_count=chunk_count,
                chunk_profile=request.chunk_profile,
            )
        except SourceFetchError as error:
            result = self._failed(
                processing_id,
                request.knowledge_version_id,
                KnowledgeProcessingFailureCode.SOURCE_FETCH_FAILED,
            )
            self._log_failure(stage, error, processing_id, request_id, request, result.failure_code)
        except TimeoutError as error:
            result = self._failed(
                processing_id,
                request.knowledge_version_id,
                KnowledgeProcessingFailureCode.PROCESSING_TIMEOUT,
            )
            self._log_failure(stage, error, processing_id, request_id, request, result.failure_code)
        except RagCoreError as error:
            try:
                failure_code = KnowledgeProcessingFailureCode(error.code)
            except ValueError:
                failure_code = KnowledgeProcessingFailureCode.CUSTOMER_AI_UNAVAILABLE
            result = self._failed(processing_id, request.knowledge_version_id, failure_code)
            self._log_failure(stage, error, processing_id, request_id, request, result.failure_code)
        except Exception as error:
            result = self._failed(
                processing_id,
                request.knowledge_version_id,
                KnowledgeProcessingFailureCode.CUSTOMER_AI_UNAVAILABLE,
            )
            self._log_failure(stage, error, processing_id, request_id, request, result.failure_code)
        if isinstance(result, KnowledgeProcessingCompleted):
            event = DiagnosticEvent(
                event_type=DiagnosticEventType.KNOWLEDGE_COMPLETED,
                request_id=request_id,
                knowledge_version_id=request.knowledge_version_id,
                processing_id=processing_id,
                chunk_count=result.chunk_count,
            )
        else:
            event = DiagnosticEvent(
                event_type=DiagnosticEventType.KNOWLEDGE_FAILED,
                request_id=request_id,
                knowledge_version_id=request.knowledge_version_id,
                processing_id=processing_id,
                failure_code=result.failure_code,
                retryable=result.retryable,
            )
        emit_safely(self.diagnostics, event)
        try:
            self.result_publisher.publish(result, request_id)
        except Exception as error:
            # Delivery failure is separate from processing failure. Preserve existing
            # exception/release semantics; do not turn a stored result into FAILED.
            self._log_failure("CALLBACK_DELIVERY", error, processing_id, request_id, request)
            raise

    @staticmethod
    def _log_failure(
        stage: str,
        error: Exception,
        processing_id: int,
        request_id: UUID,
        request: KnowledgeProcessingRequest,
        failure_code: KnowledgeProcessingFailureCode | None = None,
    ) -> None:
        try:
            detail = {
                "eventType": "KNOWLEDGE_FAILURE_DETAIL",
                "requestId": str(request_id),
                "knowledgeVersionId": request.knowledge_version_id,
                "processingId": processing_id,
                "attempt": request.attempt,
                "stage": stage,
                "errorType": type(error).__name__,
            }
            if failure_code is not None:
                detail["failureCode"] = failure_code.value
            if error.__cause__ is not None:
                detail["causeType"] = type(error.__cause__).__name__
            if isinstance(error, SourceFetchError):
                detail["sourceReason"] = _SOURCE_FAILURE_REASONS.get(
                    str(error), "SOURCE_FETCH_ERROR"
                )
            # Raw exception messages and traceback can contain presigned URLs/secrets.
            _LOGGER.warning(json.dumps(detail, ensure_ascii=False, separators=(",", ":")))
        except Exception:
            # Diagnostic output must not change the business result or callback.
            pass

    @staticmethod
    def _failed(
        processing_id: int,
        knowledge_version_id: int,
        failure_code: KnowledgeProcessingFailureCode,
    ) -> KnowledgeProcessingFailed:
        return KnowledgeProcessingFailed(
            schema_version="1.0",
            processing_id=processing_id,
            knowledge_version_id=knowledge_version_id,
            status="FAILED",
            failure_code=failure_code,
            retryable=failure_code in RETRYABLE_FAILURES,
        )

    @staticmethod
    def _immutable_fingerprint(request: KnowledgeProcessingRequest) -> str:
        payload = request.model_dump(by_alias=True, mode="json")
        payload.pop("attempt")
        source = payload["source"]
        if isinstance(source, dict):
            source.pop("downloadUrl")
        canonical = json.dumps(
            payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True
        ).encode("utf-8")
        return hashlib.sha256(canonical).hexdigest()
