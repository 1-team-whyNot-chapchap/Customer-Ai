import pytest
from pydantic import ValidationError

from chapchap_customer_ai.contracts.models import (
    ConsultationSummaryCompleted,
    ConsultationSummaryFailed,
    ConsultationSummaryRequest,
)


def valid_request() -> dict[str, object]:
    return {
        "schemaVersion": "1.0",
        "summaryJobId": 7001,
        "consultationId": 501,
        "messages": [{"senderType": "AI", "content": "정책 근거를 안내함"}],
        "callback": {"resultUri": "/internal/v1/consultation-summary-results"},
    }


@pytest.mark.parametrize(
    "mutation",
    [
        lambda value: value.update({"unexpected": True}),
        lambda value: value.update({"summaryJobId": 0}),
        lambda value: value.update({"messages": []}),
        lambda value: value["messages"][0].update({"senderType": "SYSTEM"}),
        lambda value: value["messages"][0].update({"content": "   "}),
        lambda value: value.update(
            {"callback": {"resultUri": "/internal/v1/arbitrary-results"}}
        ),
    ],
)
def test_summary_request_rejects_fields_outside_candidate_contract(mutation) -> None:
    payload = valid_request()
    mutation(payload)

    with pytest.raises(ValidationError):
        ConsultationSummaryRequest.model_validate(payload)


def test_completed_and_failed_results_keep_mutually_exclusive_fields() -> None:
    with pytest.raises(ValidationError):
        ConsultationSummaryCompleted.model_validate(
            {
                "schemaVersion": "1.0",
                "summaryJobId": 7001,
                "consultationId": 501,
                "status": "COMPLETED",
                "summary": "요약",
                "failureCode": "LLM_UNAVAILABLE",
            }
        )
    with pytest.raises(ValidationError):
        ConsultationSummaryFailed.model_validate(
            {
                "schemaVersion": "1.0",
                "summaryJobId": 7001,
                "consultationId": 501,
                "status": "FAILED",
                "failureCode": "LLM_UNAVAILABLE",
                "retryable": True,
                "summary": "요약",
            }
        )
