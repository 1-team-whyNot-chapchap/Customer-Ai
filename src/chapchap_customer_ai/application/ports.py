from collections.abc import Collection, Sequence
from typing import Protocol
from uuid import UUID

from chapchap_customer_ai.contracts.models import KnowledgeProcessingRequest, UserRole
from chapchap_customer_ai.security.models import AuthenticatedContext


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
    def verify(
        self,
        authorization: str,
        subject_assertion: str,
        *,
        expected_request_id: UUID,
        expected_consultation_id: int,
        required_subject_scope: str,
        allowed_roles: Collection[UserRole],
    ) -> AuthenticatedContext: ...
