from uuid import uuid4

import httpx
import pytest

from chapchap_customer_ai.contracts.models import ConsultationSummaryCompleted
from chapchap_customer_ai.summary.http import HttpSummaryResultPublisher
from chapchap_customer_ai.summary.models import SummaryCallbackDeliveryError


class StaticTokenProvider:
    def get_token(self) -> str:
        return "signed.service.jwt"


def completed_result() -> ConsultationSummaryCompleted:
    return ConsultationSummaryCompleted(
        schema_version="1.0",
        summary_job_id=7001,
        consultation_id=501,
        status="COMPLETED",
        summary="상담 내용을 요약함",
    )


def test_callback_retry_uses_same_job_id_and_identical_result() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(503 if len(requests) == 1 else 204)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        publisher = HttpSummaryResultPublisher(
            client,
            StaticTokenProvider(),
            "https://customer-service.internal",
            sleeper=lambda _: None,
        )
        request_id = uuid4()
        publisher.publish(completed_result(), request_id)

    assert len(requests) == 2
    assert {request.headers["idempotency-key"] for request in requests} == {"7001"}
    assert requests[0].content == requests[1].content
    assert requests[-1].url.path == "/internal/v1/consultation-summary-results"
    assert requests[-1].headers["authorization"] == "Bearer signed.service.jwt"
    assert requests[-1].headers["x-request-id"] == str(request_id)


def test_callback_does_not_retry_auth_or_contract_failure() -> None:
    calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        return httpx.Response(403)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        publisher = HttpSummaryResultPublisher(
            client,
            StaticTokenProvider(),
            "https://customer-service.internal",
            sleeper=lambda _: None,
        )
        with pytest.raises(SummaryCallbackDeliveryError):
            publisher.publish(completed_result(), uuid4())

    assert calls == 1


@pytest.mark.parametrize(
    "base_url",
    [
        "http://customer-service.internal",
        "https://user:password@customer-service.internal",
        "https://customer-service.internal/path",
        "https://customer-service.internal?query=value",
    ],
)
def test_callback_rejects_non_origin_or_non_https_base_url(base_url: str) -> None:
    with httpx.Client() as client:
        with pytest.raises(ValueError):
            HttpSummaryResultPublisher(client, StaticTokenProvider(), base_url)
