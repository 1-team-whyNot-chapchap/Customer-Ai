import json
import logging
from uuid import uuid4

import pytest
from pydantic import ValidationError

from chapchap_customer_ai.consultation.models import Capability, StateAvailability
from chapchap_customer_ai.contracts.models import ConsultationDecision, ConsultationRoute
from chapchap_customer_ai.observability.models import (
    DiagnosticEvent,
    DiagnosticEventType,
    DiagnosticFailureCode,
)
from chapchap_customer_ai.observability.sinks import JsonLogDiagnosticSink, emit_safely


def consultation_event() -> DiagnosticEvent:
    return DiagnosticEvent(
        event_type=DiagnosticEventType.CONSULTATION_RESULT,
        request_id=uuid4(),
        consultation_id=501,
        route=ConsultationRoute.POLICY,
        decision=ConsultationDecision.ANSWER,
        trace_id="0123456789abcdef0123456789abcdef",
        latency_ms=27,
    )


@pytest.mark.parametrize(
    "event",
    [
        consultation_event(),
        DiagnosticEvent(
            event_type=DiagnosticEventType.KNOWLEDGE_COMPLETED,
            request_id=uuid4(),
            knowledge_version_id=101,
            processing_id=8001,
            chunk_count=3,
        ),
        DiagnosticEvent(
            event_type=DiagnosticEventType.KNOWLEDGE_FAILED,
            request_id=uuid4(),
            knowledge_version_id=101,
            processing_id=8001,
            failure_code=DiagnosticFailureCode.EMBEDDING_UNAVAILABLE,
            retryable=True,
        ),
        DiagnosticEvent(
            event_type=DiagnosticEventType.SUMMARY_COMPLETED,
            request_id=uuid4(),
            consultation_id=501,
        ),
        DiagnosticEvent(
            event_type=DiagnosticEventType.SUMMARY_FAILED,
            request_id=uuid4(),
            consultation_id=501,
            failure_code=DiagnosticFailureCode.LLM_UNAVAILABLE,
            retryable=True,
        ),
        DiagnosticEvent(
            event_type=DiagnosticEventType.CURRENT_STATE_RESULT,
            request_id=uuid4(),
            consultation_id=501,
            capability_id=Capability.PAYMENT_CURRENT,
            availability=StateAvailability.AVAILABLE,
        ),
        DiagnosticEvent(
            event_type=DiagnosticEventType.CURRENT_STATE_RESULT,
            request_id=uuid4(),
            consultation_id=501,
            capability_id=Capability.PAYMENT_CURRENT,
            failure_code=DiagnosticFailureCode.CONTRACT_ERROR,
        ),
    ],
)
def test_each_diagnostic_event_has_a_strict_valid_shape(event: DiagnosticEvent) -> None:
    payload = event.model_dump(by_alias=True, mode="json", exclude_none=True)
    assert "requestId" in payload
    assert set(payload).issubset(
        {
            "eventType",
            "requestId",
            "traceId",
            "consultationId",
            "knowledgeVersionId",
            "processingId",
            "route",
            "capabilityId",
            "decision",
            "availability",
            "failureCode",
            "retryable",
            "latencyMs",
            "chunkCount",
        }
    )


@pytest.mark.parametrize(
    "payload",
    [
        {
            "eventType": "CONSULTATION_RESULT",
            "requestId": str(uuid4()),
            "consultationId": 501,
            "route": "POLICY",
            "decision": "ANSWER",
            "message": "raw prompt",
        },
        {
            "eventType": "CONSULTATION_RESULT",
            "requestId": str(uuid4()),
            "consultationId": 501,
            "route": "POLICY",
            "decision": "ANSWER",
            "traceId": "not-a-trace-id",
        },
        {
            "eventType": "KNOWLEDGE_COMPLETED",
            "requestId": str(uuid4()),
            "knowledgeVersionId": 101,
            "processingId": 8001,
        },
        {
            "eventType": "SUMMARY_COMPLETED",
            "requestId": str(uuid4()),
            "consultationId": 501,
            "failureCode": "LLM_UNAVAILABLE",
        },
        {
            "eventType": "CURRENT_STATE_RESULT",
            "requestId": str(uuid4()),
            "consultationId": 501,
            "capabilityId": "CAP-PAYMENT-CURRENT",
            "availability": "AVAILABLE",
            "failureCode": "CONTRACT_ERROR",
        },
    ],
)
def test_diagnostics_reject_forbidden_extra_and_cross_event_fields(payload) -> None:
    with pytest.raises(ValidationError):
        DiagnosticEvent.model_validate(payload)


def test_json_logger_emits_only_validated_allowlisted_fields(caplog) -> None:
    logger = logging.getLogger("customer-ai.diagnostics.test")
    event = consultation_event()

    with caplog.at_level(logging.INFO, logger=logger.name):
        JsonLogDiagnosticSink(logger).emit(event)

    payload = json.loads(caplog.records[-1].message)
    assert payload["requestId"] == str(event.request_id)
    assert payload["traceId"] == event.trace_id
    serialized = caplog.records[-1].message.lower()
    assert all(
        forbidden not in serialized
        for forbidden in (
            "authorization",
            "subjectassertion",
            "prompt",
            "presigned",
            "downloadurl",
            "rawtooldto",
        )
    )


def test_metric_dimensions_exclude_high_cardinality_fields() -> None:
    event = consultation_event()

    assert event.metric_dimensions() == {
        "eventType": "CONSULTATION_RESULT",
        "route": "POLICY",
        "decision": "ANSWER",
    }
    assert all(
        key not in event.metric_dimensions()
        for key in (
            "requestId",
            "traceId",
            "consultationId",
            "knowledgeVersionId",
            "processingId",
            "latencyMs",
        )
    )


class FailingSink:
    def emit(self, event: DiagnosticEvent) -> None:
        raise RuntimeError("diagnostic backend unavailable")


def test_safe_emission_never_propagates_sink_failure() -> None:
    emit_safely(FailingSink(), consultation_event())
