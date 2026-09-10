import json
from pathlib import Path
from uuid import uuid4

import httpx
import pytest

from chapchap_customer_ai.application.persistence import (
    PersistentKnowledgeJobRegistry,
    PersistentSummaryJobRegistry,
    RuntimeStore,
)
from chapchap_customer_ai.application.runtime import create_provider_runtime
from chapchap_customer_ai.contracts.models import KnowledgeProcessingRequest
from chapchap_customer_ai.core.settings import Settings
from chapchap_customer_ai.knowledge.http import HttpKnowledgeSourceFetcher
from chapchap_customer_ai.knowledge.models import KnowledgeRequestError, SourceFetchError
from chapchap_customer_ai.security.transport import allowed_url
from chapchap_customer_ai.summary.models import SummaryRequestError


@pytest.mark.parametrize(
    "url",
    [
        "http://auth-service.evil/jwks",
        "http://auth-service:81/jwks",
        "http://user@auth-service/jwks",
        "http://auth-service/jwks#x",
        "http://127.0.0.1/jwks",
        "http://169.254.169.254/latest",
        "file:///tmp/key",
        "http://auth-service:0/jwks",
        "http://auth-service:99999/jwks",
        "http://auth-service\\@evil/jwks",
        "http://auth-service\n/jwks",
    ],
)
def test_http_exception_is_exact_origin(url):
    assert not allowed_url(url, ("http://auth-service:80",))


def test_https_default_and_explicit_http():
    assert not allowed_url("http://auth-service/jwks")
    assert allowed_url("https://auth-service/jwks")
    assert allowed_url("http://auth-service/jwks", ("http://auth-service:80",))
    assert not allowed_url("http://auth-service/path", ("http://auth-service",), origin_only=True)


def test_durable_knowledge_identity_retry_completion_and_conflict(tmp_path):
    first = PersistentKnowledgeJobRegistry(RuntimeStore(tmp_path))
    original = first.register("1:HYBRID_POLICY_V1", "fp", 1)
    assert original.should_schedule
    assert not first.register("1:HYBRID_POLICY_V1", "fp", 1).should_schedule
    restarted = PersistentKnowledgeJobRegistry(RuntimeStore(tmp_path))
    retry = restarted.register("1:HYBRID_POLICY_V1", "fp", 1)
    assert retry.processing_id == original.processing_id and retry.should_schedule
    restarted.complete_attempt("1:HYBRID_POLICY_V1", 1)
    third = PersistentKnowledgeJobRegistry(RuntimeStore(tmp_path))
    assert not third.register("1:HYBRID_POLICY_V1", "fp", 1).should_schedule
    assert third.register("2:HYBRID_POLICY_V1", "fp2", 1).processing_id > original.processing_id
    with pytest.raises(KnowledgeRequestError):
        third.register("1:HYBRID_POLICY_V1", "changed", 2)


def test_summary_survives_restart_and_rejects_reused_job_id(tmp_path):
    first = PersistentSummaryJobRegistry(RuntimeStore(tmp_path))
    assert first.register("s1", 10, "fp").should_schedule
    second = PersistentSummaryJobRegistry(RuntimeStore(tmp_path))
    assert second.register("s1", 10, "fp").should_schedule
    second.complete("s1", 10)
    third = PersistentSummaryJobRegistry(RuntimeStore(tmp_path))
    assert not third.register("s1", 10, "fp").should_schedule
    with pytest.raises(SummaryRequestError):
        third.register("s2", 10, "fp")


def test_pending_request_survives_until_callback_completed(tmp_path):
    fixture = json.loads(
        Path("tests/contract/fixtures/customer_ai_candidate_v1.json").read_text(encoding="utf-8")
    )
    # Use a real schema fixture; no credentials are written to the journal.
    request_data = fixture["knowledge"]["request"]
    request = KnowledgeProcessingRequest.model_validate(request_data)
    key = f"{request.knowledge_version_id}:{request.chunk_profile}"
    store = RuntimeStore(tmp_path)
    registry = PersistentKnowledgeJobRegistry(store)
    registry.register(key, "fp", request.attempt)
    registry.record_request(key, uuid4(), request)
    restored = RuntimeStore(tmp_path)
    assert len(restored.pending()) == 1
    PersistentKnowledgeJobRegistry(restored).complete_attempt(key, request.attempt)
    assert restored.pending() == []


def test_academy_rejects_missing_persistent_storage():
    with pytest.raises(ValueError, match="persistent"):
        create_provider_runtime(
            Settings(
                _env_file=None,
                provider_runtime_mode="academy",
                environment="production",
                internal_security_enabled=True,
            )
        )


def test_minio_http_exception_does_not_follow_redirects():
    calls = []

    def respond(request):
        calls.append(request.url)
        return httpx.Response(302, headers={"location": "http://169.254.169.254/latest"})

    from chapchap_customer_ai.contracts.models import KnowledgeSource

    source = KnowledgeSource(
        downloadUrl="http://minio:9000/bucket/doc", contentType="text/plain", fileSize=4
    )
    with httpx.Client(transport=httpx.MockTransport(respond), follow_redirects=True) as client:
        fetcher = HttpKnowledgeSourceFetcher(
            client, ("minio",), http_allowed_origins=("http://minio:9000",)
        )
        with pytest.raises(SourceFetchError):
            fetcher.fetch(source)
    assert len(calls) == 1


def test_runtime_volume_refuses_concurrent_worker_and_reopens_after_close(tmp_path):
    from chapchap_customer_ai.application.persistence import claim_runtime_volume

    with claim_runtime_volume(tmp_path):
        with pytest.raises(ValueError, match="active worker"):
            claim_runtime_volume(tmp_path)
    with claim_runtime_volume(tmp_path):
        pass


def test_consultation_response_replayed_after_restart_without_llm_call(tmp_path):
    from chapchap_customer_ai.application.persistence import PersistentConsultationResponseRegistry
    from chapchap_customer_ai.consultation.models import ConsultationRequestError
    from chapchap_customer_ai.contracts.models import ConsultationResponse

    fixture = json.loads(
        Path("tests/contract/fixtures/customer_ai_candidate_v1.json").read_text(encoding="utf-8")
    )
    response = ConsultationResponse.model_validate(fixture["consultation"]["answer"])
    first = PersistentConsultationResponseRegistry(RuntimeStore(tmp_path))
    first.execute_once("request", "fingerprint", lambda: response)
    second = PersistentConsultationResponseRegistry(RuntimeStore(tmp_path))

    def unexpected_call():
        raise AssertionError("LLM must not run for a completed request")

    assert second.execute_once("request", "fingerprint", unexpected_call) == response
    with pytest.raises(ConsultationRequestError):
        second.execute_once("request", "different", unexpected_call)
