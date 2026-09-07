import json
from pathlib import Path
from uuid import uuid4

import httpx
import pytest

from chapchap_customer_ai.contracts.models import (
    ConsultationSummaryCompleted,
    KnowledgeProcessingCompleted,
    KnowledgeSource,
)
from chapchap_customer_ai.knowledge.http import (
    HttpKnowledgeResultPublisher,
    HttpKnowledgeSourceFetcher,
)
from chapchap_customer_ai.summary.http import HttpSummaryResultPublisher


def test_presigned_source_does_not_inherit_credentials_or_query():
    seen = []

    def handler(req):
        seen.append(req)
        return httpx.Response(200, content=b"text", headers={"content-type": "text/plain"})

    with httpx.Client(
        transport=httpx.MockTransport(handler),
        auth=("private", "private"),
        cookies={"session": "private"},
        params={"userId": "999"},
    ) as client:
        fetcher = HttpKnowledgeSourceFetcher(client, {"minio.test"})
        assert (
            fetcher.fetch(
                KnowledgeSource(
                    downloadUrl="https://minio.test/doc?sig=test",
                    contentType="text/plain",
                    fileSize=4,
                )
            )
            == b"text"
        )
    assert str(seen[0].url) == "https://minio.test/doc?sig=test"
    assert "authorization" not in seen[0].headers and "cookie" not in seen[0].headers


@pytest.mark.parametrize(
    "kind,publisher,model",
    [
        ("knowledge", HttpKnowledgeResultPublisher, KnowledgeProcessingCompleted),
        ("summary", HttpSummaryResultPublisher, ConsultationSummaryCompleted),
    ],
)
def test_callback_uses_only_issued_service_identity(kind, publisher, model):
    fixture = json.loads(
        Path("tests/contract/fixtures/customer_ai_candidate_v1.json").read_text(encoding="utf-8")
    )
    seen = []

    class Tokens:
        def get_token(self):
            return "issued-test-token"

    def handler(req):
        seen.append(req)
        return httpx.Response(204)

    with httpx.Client(
        transport=httpx.MockTransport(handler),
        auth=("private", "private"),
        cookies={"session": "private"},
        params={"userId": "999"},
    ) as client:
        publisher(client, Tokens(), "https://customer.test").publish(
            model.model_validate(fixture[kind]["completed"]), uuid4()
        )
    assert not seen[0].url.query and "cookie" not in seen[0].headers
    assert seen[0].headers["authorization"] == "Bearer issued-test-token"
