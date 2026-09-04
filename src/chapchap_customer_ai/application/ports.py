from collections.abc import Sequence
from typing import Protocol

from chapchap_customer_ai.contracts.models import KnowledgeProcessingRequest


class TextExtractor(Protocol):
    def extract(self, source_url: str, content_type: str) -> str: ...


class Chunker(Protocol):
    def chunk(self, text: str, profile: str) -> Sequence[str]: ...


class Embedder(Protocol):
    def embed(self, texts: Sequence[str]) -> Sequence[Sequence[float]]: ...


class VectorStore(Protocol):
    def upsert_knowledge(
        self,
        request: KnowledgeProcessingRequest,
        chunks: Sequence[str],
    ) -> int: ...


class ServiceIdentityVerifier(Protocol):
    def verify(self, authorization: str, subject_assertion: str | None) -> None: ...
