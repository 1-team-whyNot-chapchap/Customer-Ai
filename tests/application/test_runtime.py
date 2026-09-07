import json
import time
from threading import Event
from uuid import uuid4

import httpx
import jwt
import pytest
from cryptography.hazmat.primitives.asymmetric import rsa
from fastapi.testclient import TestClient
from pydantic import SecretStr

from chapchap_customer_ai.application.runtime import (
    ProviderRuntimeDependencies,
    create_isolated_app,
    create_provider_runtime,
)
from chapchap_customer_ai.core.settings import Settings
from chapchap_customer_ai.rag.chunking import HybridPolicyV1Chunker
from chapchap_customer_ai.rag.extraction import TextDocumentExtractor
from chapchap_customer_ai.rag.retrieval import VectorRetrievalService
from chapchap_customer_ai.rag.services import RagCoreService
from chapchap_customer_ai.rag.vector_store import ChromaVectorStore
from chapchap_customer_ai.security.jwt_verifier import InternalSecurityVerifier
from chapchap_customer_ai.security.keys import StaticVerificationKeyResolver


def settings(**changes):
    return Settings(
        _env_file=None,
        **{
            "environment": "test",
            "provider_runtime_mode": "isolated",
            "internal_security_enabled": True,
            "auth_token_base_url": "https://auth.test",
            "auth_client_id": "ai-test",
            "auth_client_secret": SecretStr("test-secret"),
            "deepseek_api_key": SecretStr("test-key"),
            "knowledge_callback_base_url": "https://customer.test",
            "summary_callback_base_url": "https://customer.test",
            "knowledge_source_allowed_hosts": ("minio.test",),
            **changes,
        },
    )


@pytest.mark.parametrize(
    "changes",
    [
        {"environment": "production"},
        {"provider_runtime_mode": "disabled"},
        {"internal_security_enabled": False},
        {"auth_client_secret": None},
        {"deepseek_api_key": None},
        {"knowledge_source_allowed_hosts": ()},
    ],
)
def test_runtime_rejects_incomplete_or_unsafe_activation(changes):
    with pytest.raises(ValueError):
        create_provider_runtime(settings(**changes))


class TestEmbedding:
    def embed_passages(self, texts):
        return [[1.0, 0.0] for text in texts]

    def embed_query(self, text):
        return [1.0, 0.0]


class TestTokens:
    def count(self, text):
        return len(text.split())


class Collection:
    def __init__(self):
        self.rows = {}
        self.filters = []

    def upsert(self, ids, documents, metadatas, embeddings):
        self.rows.update(
            {key: (doc, meta) for key, doc, meta in zip(ids, documents, metadatas, strict=True)}
        )

    def query(self, *, where, n_results, **kwargs):
        self.filters.append(where)
        allowed = where["knowledgeVersionId"]
        allowed = allowed["$in"] if isinstance(allowed, dict) else [allowed]
        rows = [
            (key, doc, meta)
            for key, (doc, meta) in self.rows.items()
            if meta["knowledgeVersionId"] in allowed
        ][:n_results]
        return {
            "ids": [[r[0] for r in rows]],
            "documents": [[r[1] for r in rows]],
            "metadatas": [[r[2] for r in rows]],
            "distances": [[0.1 for r in rows]],
        }


def security():
    auth = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    verifier = InternalSecurityVerifier(
        StaticVerificationKeyResolver(
            {
                ("chapchap-auth-service", "auth-test"): auth.public_key(),
                ("chapchap-customer-service", "subject-test"): subject.public_key(),
            }
        )
    )
    return verifier, auth, subject


def headers(auth, subject, request_id, key, scopes=None):
    now = int(time.time())
    service_token = jwt.encode(
        {
            "iss": "chapchap-auth-service",
            "sub": "customer-service",
            "aud": "chapchap-customer-ai",
            "scope": "customer-ai.invoke",
            "iat": now - 1,
            "exp": now + 299,
            "jti": str(uuid4()),
        },
        auth,
        algorithm="RS256",
        headers={"kid": "auth-test"},
    )
    assertion = jwt.encode(
        {
            "iss": "chapchap-customer-service",
            "aud": "chapchap-customer-ai",
            "userId": 42,
            "role": "CUSTOMER",
            "allowedAiScopes": scopes or ["customer-ai.policy.read"],
            "requestId": str(request_id),
            "consultationId": 501,
            "iat": now - 1,
            "exp": now + 59,
            "jti": str(uuid4()),
            "kid": "subject-test",
        },
        subject,
        algorithm="RS256",
        headers={"kid": "subject-test"},
    )
    return {
        "Authorization": f"Bearer {service_token}",
        "X-Subject-Assertion": assertion,
        "X-Request-Id": str(request_id),
        "Idempotency-Key": key,
    }


def test_authenticated_knowledge_consultation_summary_flow_and_shutdown():
    verifier, auth, subject = security()
    collection = Collection()
    callbacks = []
    llm_calls = []
    auth_calls = []
    done = Event()
    text = "환불은 결제 후 7일 이내 가능합니다."

    def source(req):
        assert "authorization" not in req.headers and "cookie" not in req.headers
        return httpx.Response(200, content=text.encode(), headers={"Content-Type": "text/plain"})

    def token(req):
        auth_calls.append(req)
        return httpx.Response(
            200,
            json={
                "access_token": "callback-test",
                "token_type": "Bearer",
                "expires_in": 300,
                "scope": "customer-ai.callback",
            },
        )

    def llm(req):
        llm_calls.append(req)
        data = json.loads(json.loads(req.content)["messages"][1]["content"])
        result = (
            {"answer": text, "usedChunkIds": [data["evidence"][0]["chunkId"]]}
            if "evidence" in data
            else {"summary": "환불 정책 안내를 요청하여 7일 기준을 안내함."}
        )
        return httpx.Response(
            200,
            json={
                "choices": [
                    {
                        "finish_reason": "stop",
                        "message": {
                            "role": "assistant",
                            "content": json.dumps(result, ensure_ascii=False),
                        },
                    }
                ]
            },
        )

    def callback(req):
        assert req.headers["authorization"] == "Bearer callback-test"
        callbacks.append((req.url.path, json.loads(req.content)))
        done.set()
        return httpx.Response(204)

    deps = ProviderRuntimeDependencies(
        verifier=verifier,
        retrieval=VectorRetrievalService(TestEmbedding(), ChromaVectorStore(collection)),
        chunk_builder=RagCoreService(TextDocumentExtractor(), HybridPolicyV1Chunker(TestTokens())),
        http_transports={
            name: httpx.MockTransport(handler)
            for name, handler in {
                "source": source,
                "auth": token,
                "llm": llm,
                "callback": callback,
            }.items()
        },
    )
    app = create_isolated_app(settings(), deps)
    request_id = uuid4()
    with TestClient(app) as client:
        knowledge = {
            "schemaVersion": "1.0",
            "knowledgeVersionId": 101,
            "attempt": 1,
            "source": {
                "downloadUrl": "https://minio.test/policy?signature=test",
                "contentType": "text/plain",
                "fileSize": len(text.encode()),
            },
            "metadata": {
                "documentKey": "refund",
                "sourceService": "subscription-service",
                "category": "REFUND",
                "version": "1",
                "effectiveFrom": "2026-09-07T00:00:00+09:00",
            },
            "chunkProfile": "HYBRID_POLICY_V1",
            "callback": {"resultUri": "/internal/v1/knowledge-processing-results"},
        }
        response = client.post(
            "/internal/v1/knowledge-processings",
            json=knowledge,
            headers=headers(auth, subject, request_id, "101:HYBRID_POLICY_V1"),
        )
        assert response.status_code == 202
        assert done.wait(5)
        assert callbacks[0][1]["status"] == "COMPLETED"
        done.clear()
        consultation = {
            "schemaVersion": "1.0",
            "requestId": str(request_id),
            "consultationId": 501,
            "triggerMessageId": 9002,
            "subject": {
                "userId": 42,
                "role": "CUSTOMER",
                "allowedAiScopes": ["customer-ai.policy.read"],
            },
            "message": "환불 정책",
            "conversationContext": [],
            "knowledgeVersionIds": [101],
        }
        response = client.post(
            "/internal/v1/consultation-responses",
            json=consultation,
            headers=headers(auth, subject, request_id, "consultation-1"),
        )
        assert response.status_code == 200, response.text
        assert response.json()["decision"] == "ANSWER"
        assert response.json()["evidence"][0]["knowledgeVersionId"] == 101
        assert collection.filters == [{"knowledgeVersionId": 101}]
        # Repeated request returns stored answer without another paid generation.
        assert (
            client.post(
                "/internal/v1/consultation-responses",
                json=consultation,
                headers=headers(auth, subject, request_id, "consultation-1"),
            ).json()
            == response.json()
        )
        assert len(llm_calls) == 1
        invalid = headers(auth, subject, request_id, "forged")
        invalid["Authorization"] = "Bearer invalid"
        assert (
            client.post(
                "/internal/v1/consultation-responses", json=consultation, headers=invalid
            ).status_code
            == 401
        )
        assert len(llm_calls) == 1
        summary = {
            "schemaVersion": "1.0",
            "summaryJobId": 11,
            "consultationId": 501,
            "messages": [{"senderType": "USER", "content": "환불 정책 알려주세요"}],
            "callback": {"resultUri": "/internal/v1/consultation-summary-results"},
        }
        assert (
            client.post(
                "/internal/v1/consultation-summaries",
                json=summary,
                headers=headers(auth, subject, request_id, "summary-11"),
            ).status_code
            == 202
        )
        assert done.wait(5)
    assert len(callbacks) == 2 and callbacks[1][1]["status"] == "COMPLETED"
    assert len(callbacks[1][1]["summary"]) <= 500
    assert len(auth_calls) == 1 and len(llm_calls) == 2
    with pytest.raises(RuntimeError):
        app.state.provider_runtime.knowledge.scheduler.submit(lambda: None)


def test_initialization_failure_closes_created_http_clients():
    verifier, _, _ = security()

    class ClosingTransport(httpx.MockTransport):
        closed = False

        def close(self):
            self.closed = True

    transport = ClosingTransport(lambda req: httpx.Response(500))
    deps = ProviderRuntimeDependencies(verifier=verifier, http_transports={"auth": transport})
    with pytest.raises(ValueError):
        create_provider_runtime(settings(deepseek_model="unapproved"), deps)
    assert transport.closed
