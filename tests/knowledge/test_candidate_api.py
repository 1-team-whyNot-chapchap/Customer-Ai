from uuid import uuid4

from fastapi import FastAPI
from fastapi.testclient import TestClient

from chapchap_customer_ai.api.knowledge import build_candidate_knowledge_router
from chapchap_customer_ai.contracts.models import KnowledgeProcessingAccepted
from chapchap_customer_ai.main import create_app
from chapchap_customer_ai.security.models import AuthenticatedService


def request_payload() -> dict[str, object]:
    return {
        "schemaVersion": "1.0",
        "knowledgeVersionId": 101,
        "attempt": 1,
        "source": {
            "downloadUrl": "https://private-minio.example/policy?signature=secret",
            "contentType": "text/plain",
            "fileSize": 4,
        },
        "metadata": {
            "documentKey": "refund-policy",
            "sourceService": "subscription-service",
            "category": "REFUND",
            "version": "2026.09",
            "effectiveFrom": "2026-09-03T00:00:00Z",
        },
        "chunkProfile": "HYBRID_POLICY_V1",
        "callback": {"resultUri": "/internal/v1/knowledge-processing-results"},
    }


class AcceptingVerifier:
    def verify_service(self, authorization: str) -> AuthenticatedService:
        assert authorization == "Bearer service-token"
        return AuthenticatedService("customer-service")


class AcceptingService:
    def accept(self, request, *, request_id, idempotency_key):
        assert idempotency_key == "101:HYBRID_POLICY_V1"
        return KnowledgeProcessingAccepted(
            schema_version="1.0",
            processing_id=9001,
            knowledge_version_id=request.knowledge_version_id,
            status="ACCEPTED",
        )


def test_candidate_router_returns_202_contract() -> None:
    app = FastAPI()
    app.include_router(build_candidate_knowledge_router(AcceptingService(), AcceptingVerifier()))
    response = TestClient(app).post(
        "/internal/v1/knowledge-processings",
        headers={
            "Authorization": "Bearer service-token",
            "X-Request-Id": str(uuid4()),
            "Idempotency-Key": "101:HYBRID_POLICY_V1",
        },
        json=request_payload(),
    )

    assert response.status_code == 202
    assert response.json() == {
        "schemaVersion": "1.0",
        "processingId": 9001,
        "knowledgeVersionId": 101,
        "status": "ACCEPTED",
    }


def test_candidate_router_is_not_mounted_in_default_app() -> None:
    response = TestClient(create_app()).post(
        "/internal/v1/knowledge-processings", json=request_payload()
    )

    assert response.status_code == 404
