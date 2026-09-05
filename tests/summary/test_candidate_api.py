from uuid import uuid4

from fastapi import FastAPI
from fastapi.testclient import TestClient

from chapchap_customer_ai.api.summary import build_candidate_summary_router
from chapchap_customer_ai.contracts.models import ConsultationSummaryAccepted
from chapchap_customer_ai.main import create_app
from chapchap_customer_ai.security.models import AuthenticatedService


def request_payload() -> dict[str, object]:
    return {
        "schemaVersion": "1.0",
        "summaryJobId": 7001,
        "consultationId": 501,
        "messages": [
            {"senderType": "USER", "content": "환불을 문의함"},
            {"senderType": "ADMIN", "content": "환불 정책을 안내함"},
        ],
        "callback": {"resultUri": "/internal/v1/consultation-summary-results"},
    }


class AcceptingVerifier:
    def verify_service(self, authorization: str) -> AuthenticatedService:
        assert authorization == "Bearer service-token"
        return AuthenticatedService("customer-service")


class AcceptingService:
    def accept(self, request, *, request_id, idempotency_key):
        assert idempotency_key == "close-501"
        return ConsultationSummaryAccepted(
            schema_version="1.0",
            summary_job_id=request.summary_job_id,
            consultation_id=request.consultation_id,
            status="ACCEPTED",
        )


def test_candidate_router_returns_202_contract() -> None:
    app = FastAPI()
    app.include_router(build_candidate_summary_router(AcceptingService(), AcceptingVerifier()))

    response = TestClient(app).post(
        "/internal/v1/consultation-summaries",
        headers={
            "Authorization": "Bearer service-token",
            "X-Request-Id": str(uuid4()),
            "Idempotency-Key": "close-501",
        },
        json=request_payload(),
    )

    assert response.status_code == 202
    assert response.json() == {
        "schemaVersion": "1.0",
        "summaryJobId": 7001,
        "consultationId": 501,
        "status": "ACCEPTED",
    }


def test_candidate_router_requires_service_headers() -> None:
    app = FastAPI()
    app.include_router(build_candidate_summary_router(AcceptingService(), AcceptingVerifier()))

    response = TestClient(app).post(
        "/internal/v1/consultation-summaries",
        json=request_payload(),
    )

    assert response.status_code == 422


def test_candidate_router_is_not_mounted_in_default_app() -> None:
    response = TestClient(create_app()).post(
        "/internal/v1/consultation-summaries",
        json=request_payload(),
    )

    assert response.status_code == 404
