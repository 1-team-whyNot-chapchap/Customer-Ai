from uuid import uuid4

import pytest
from pydantic import ValidationError

from chapchap_customer_ai.contracts.models import ConsultationResponseRequest


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
