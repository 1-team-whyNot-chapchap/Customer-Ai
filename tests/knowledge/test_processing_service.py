from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from uuid import UUID, uuid4

import pytest

from chapchap_customer_ai.contracts.models import (
    KnowledgeProcessingFailureCode,
    KnowledgeProcessingRequest,
)
from chapchap_customer_ai.knowledge.idempotency import InMemoryKnowledgeJobRegistry
from chapchap_customer_ai.knowledge.models import KnowledgeRequestError, SourceFetchError
from chapchap_customer_ai.knowledge.ports import KnowledgeResult
from chapchap_customer_ai.knowledge.services import KnowledgeProcessingService
from chapchap_customer_ai.rag.models import (
    KnowledgeChunk,
    RagCoreError,
    RagFailureCode,
)


def request_payload(*, attempt: int = 1, url_suffix: str = "first", category: str = "REFUND"):
    return {
        "schemaVersion": "1.0",
        "knowledgeVersionId": 101,
        "attempt": attempt,
        "source": {
            "downloadUrl": f"https://private-minio.example/{url_suffix}?signature=secret",
            "contentType": "text/plain",
            "fileSize": 4,
        },
        "metadata": {
            "documentKey": "refund-policy",
            "sourceService": "subscription-service",
            "category": category,
            "version": "2026.09",
            "effectiveFrom": "2026-09-03T00:00:00Z",
        },
        "chunkProfile": "HYBRID_POLICY_V1",
        "callback": {"resultUri": "/internal/v1/knowledge-processing-results"},
    }


class InlineScheduler:
    def __init__(self) -> None:
        self.submissions = 0

    def submit(self, task: Callable[[], None]) -> None:
        self.submissions += 1
        task()


@dataclass
class StaticFetcher:
    content: bytes = b"text"
    error: Exception | None = None

    def fetch(self, source: object) -> bytes:
        if self.error:
            raise self.error
        return self.content


@dataclass
class StaticChunkBuilder:
    error: Exception | None = None

    def build_chunks(
        self, context: object, content: bytes, content_type: str
    ) -> Sequence[KnowledgeChunk]:
        if self.error:
            raise self.error
        return (
            KnowledgeChunk(
                "stable-id",
                101,
                "HYBRID_POLICY_V1",
                "refund-policy",
                "REFUND",
                "2026.09",
                "2026-09-03T00:00:00Z",
                ("root",),
                1,
                "text",
            ),
        )


@dataclass
class StaticIndexer:
    count: int = 1
    error: Exception | None = None

    def index(self, chunks: Sequence[KnowledgeChunk]) -> int:
        if self.error:
            raise self.error
        return self.count


@dataclass
class RecordingPublisher:
    results: list[KnowledgeResult] = field(default_factory=list)
    request_ids: list[UUID] = field(default_factory=list)

    def publish(self, result: KnowledgeResult, request_id: UUID) -> None:
        self.results.append(result)
        self.request_ids.append(request_id)


def make_service(
    *,
    registry: InMemoryKnowledgeJobRegistry | None = None,
    scheduler: InlineScheduler | None = None,
    fetcher: StaticFetcher | None = None,
    builder: StaticChunkBuilder | None = None,
    indexer: StaticIndexer | None = None,
    publisher: RecordingPublisher | None = None,
) -> tuple[KnowledgeProcessingService, InlineScheduler, RecordingPublisher]:
    actual_scheduler = scheduler or InlineScheduler()
    actual_publisher = publisher or RecordingPublisher()
    return (
        KnowledgeProcessingService(
            registry or InMemoryKnowledgeJobRegistry(starting_processing_id=9001),
            actual_scheduler,
            fetcher or StaticFetcher(),
            builder or StaticChunkBuilder(),
            indexer or StaticIndexer(),
            actual_publisher,
        ),
        actual_scheduler,
        actual_publisher,
    )


def test_success_publishes_minimal_completed_result() -> None:
    service, _, publisher = make_service()
    request_id = uuid4()

    accepted = service.accept(
        KnowledgeProcessingRequest.model_validate(request_payload()),
        request_id=request_id,
        idempotency_key="101:HYBRID_POLICY_V1",
    )

    assert accepted.processing_id == 9001
    assert publisher.results[0].model_dump(by_alias=True) == {
        "schemaVersion": "1.0",
        "processingId": 9001,
        "knowledgeVersionId": 101,
        "status": "COMPLETED",
        "chunkCount": 1,
        "chunkProfile": "HYBRID_POLICY_V1",
    }
    assert publisher.request_ids == [request_id]


def test_same_attempt_is_not_rescheduled_and_next_attempt_reuses_processing_id() -> None:
    service, scheduler, publisher = make_service()
    request_id = uuid4()

    first = service.accept(
        KnowledgeProcessingRequest.model_validate(request_payload()),
        request_id=request_id,
        idempotency_key="101:HYBRID_POLICY_V1",
    )
    duplicate = service.accept(
        KnowledgeProcessingRequest.model_validate(request_payload(url_suffix="rotated")),
        request_id=request_id,
        idempotency_key="101:HYBRID_POLICY_V1",
    )
    retry = service.accept(
        KnowledgeProcessingRequest.model_validate(
            request_payload(attempt=2, url_suffix="retry")
        ),
        request_id=request_id,
        idempotency_key="101:HYBRID_POLICY_V1",
    )

    assert first.processing_id == duplicate.processing_id == retry.processing_id
    assert scheduler.submissions == 2
    assert len(publisher.results) == 2


def test_idempotency_key_and_immutable_payload_conflicts_are_rejected() -> None:
    service, _, _ = make_service()
    request = KnowledgeProcessingRequest.model_validate(request_payload())

    with pytest.raises(KnowledgeRequestError) as key_error:
        service.accept(request, request_id=uuid4(), idempotency_key="wrong")
    service.accept(request, request_id=uuid4(), idempotency_key="101:HYBRID_POLICY_V1")
    with pytest.raises(KnowledgeRequestError) as conflict_error:
        service.accept(
            KnowledgeProcessingRequest.model_validate(request_payload(category="DELIVERY")),
            request_id=uuid4(),
            idempotency_key="101:HYBRID_POLICY_V1",
        )

    assert key_error.value.status_code == 400
    assert conflict_error.value.status_code == 409


@pytest.mark.parametrize(
    ("error", "expected_code", "retryable"),
    [
        (SourceFetchError("safe"), KnowledgeProcessingFailureCode.SOURCE_FETCH_FAILED, True),
        (
            RagCoreError(RagFailureCode.TEXT_EXTRACTION_FAILED, "safe"),
            KnowledgeProcessingFailureCode.TEXT_EXTRACTION_FAILED,
            False,
        ),
        (
            RagCoreError(RagFailureCode.UNSUPPORTED_DOCUMENT, "safe"),
            KnowledgeProcessingFailureCode.UNSUPPORTED_DOCUMENT,
            False,
        ),
        (
            RagCoreError(RagFailureCode.ENCRYPTED_DOCUMENT, "safe"),
            KnowledgeProcessingFailureCode.ENCRYPTED_DOCUMENT,
            False,
        ),
        (
            RagCoreError(RagFailureCode.EMBEDDING_UNAVAILABLE, "safe"),
            KnowledgeProcessingFailureCode.EMBEDDING_UNAVAILABLE,
            True,
        ),
        (
            RagCoreError(RagFailureCode.VECTOR_STORE_UNAVAILABLE, "safe"),
            KnowledgeProcessingFailureCode.VECTOR_STORE_UNAVAILABLE,
            True,
        ),
        (TimeoutError(), KnowledgeProcessingFailureCode.PROCESSING_TIMEOUT, True),
        (RuntimeError("private"), KnowledgeProcessingFailureCode.CUSTOMER_AI_UNAVAILABLE, True),
    ],
)
def test_failures_are_reduced_to_approved_callback_codes(
    error: Exception,
    expected_code: KnowledgeProcessingFailureCode,
    retryable: bool,
) -> None:
    fetcher = StaticFetcher(error=error) if isinstance(error, SourceFetchError) else StaticFetcher()
    builder = StaticChunkBuilder(error=error) if not isinstance(error, SourceFetchError) else None
    service, _, publisher = make_service(fetcher=fetcher, builder=builder)

    service.accept(
        KnowledgeProcessingRequest.model_validate(request_payload()),
        request_id=uuid4(),
        idempotency_key="101:HYBRID_POLICY_V1",
    )

    result = publisher.results[0]
    assert result.failure_code == expected_code
    assert result.retryable is retryable
    assert "private" not in str(result)
