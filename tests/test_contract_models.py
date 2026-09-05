from uuid import uuid4

import pytest
from pydantic import ValidationError

from chapchap_customer_ai.contracts.models import (
    ConsultationResponse,
    ConsultationResponseRequest,
)


def consultation_payload(user_id: int) -> dict[str, object]:
    return {
        "schemaVersion": "1.0",
        "requestId": str(uuid4()),
        "consultationId": 1,
        "triggerMessageId": 2,
        "subject": {
            "userId": user_id,
            "role": "CUSTOMER",
            "allowedAiScopes": ["customer-ai.policy.read"],
        },
        "message": "환불 정책을 알려줘",
        "conversationContext": [],
    }


def test_consultation_contract_accepts_positive_numeric_user_id() -> None:
    request = ConsultationResponseRequest.model_validate(consultation_payload(42))

    assert request.subject.user_id == 42


@pytest.mark.parametrize("user_id", [0, -1, "42"])
def test_consultation_contract_rejects_non_positive_or_string_user_id(user_id: object) -> None:
    with pytest.raises(ValidationError):
        ConsultationResponseRequest.model_validate(consultation_payload(user_id))


def test_consultation_response_enforces_decision_and_evidence_contract() -> None:
    request_id = str(uuid4())
    answer = ConsultationResponse.model_validate(
        {
            "schemaVersion": "1.0",
            "requestId": request_id,
            "decision": "ANSWER",
            "answer": "환불은 7일 이내 가능합니다.",
            "route": "POLICY",
            "degraded": False,
            "handoffRequired": False,
            "evidence": [
                {
                    "knowledgeVersionId": 101,
                    "chunkId": "chunk-1",
                    "retrievalRank": 1,
                    "retrievalScore": 0.9,
                }
            ],
        }
    )

    assert answer.evidence[0].chunk_id == "chunk-1"
    for invalid in (
        {"decision": "ANSWER", "answer": None, "route": "USER_STATE"},
        {"decision": "HANDOFF", "answer": "unsafe", "route": "POLICY"},
        {"decision": "DEGRADED", "answer": "partial", "route": "POLICY"},
    ):
        body = {
            "schemaVersion": "1.0",
            "requestId": request_id,
            "degraded": invalid["decision"] == "DEGRADED",
            "handoffRequired": invalid["decision"] == "HANDOFF",
            "evidence": [],
            **invalid,
        }
        with pytest.raises(ValidationError):
            ConsultationResponse.model_validate(body)


def test_consultation_subject_scopes_must_be_unique() -> None:
    body = consultation_payload(42)
    body["subject"]["allowedAiScopes"] = [
        "customer-ai.policy.read",
        "customer-ai.policy.read",
    ]

    with pytest.raises(ValidationError):
        ConsultationResponseRequest.model_validate(body)
