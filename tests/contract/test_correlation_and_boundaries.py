import json
from pathlib import Path
from uuid import UUID, uuid4

import httpx
from fastapi.testclient import TestClient

from chapchap_customer_ai.contracts.models import (
    ConsultationSummaryCompleted,
    KnowledgeProcessingCompleted,
)
from chapchap_customer_ai.knowledge.http import HttpKnowledgeResultPublisher
from chapchap_customer_ai.main import create_app
from chapchap_customer_ai.summary.http import HttpSummaryResultPublisher

FIXTURE_PATH = Path("tests/contract/fixtures/customer_ai_candidate_v1.json")


class StaticTokenProvider:
    def get_token(self) -> str:
        return "signed.service.jwt"


def test_async_callbacks_preserve_request_correlation_and_job_idempotency() -> None:
    fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(204)

    request_id = UUID(fixture["consultation"]["request"]["requestId"])
    knowledge_result = KnowledgeProcessingCompleted.model_validate(
        fixture["knowledge"]["completed"]
    )
    summary_result = ConsultationSummaryCompleted.model_validate(
        fixture["summary"]["completed"]
    )
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        HttpKnowledgeResultPublisher(
            client, StaticTokenProvider(), "https://customer-service.internal"
        ).publish(knowledge_result, request_id)
        HttpSummaryResultPublisher(
            client, StaticTokenProvider(), "https://customer-service.internal"
        ).publish(summary_result, request_id)

    assert {request.headers["x-request-id"] for request in requests} == {str(request_id)}
    assert requests[0].headers["idempotency-key"] == str(knowledge_result.processing_id)
    assert requests[1].headers["idempotency-key"] == str(summary_result.summary_job_id)


def test_all_candidate_routes_remain_unmounted_in_default_app() -> None:
    client = TestClient(create_app())
    headers = {
        "Authorization": "Bearer placeholder",
        "X-Request-Id": str(uuid4()),
        "Idempotency-Key": "placeholder",
    }

    assert client.post("/internal/v1/consultation-responses", headers=headers).status_code == 404
    assert client.post("/internal/v1/knowledge-processings", headers=headers).status_code == 404
    assert client.post("/internal/v1/consultation-summaries", headers=headers).status_code == 404
