import json
from copy import deepcopy
from pathlib import Path
from uuid import UUID

import pytest
from pydantic import ValidationError

from chapchap_customer_ai.contracts.models import (
    ConsultationResponse,
    ConsultationResponseRequest,
    ConsultationSummaryAccepted,
    ConsultationSummaryCompleted,
    ConsultationSummaryFailed,
    ConsultationSummaryRequest,
    KnowledgeProcessingAccepted,
    KnowledgeProcessingCompleted,
    KnowledgeProcessingFailed,
    KnowledgeProcessingRequest,
)
from chapchap_customer_ai.current_state.contracts import (
    CurrentDeliveryState,
    CurrentPaymentState,
    CurrentSubscriptionState,
    RecentRefundResult,
)

FIXTURE_PATH = Path("tests/contract/fixtures/customer_ai_candidate_v1.json")


@pytest.fixture(scope="module")
def fixture() -> dict[str, object]:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def provider_cases(payload: dict[str, object]):
    consultation = payload["consultation"]
    knowledge = payload["knowledge"]
    summary = payload["summary"]
    current_state = payload["currentState"]
    return (
        (ConsultationResponseRequest, consultation["request"]),
        (ConsultationResponse, consultation["answer"]),
        (ConsultationResponse, consultation["handoff"]),
        (ConsultationResponse, consultation["degraded"]),
        (KnowledgeProcessingRequest, knowledge["request"]),
        (KnowledgeProcessingAccepted, knowledge["accepted"]),
        (KnowledgeProcessingCompleted, knowledge["completed"]),
        (KnowledgeProcessingFailed, knowledge["failed"]),
        (ConsultationSummaryRequest, summary["request"]),
        (ConsultationSummaryAccepted, summary["accepted"]),
        (ConsultationSummaryCompleted, summary["completed"]),
        (ConsultationSummaryFailed, summary["failed"]),
        (CurrentPaymentState, current_state["payment"]),
        (RecentRefundResult, current_state["refund"]),
        (CurrentSubscriptionState, current_state["subscription"]),
        (CurrentDeliveryState, current_state["delivery"]),
    )


def test_provider_models_round_trip_every_candidate_fixture(fixture) -> None:
    assert fixture["contractStatus"] == "CANDIDATE"
    assert fixture["schemaVersion"] == "1.0"

    for model, candidate in provider_cases(fixture):
        parsed = model.model_validate(candidate)
        exclude_none = model is ConsultationResponse
        assert parsed.model_dump(
            by_alias=True, mode="json", exclude_none=exclude_none,
            exclude_unset=model is ConsultationResponseRequest,
        ) == candidate


def assert_exact_object(value, required_keys: set[str]) -> None:
    assert type(value) is dict
    assert set(value) == required_keys


def assert_positive_int(value) -> None:
    assert type(value) is int and 0 < value <= 9_223_372_036_854_775_807


def assert_uuid(value) -> None:
    assert type(value) is str
    UUID(value)


def test_consumer_shape_independently_checks_ids_and_result_exclusivity(fixture) -> None:
    consultation = fixture["consultation"]
    knowledge = fixture["knowledge"]
    summary = fixture["summary"]

    request = consultation["request"]
    assert_exact_object(
        request,
        {
            "schemaVersion",
            "requestId",
            "consultationId",
            "triggerMessageId",
            "subject",
            "message",
            "conversationContext",
        },
    )
    assert_uuid(request["requestId"])
    assert_positive_int(request["consultationId"])
    assert_positive_int(request["triggerMessageId"])
    for name in ("answer", "handoff", "degraded"):
        assert consultation[name]["requestId"] == request["requestId"]
    assert "answer" in consultation["answer"] and "answer" not in consultation["handoff"]

    assert knowledge["accepted"]["knowledgeVersionId"] == knowledge["request"][
        "knowledgeVersionId"
    ]
    assert knowledge["completed"]["processingId"] == knowledge["failed"]["processingId"]
    assert "failureCode" not in knowledge["completed"]
    assert "chunkCount" not in knowledge["failed"]

    assert summary["accepted"]["summaryJobId"] == summary["request"]["summaryJobId"]
    assert summary["completed"]["consultationId"] == summary["failed"]["consultationId"]
    assert "failureCode" not in summary["completed"]
    assert "summary" not in summary["failed"]


@pytest.mark.parametrize(
    ("case_index", "field", "value"),
    [
        (1, "decision", "UNKNOWN"),
        (6, "status", "READY"),
        (7, "failureCode", "RAW_PROVIDER_ERROR"),
        (9, "status", "RUNNING"),
        (11, "failureCode", "PRIVATE_ERROR"),
        (12, "status", "COMPLETED"),
        (15, "status", "DELIVERED"),
    ],
)
def test_unknown_status_and_failure_code_are_fail_closed(
    fixture, case_index: int, field: str, value: str
) -> None:
    model, original = provider_cases(fixture)[case_index]
    candidate = deepcopy(original)
    candidate[field] = value

    with pytest.raises(ValidationError):
        model.model_validate(candidate)


def test_extra_sensitive_field_is_rejected_by_every_provider_model(fixture) -> None:
    for model, original in provider_cases(fixture):
        candidate = deepcopy(original)
        candidate["authorization"] = "forbidden"
        with pytest.raises(ValidationError):
            model.model_validate(candidate)


def test_fixture_contains_no_secret_or_raw_transport_material(fixture) -> None:
    serialized = json.dumps(fixture, ensure_ascii=False).lower()
    forbidden = (
        "bearer ",
        "subject-assertion",
        "clientsecret",
        "privatekey",
        "signature=",
        "presigned",
        "rawtooldto",
    )
    assert all(value not in serialized for value in forbidden)
