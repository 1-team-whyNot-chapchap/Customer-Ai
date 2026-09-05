from collections.abc import Callable, Sequence
from typing import Protocol, TypeAlias
from uuid import UUID

from chapchap_customer_ai.contracts.models import (
    KnowledgeProcessingCompleted,
    KnowledgeProcessingFailed,
    KnowledgeSource,
)
from chapchap_customer_ai.knowledge.models import JobRegistration
from chapchap_customer_ai.rag.models import KnowledgeChunk, KnowledgeContext

KnowledgeResult: TypeAlias = KnowledgeProcessingCompleted | KnowledgeProcessingFailed


class KnowledgeSourceFetcher(Protocol):
    def fetch(self, source: KnowledgeSource) -> bytes: ...


class KnowledgeJobRegistry(Protocol):
    def register(self, logical_key: str, fingerprint: str, attempt: int) -> JobRegistration: ...

    def release_attempt(self, logical_key: str, attempt: int) -> None: ...


class JobScheduler(Protocol):
    def submit(self, task: Callable[[], None]) -> None: ...


class KnowledgeResultPublisher(Protocol):
    def publish(self, result: KnowledgeResult, request_id: UUID) -> None: ...


class RagChunkBuilder(Protocol):
    def build_chunks(
        self, context: KnowledgeContext, content: bytes, content_type: str
    ) -> Sequence[KnowledgeChunk]: ...


class KnowledgeIndexer(Protocol):
    def index(self, chunks: Sequence[KnowledgeChunk]) -> int: ...


class ServiceTokenProvider(Protocol):
    def get_token(self) -> str: ...
