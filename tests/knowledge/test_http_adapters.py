from uuid import uuid4

import httpx
import pytest

from chapchap_customer_ai.contracts.models import (
    KnowledgeProcessingCompleted,
    KnowledgeSource,
)
from chapchap_customer_ai.knowledge.http import (
    HttpKnowledgeResultPublisher,
    HttpKnowledgeSourceFetcher,
)
from chapchap_customer_ai.knowledge.models import CallbackDeliveryError, SourceFetchError


class StaticTokenProvider:
    def get_token(self) -> str:
        return "signed.service.jwt"


def source(url: str = "https://private-minio.example/policy?secret=value") -> KnowledgeSource:
    return KnowledgeSource(download_url=url, content_type="text/plain", file_size=4)


def test_source_fetcher_uses_get_and_validates_type_and_size() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            200,
            headers={"Content-Type": "text/plain; charset=utf-8", "Content-Length": "4"},
            content=b"text",
        )

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        fetcher = HttpKnowledgeSourceFetcher(client, {"private-minio.example"})
        assert fetcher.fetch(source()) == b"text"

    assert requests[0].method == "GET"


@pytest.mark.parametrize(
    "candidate",
    [
        "http://private-minio.example/policy",
        "https://other.example/policy",
        "https://user:password@private-minio.example/policy",
        "https://private-minio.example/policy#fragment",
    ],
)
def test_source_fetcher_rejects_untrusted_urls_without_request(candidate: str) -> None:
    def unexpected(request: httpx.Request) -> httpx.Response:
        raise AssertionError("network request must not be made")

    with httpx.Client(transport=httpx.MockTransport(unexpected)) as client:
        fetcher = HttpKnowledgeSourceFetcher(client, {"private-minio.example"})
        with pytest.raises(SourceFetchError) as error:
            fetcher.fetch(source(candidate))

    assert candidate not in str(error.value)


def test_source_fetcher_rejects_redirect_and_mismatched_body() -> None:
    responses = iter(
        [
            httpx.Response(302, headers={"Location": "https://other.example/secret"}),
            httpx.Response(200, headers={"Content-Type": "text/plain"}, content=b"too-long"),
        ]
    )

    def handler(request: httpx.Request) -> httpx.Response:
        return next(responses)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        fetcher = HttpKnowledgeSourceFetcher(client, {"private-minio.example"})
        with pytest.raises(SourceFetchError):
            fetcher.fetch(source())
        with pytest.raises(SourceFetchError):
            fetcher.fetch(source())


def completed_result() -> KnowledgeProcessingCompleted:
    return KnowledgeProcessingCompleted(
        schema_version="1.0",
        processing_id=9001,
        knowledge_version_id=101,
        status="COMPLETED",
        chunk_count=1,
        chunk_profile="HYBRID_POLICY_V1",
    )


def test_callback_retries_5xx_and_sends_contract_headers() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(503 if len(requests) == 1 else 204)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        publisher = HttpKnowledgeResultPublisher(
            client,
            StaticTokenProvider(),
            "https://customer-service.internal",
            sleeper=lambda _: None,
        )
        request_id = uuid4()
        publisher.publish(completed_result(), request_id)

    assert len(requests) == 2
    assert requests[-1].url.path == "/internal/v1/knowledge-processing-results"
    assert requests[-1].headers["authorization"] == "Bearer signed.service.jwt"
    assert requests[-1].headers["x-request-id"] == str(request_id)
    assert requests[-1].headers["idempotency-key"] == "9001"
    assert b'"chunkCount":1' in requests[-1].content


def test_callback_does_not_retry_contract_or_auth_failure() -> None:
    calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        return httpx.Response(403)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        publisher = HttpKnowledgeResultPublisher(
            client,
            StaticTokenProvider(),
            "https://customer-service.internal",
            sleeper=lambda _: None,
        )
        with pytest.raises(CallbackDeliveryError):
            publisher.publish(completed_result(), uuid4())

    assert calls == 1
