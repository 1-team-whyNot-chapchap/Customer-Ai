from uuid import uuid4

from fastapi import FastAPI
from fastapi.testclient import TestClient

from chapchap_customer_ai.api.consultation import build_candidate_consultation_router
from chapchap_customer_ai.contracts.models import (
    ConsultationDecision,
    ConsultationResponse,
    ConsultationRoute,
    UserRole,
)
from chapchap_customer_ai.main import create_app
from chapchap_customer_ai.security.models import AuthenticatedContext, AuthenticatedSubject


def payload(request_id: str) -> dict[str, object]:
    return {
        "schemaVersion": "1.0",
        "requestId": request_id,
        "consultationId": 501,
        "triggerMessageId": 9002,
        "subject": {
            "userId": 42,
            "role": "CUSTOMER",
            "allowedAiScopes": ["customer-ai.policy.read"],
        },
        "message": "환불 정책 알려줘",
        "conversationContext": [],
    }


class Verifier:
    def verify_consultation(self, authorization, subject_assertion, **kwargs):
        assert authorization == "Bearer service-token"
        assert subject_assertion == "signed-subject"
        return AuthenticatedContext(
            "customer-service",
            AuthenticatedSubject(
                42,
                UserRole.CUSTOMER,
                frozenset({"customer-ai.policy.read"}),
                kwargs["expected_request_id"],
                kwargs["expected_consultation_id"],
            ),
        )


class Service:
    def respond(self, request, context, *, idempotency_key):
        assert idempotency_key == "message-9002"
        return ConsultationResponse(
            schema_version="1.0",
            request_id=request.request_id,
            decision=ConsultationDecision.HANDOFF,
            route=ConsultationRoute.POLICY,
            degraded=False,
            handoff_required=True,
        )


def test_candidate_api_validates_headers_and_returns_contract() -> None:
    request_id = str(uuid4())
    app = FastAPI()
    app.include_router(build_candidate_consultation_router(Service(), Verifier()))

    response = TestClient(app).post(
        "/internal/v1/consultation-responses",
        headers={
            "Authorization": "Bearer service-token",
            "X-Subject-Assertion": "signed-subject",
            "X-Request-Id": request_id,
            "Idempotency-Key": "message-9002",
        },
        json=payload(request_id),
    )

    assert response.status_code == 200
    assert response.json() == {
        "schemaVersion": "1.0",
        "requestId": request_id,
        "decision": "HANDOFF",
        "route": "POLICY",
        "degraded": False,
        "handoffRequired": True,
        "evidence": [],
    }


def test_header_body_request_id_mismatch_is_rejected() -> None:
    body_request_id = str(uuid4())
    app = FastAPI()
    app.include_router(build_candidate_consultation_router(Service(), Verifier()))

    response = TestClient(app).post(
        "/internal/v1/consultation-responses",
        headers={
            "Authorization": "Bearer service-token",
            "X-Subject-Assertion": "signed-subject",
            "X-Request-Id": str(uuid4()),
            "Idempotency-Key": "message-9002",
        },
        json=payload(body_request_id),
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "REQUEST_ID_MISMATCH"


def test_candidate_api_is_not_mounted_in_default_app() -> None:
    response = TestClient(create_app()).post(
        "/internal/v1/consultation-responses", json=payload(str(uuid4()))
    )

    assert response.status_code == 404
