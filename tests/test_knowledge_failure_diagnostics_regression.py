"""Knowledge lifecycle tests using fake external dependencies (no real AI/Chroma)."""
import json
from dataclasses import replace
from unittest.mock import Mock
from uuid import UUID

import pytest

from chapchap_customer_ai.contracts.models import (
    KnowledgeProcessingRequest, KnowledgeProcessingFailureCode,
)
from chapchap_customer_ai.knowledge.models import SourceFetchError, CallbackDeliveryError, JobRegistration
from chapchap_customer_ai.knowledge.services import KnowledgeProcessingService
from chapchap_customer_ai.rag.models import KnowledgeChunk, RagCoreError, RagFailureCode

REQUEST_ID = UUID("2225163f-0ae1-473c-a71d-74e4d38e8838")

@pytest.fixture
def knowledge_request():
    return KnowledgeProcessingRequest.model_validate({
        "schemaVersion": "1.0", "knowledgeVersionId": 7, "attempt": 1,
        "chunkProfile": "HYBRID_POLICY_V1",
        "source": {"downloadUrl": "https://minio.internal/doc?signature=TOP_SECRET",
                   "contentType": "text/markdown", "fileSize": 5},
        "metadata": {"documentKey": "policy", "sourceService": "SUBSCRIPTION",
                     "category": "POLICY", "version": "v1", "effectiveFrom": "2026-09-17T00:00:00+09:00"},
        "callback": {"resultUri": "/internal/v1/knowledge-processing-results"},
    })

@pytest.fixture
def service():
    chunk = KnowledgeChunk("knowledge-7-example", 7, "HYBRID_POLICY_V1", "policy",
                           "POLICY", "v1", "2026-09-17T00:00:00+09:00", ("정책",), 1, "hello")
    source = Mock(); source.fetch.return_value = b"hello"
    builder = Mock(); builder.build_chunks.return_value = (chunk,)
    indexer = Mock(); indexer.index.return_value = 1
    return KnowledgeProcessingService(Mock(), Mock(), source, builder, indexer, Mock(), Mock())


def details(caplog):
    return [json.loads(r.getMessage()) for r in caplog.records
            if r.name == "chapchap_customer_ai.knowledge.services"]


def result(service):
    return service.result_publisher.publish.call_args.args[0]


def test_success_still_publishes_completed_after_indexing(service, knowledge_request, caplog):
    service._process(9, REQUEST_ID, knowledge_request)
    assert result(service).status == "COMPLETED"
    assert result(service).chunk_count == 1
    assert service.diagnostics.emit.call_args.args[0].event_type == "KNOWLEDGE_COMPLETED"
    assert details(caplog) == []


@pytest.mark.parametrize("message,reason", [
    ("The knowledge source is not allowed.", "SOURCE_NOT_ALLOWED"),
    ("The knowledge source could not be fetched.", "FETCH_UNAVAILABLE"),
    ("The knowledge source content type does not match.", "CONTENT_TYPE_MISMATCH"),
    ("The knowledge source size does not match.", "SIZE_MISMATCH"),
    ("The knowledge source exceeds the allowed size.", "SIZE_LIMIT_EXCEEDED"),
    ("The knowledge source size is invalid.", "INVALID_SIZE"),
    ("URL=https://host?signature=TOP_SECRET", "SOURCE_FETCH_ERROR"),
])
def test_source_failure_records_safe_reason_without_raw_url(service, knowledge_request, caplog, message, reason):
    service.source_fetcher.fetch.side_effect = SourceFetchError(message)
    service._process(9, REQUEST_ID, knowledge_request)
    assert result(service).failure_code == KnowledgeProcessingFailureCode.SOURCE_FETCH_FAILED
    assert result(service).retryable is True
    detail = details(caplog)[0]
    assert detail["stage"] == "SOURCE_FETCH"
    assert detail["sourceReason"] == reason
    assert detail["requestId"] == str(REQUEST_ID)
    assert "TOP_SECRET" not in caplog.text
    service.chunk_builder.build_chunks.assert_not_called()
    service.indexer.index.assert_not_called()


@pytest.mark.parametrize("code,stage,retryable", [
    (RagFailureCode.TEXT_EXTRACTION_FAILED, "CHUNK_BUILD", False),
    (RagFailureCode.UNSUPPORTED_DOCUMENT, "CHUNK_BUILD", False),
    (RagFailureCode.ENCRYPTED_DOCUMENT, "CHUNK_BUILD", False),
    (RagFailureCode.CHUNK_PROFILE_INVALID, "CHUNK_BUILD", False),
    (RagFailureCode.EMBEDDING_UNAVAILABLE, "EMBEDDING_AND_STORE", True),
    (RagFailureCode.VECTOR_STORE_UNAVAILABLE, "EMBEDDING_AND_STORE", True),
])
def test_rag_failure_code_and_retry_policy_are_preserved(service, knowledge_request, caplog, code, stage, retryable):
    error = RagCoreError(code, "document body TOP_SECRET")
    error.__cause__ = ValueError("presigned URL TOP_SECRET")
    if stage == "CHUNK_BUILD":
        service.chunk_builder.build_chunks.side_effect = error
    else:
        service.indexer.index.side_effect = error
    service._process(9, REQUEST_ID, knowledge_request)
    assert result(service).failure_code == code.value
    assert result(service).retryable is retryable
    detail = details(caplog)[0]
    assert detail["stage"] == stage
    assert detail["causeType"] == "ValueError"
    assert "TOP_SECRET" not in caplog.text


def test_unexpected_error_has_type_but_no_secret(service, knowledge_request, caplog):
    service.indexer.index.side_effect = RuntimeError("Bearer TOP_SECRET")
    service._process(9, REQUEST_ID, knowledge_request)
    assert result(service).failure_code == "CUSTOMER_AI_UNAVAILABLE"
    assert details(caplog)[0]["errorType"] == "RuntimeError"
    assert "TOP_SECRET" not in caplog.text


def test_timeout_keeps_existing_timeout_result(service, knowledge_request, caplog):
    service.indexer.index.side_effect = TimeoutError("TOP_SECRET")
    service._process(9, REQUEST_ID, knowledge_request)
    assert result(service).failure_code == "PROCESSING_TIMEOUT"
    assert result(service).retryable is True
    assert details(caplog)[0]["stage"] == "EMBEDDING_AND_STORE"


def test_partial_index_count_does_not_report_completed(service, knowledge_request, caplog):
    service.indexer.index.return_value = 0
    service._process(9, REQUEST_ID, knowledge_request)
    assert result(service).failure_code == "VECTOR_STORE_UNAVAILABLE"


def test_logging_failure_does_not_block_failed_callback(service, knowledge_request, monkeypatch):
    service.source_fetcher.fetch.side_effect = SourceFetchError("safe")
    def broken_logger(*args, **kwargs):
        raise RuntimeError("logger unavailable")
    monkeypatch.setattr("chapchap_customer_ai.knowledge.services._LOGGER.warning", broken_logger)
    service._process(9, REQUEST_ID, knowledge_request)
    assert result(service).status == "FAILED"
    service.result_publisher.publish.assert_called_once()


def test_callback_delivery_failure_is_not_reclassified_as_processing_failure(service, knowledge_request, caplog):
    service.result_publisher.publish.side_effect = CallbackDeliveryError("TOP_SECRET")
    with pytest.raises(CallbackDeliveryError):
        service._run_registered("7:HYBRID_POLICY_V1", 9, REQUEST_ID, knowledge_request)
    assert result(service).status == "COMPLETED"
    assert details(caplog)[0]["stage"] == "CALLBACK_DELIVERY"
    assert "failureCode" not in details(caplog)[0]
    assert "TOP_SECRET" not in caplog.text
    service.registry.release_attempt.assert_called_once_with("7:HYBRID_POLICY_V1", 1)
    service.result_publisher.publish.assert_called_once()


def test_diagnostic_sink_failure_does_not_block_completed_callback(service, knowledge_request):
    service.diagnostics.emit.side_effect = RuntimeError("sink failure")
    service._process(9, REQUEST_ID, knowledge_request)
    assert result(service).status == "COMPLETED"


def test_same_logical_job_retains_processing_id_across_attempts(service, knowledge_request):
    service.registry.register.return_value = JobRegistration(9, True)
    first = service.accept(knowledge_request, request_id=REQUEST_ID, idempotency_key="7:HYBRID_POLICY_V1")
    second_request = knowledge_request.model_copy(update={"attempt": 2})
    second = service.accept(second_request, request_id=UUID(int=5), idempotency_key="7:HYBRID_POLICY_V1")
    assert first.processing_id == second.processing_id == 9
    calls = service.registry.register.call_args_list
    assert calls[0].args[:2] == calls[1].args[:2]
    assert [call.args[2] for call in calls] == [1, 2]
