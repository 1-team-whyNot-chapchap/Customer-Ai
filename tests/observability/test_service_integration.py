from dataclasses import replace
from uuid import uuid4

from chapchap_customer_ai.consultation.models import Capability
from chapchap_customer_ai.consultation.services import ConsultationResponseService
from chapchap_customer_ai.contracts.models import (
    ConsultationSummaryRequest,
    KnowledgeProcessingRequest,
)
from chapchap_customer_ai.current_state.adapter import CurrentStateAdapter
from chapchap_customer_ai.current_state.models import TransportOutcome, TransportResult
from chapchap_customer_ai.observability.models import DiagnosticEvent, DiagnosticEventType
from tests.consultation.test_response_service import Dependencies, context, request
from tests.current_state.test_adapter import PAYMENT_PAYLOAD, RecordingTransport
from tests.knowledge.test_processing_service import (
    SourceFetchError,
    StaticFetcher,
)
from tests.knowledge.test_processing_service import (
    make_service as make_knowledge_service,
)
from tests.knowledge.test_processing_service import request_payload as knowledge_payload
from tests.summary.test_summary_service import (
    StaticComposer,
    SummaryComposerError,
)
from tests.summary.test_summary_service import (
    make_service as make_summary_service,
)
from tests.summary.test_summary_service import request_payload as summary_payload


class RecordingSink:
    def __init__(self) -> None:
        self.events: list[DiagnosticEvent] = []

    def emit(self, event: DiagnosticEvent) -> None:
        self.events.append(event)


class FailingSink:
    def emit(self, event: DiagnosticEvent) -> None:
        raise RuntimeError("private diagnostics failure")


def test_consultation_result_emits_minimal_correlated_diagnostic() -> None:
    dependencies = Dependencies()
    sink = RecordingSink()
    service = ConsultationResponseService(
        dependencies.versions,
        dependencies.retriever,
        dependencies.state,
        dependencies.composer,
        dependencies.service().registry,
        diagnostics=sink,
    )
    value = request("환불 정책 알려줘", ("customer-ai.policy.read",))

    response = service.respond(value, context(value), idempotency_key="observed")

    event = sink.events[0]
    assert event.event_type == DiagnosticEventType.CONSULTATION_RESULT
    assert event.request_id == response.request_id == value.request_id
    assert event.consultation_id == value.consultation_id
    assert event.route == response.route
    assert event.decision == response.decision


def test_knowledge_and_summary_results_emit_correlated_diagnostics() -> None:
    knowledge_sink = RecordingSink()
    knowledge_service, _, knowledge_publisher = make_knowledge_service()
    knowledge_service = replace(knowledge_service, diagnostics=knowledge_sink)
    knowledge_request_id = uuid4()
    knowledge_service.accept(
        KnowledgeProcessingRequest.model_validate(knowledge_payload()),
        request_id=knowledge_request_id,
        idempotency_key="101:HYBRID_POLICY_V1",
    )

    summary_sink = RecordingSink()
    summary_service, _, _, summary_publisher = make_summary_service()
    summary_service = replace(summary_service, diagnostics=summary_sink)
    summary_request_id = uuid4()
    summary_service.accept(
        ConsultationSummaryRequest.model_validate(summary_payload()),
        request_id=summary_request_id,
        idempotency_key="close-501",
    )

    assert knowledge_sink.events[0].request_id == knowledge_request_id
    assert knowledge_sink.events[0].processing_id == (
        knowledge_publisher.results[0].processing_id
    )
    assert knowledge_sink.events[0].event_type == DiagnosticEventType.KNOWLEDGE_COMPLETED
    assert summary_sink.events[0].request_id == summary_request_id
    assert summary_sink.events[0].consultation_id == (
        summary_publisher.results[0].consultation_id
    )
    assert summary_sink.events[0].event_type == DiagnosticEventType.SUMMARY_COMPLETED


def test_async_failures_emit_allowlisted_failure_diagnostics() -> None:
    knowledge_sink = RecordingSink()
    knowledge_service, _, _ = make_knowledge_service(
        fetcher=StaticFetcher(error=SourceFetchError("private detail"))
    )
    knowledge_service = replace(knowledge_service, diagnostics=knowledge_sink)
    knowledge_service.accept(
        KnowledgeProcessingRequest.model_validate(knowledge_payload()),
        request_id=uuid4(),
        idempotency_key="101:HYBRID_POLICY_V1",
    )

    summary_sink = RecordingSink()
    summary_service, _, _, _ = make_summary_service(
        composer=StaticComposer(error=SummaryComposerError("private detail"))
    )
    summary_service = replace(summary_service, diagnostics=summary_sink)
    summary_service.accept(
        ConsultationSummaryRequest.model_validate(summary_payload()),
        request_id=uuid4(),
        idempotency_key="close-501",
    )

    knowledge_event = knowledge_sink.events[0]
    summary_event = summary_sink.events[0]
    assert knowledge_event.event_type == DiagnosticEventType.KNOWLEDGE_FAILED
    assert knowledge_event.failure_code.value == "SOURCE_FETCH_FAILED"
    assert knowledge_event.retryable is True
    assert summary_event.event_type == DiagnosticEventType.SUMMARY_FAILED
    assert summary_event.failure_code.value == "LLM_UNAVAILABLE"
    assert summary_event.retryable is True


def test_current_state_contract_error_emits_only_contract_failure_code() -> None:
    sink = RecordingSink()
    transport = RecordingTransport(
        [TransportResult(TransportOutcome.CONTRACT_ERROR)]
    )
    value = request("내 결제 상태 알려줘", ("subscription.payment.read",))

    CurrentStateAdapter(transport, diagnostics=sink).fetch(
        (Capability.PAYMENT_CURRENT,), context(value), timeout_seconds=3.0
    )

    event = sink.events[0]
    assert event.event_type == DiagnosticEventType.CURRENT_STATE_RESULT
    assert event.failure_code.value == "CONTRACT_ERROR"
    assert event.availability is None


def test_current_state_emits_one_result_per_capability_without_business_values() -> None:
    sink = RecordingSink()
    transport = RecordingTransport(
        [TransportResult(TransportOutcome.SUCCESS, PAYMENT_PAYLOAD)]
    )
    value = request("내 결제 상태 알려줘", ("subscription.payment.read",))

    facts = CurrentStateAdapter(transport, diagnostics=sink).fetch(
        (Capability.PAYMENT_CURRENT,), context(value), timeout_seconds=3.0
    )

    event = sink.events[0]
    assert event.request_id == value.request_id
    assert event.consultation_id == value.consultation_id
    assert event.capability_id == Capability.PAYMENT_CURRENT
    assert event.availability == facts[0].availability
    assert "amount" not in event.model_dump(by_alias=True, exclude_none=True)


def test_diagnostic_sink_failure_does_not_change_consultation_result() -> None:
    dependencies = Dependencies()
    service = ConsultationResponseService(
        dependencies.versions,
        dependencies.retriever,
        dependencies.state,
        dependencies.composer,
        dependencies.service().registry,
        diagnostics=FailingSink(),
    )
    value = request("환불 정책 알려줘", ("customer-ai.policy.read",))

    response = service.respond(value, context(value), idempotency_key="sink-failure")

    assert response.decision.value == "ANSWER"


def test_diagnostic_sink_failure_does_not_change_async_callbacks() -> None:
    knowledge_service, _, knowledge_publisher = make_knowledge_service()
    knowledge_service = replace(knowledge_service, diagnostics=FailingSink())
    knowledge_service.accept(
        KnowledgeProcessingRequest.model_validate(knowledge_payload()),
        request_id=uuid4(),
        idempotency_key="101:HYBRID_POLICY_V1",
    )

    summary_service, _, _, summary_publisher = make_summary_service()
    summary_service = replace(summary_service, diagnostics=FailingSink())
    summary_service.accept(
        ConsultationSummaryRequest.model_validate(summary_payload()),
        request_id=uuid4(),
        idempotency_key="close-501",
    )

    assert len(knowledge_publisher.results) == 1
    assert knowledge_publisher.results[0].status == "COMPLETED"
    assert len(summary_publisher.results) == 1
    assert summary_publisher.results[0].status == "COMPLETED"


def test_diagnostic_sink_failure_does_not_change_current_state_result() -> None:
    transport = RecordingTransport(
        [TransportResult(TransportOutcome.SUCCESS, PAYMENT_PAYLOAD)]
    )
    value = request("내 결제 상태 알려줘", ("subscription.payment.read",))

    facts = CurrentStateAdapter(transport, diagnostics=FailingSink()).fetch(
        (Capability.PAYMENT_CURRENT,), context(value), timeout_seconds=3.0
    )

    assert len(facts) == 1
    assert facts[0].availability.value == "AVAILABLE"
