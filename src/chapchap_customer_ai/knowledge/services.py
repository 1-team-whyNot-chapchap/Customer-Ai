import hashlib
import json
from dataclasses import dataclass
from uuid import UUID

from chapchap_customer_ai.contracts.models import (
    KnowledgeProcessingAccepted,
    KnowledgeProcessingCompleted,
    KnowledgeProcessingFailed,
    KnowledgeProcessingFailureCode,
    KnowledgeProcessingRequest,
)
from chapchap_customer_ai.knowledge.models import (
    RETRYABLE_FAILURES,
    KnowledgeRequestError,
    SourceFetchError,
)
from chapchap_customer_ai.knowledge.ports import (
    JobScheduler,
    KnowledgeIndexer,
    KnowledgeJobRegistry,
    KnowledgeResultPublisher,
    KnowledgeSourceFetcher,
    RagChunkBuilder,
)
from chapchap_customer_ai.rag.models import (
    KnowledgeContext,
    RagCoreError,
    RagFailureCode,
)


@dataclass(frozen=True, slots=True)
class KnowledgeProcessingService:
    registry: KnowledgeJobRegistry
    scheduler: JobScheduler
    source_fetcher: KnowledgeSourceFetcher
    chunk_builder: RagChunkBuilder
    indexer: KnowledgeIndexer
    result_publisher: KnowledgeResultPublisher

    def accept(
        self,
        request: KnowledgeProcessingRequest,
        *,
        request_id: UUID,
        idempotency_key: str,
    ) -> KnowledgeProcessingAccepted:
        logical_key = f"{request.knowledge_version_id}:{request.chunk_profile}"
        if idempotency_key != logical_key:
            raise KnowledgeRequestError(
                "Idempotency-Key must match knowledgeVersionId and chunkProfile."
            )
        registration = self.registry.register(
            logical_key, self._immutable_fingerprint(request), request.attempt
        )
        if registration.should_schedule:
            try:
                self.scheduler.submit(
                    lambda: self._process(registration.processing_id, request_id, request)
                )
            except Exception:
                self.registry.release_attempt(logical_key, request.attempt)
                raise KnowledgeRequestError(
                    "Knowledge processing is temporarily unavailable.", status_code=503
                ) from None
        return KnowledgeProcessingAccepted(
            schema_version="1.0",
            processing_id=registration.processing_id,
            knowledge_version_id=request.knowledge_version_id,
            status="ACCEPTED",
        )

    def _process(
        self, processing_id: int, request_id: UUID, request: KnowledgeProcessingRequest
    ) -> None:
        try:
            content = self.source_fetcher.fetch(request.source)
            context = KnowledgeContext(
                request.knowledge_version_id,
                request.chunk_profile,
                request.metadata.document_key,
                request.metadata.category,
                request.metadata.version,
                request.metadata.effective_from,
            )
            chunks = tuple(
                self.chunk_builder.build_chunks(context, content, request.source.content_type)
            )
            chunk_count = self.indexer.index(chunks)
            if chunk_count < 1 or chunk_count != len(chunks):
                raise RagCoreError(
                    RagFailureCode.VECTOR_STORE_UNAVAILABLE,
                    "Not all knowledge chunks were stored.",
                )
            result = KnowledgeProcessingCompleted(
                schema_version="1.0",
                processing_id=processing_id,
                knowledge_version_id=request.knowledge_version_id,
                status="COMPLETED",
                chunk_count=chunk_count,
                chunk_profile=request.chunk_profile,
            )
        except SourceFetchError:
            result = self._failed(
                processing_id,
                request.knowledge_version_id,
                KnowledgeProcessingFailureCode.SOURCE_FETCH_FAILED,
            )
        except TimeoutError:
            result = self._failed(
                processing_id,
                request.knowledge_version_id,
                KnowledgeProcessingFailureCode.PROCESSING_TIMEOUT,
            )
        except RagCoreError as error:
            try:
                failure_code = KnowledgeProcessingFailureCode(error.code)
            except ValueError:
                failure_code = KnowledgeProcessingFailureCode.CUSTOMER_AI_UNAVAILABLE
            result = self._failed(processing_id, request.knowledge_version_id, failure_code)
        except Exception:
            result = self._failed(
                processing_id,
                request.knowledge_version_id,
                KnowledgeProcessingFailureCode.CUSTOMER_AI_UNAVAILABLE,
            )
        self.result_publisher.publish(result, request_id)

    @staticmethod
    def _failed(
        processing_id: int,
        knowledge_version_id: int,
        failure_code: KnowledgeProcessingFailureCode,
    ) -> KnowledgeProcessingFailed:
        return KnowledgeProcessingFailed(
            schema_version="1.0",
            processing_id=processing_id,
            knowledge_version_id=knowledge_version_id,
            status="FAILED",
            failure_code=failure_code,
            retryable=failure_code in RETRYABLE_FAILURES,
        )

    @staticmethod
    def _immutable_fingerprint(request: KnowledgeProcessingRequest) -> str:
        payload = request.model_dump(by_alias=True, mode="json")
        payload.pop("attempt")
        source = payload["source"]
        if isinstance(source, dict):
            source.pop("downloadUrl")
        canonical = json.dumps(
            payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True
        ).encode("utf-8")
        return hashlib.sha256(canonical).hexdigest()
