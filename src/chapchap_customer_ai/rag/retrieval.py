from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol

from chapchap_customer_ai.core.settings import Settings
from chapchap_customer_ai.rag.embeddings import EmbeddingModel, MultilingualE5SmallEmbedder
from chapchap_customer_ai.rag.models import (
    KnowledgeChunk,
    RagCoreError,
    RagFailureCode,
    RetrievedKnowledge,
)
from chapchap_customer_ai.rag.vector_store import create_persistent_chroma_vector_store


class KnowledgeVectorStore(Protocol):
    def upsert(
        self,
        chunks: Sequence[KnowledgeChunk],
        embeddings: Sequence[Sequence[float]],
    ) -> int: ...

    def search(
        self,
        query_embedding: Sequence[float],
        allowed_knowledge_version_ids: Sequence[int],
        *,
        top_k: int,
        similarity_threshold: float,
    ) -> tuple[RetrievedKnowledge, ...]: ...


@dataclass(frozen=True, slots=True)
class VectorRetrievalService:
    embedder: EmbeddingModel
    vector_store: KnowledgeVectorStore
    top_k: int = 5
    similarity_threshold: float = 0.70

    def __post_init__(self) -> None:
        if self.top_k <= 0:
            raise ValueError("top_k must be positive")
        if not 0.0 <= self.similarity_threshold <= 1.0:
            raise ValueError("similarity_threshold must be between 0.0 and 1.0")

    def index(self, chunks: Sequence[KnowledgeChunk]) -> int:
        embeddings = self.embedder.embed_passages([chunk.text for chunk in chunks])
        return self.vector_store.upsert(chunks, embeddings)

    def retrieve(
        self, query: str, allowed_knowledge_version_ids: Sequence[int]
    ) -> tuple[RetrievedKnowledge, ...]:
        if not query.strip():
            raise ValueError("query must not be blank")
        if not allowed_knowledge_version_ids:
            raise ValueError("allowed knowledge version ids must not be empty")
        query_embedding = self.embedder.embed_query(query)
        return self.vector_store.search(
            query_embedding,
            allowed_knowledge_version_ids,
            top_k=self.top_k,
            similarity_threshold=self.similarity_threshold,
        )


def create_vector_retrieval_service(settings: Settings) -> VectorRetrievalService:
    if (
        settings.rag_embedding_model != MultilingualE5SmallEmbedder.model_id
        or settings.rag_embedding_dimensions != 384
    ):
        raise RagCoreError(
            RagFailureCode.EMBEDDING_UNAVAILABLE,
            "The configured embedding model does not match the approved architecture.",
        )
    vector_store = create_persistent_chroma_vector_store(
        settings.chroma_persist_directory,
        settings.chroma_collection_name,
    )
    embedder = MultilingualE5SmallEmbedder.from_pretrained(
        dimensions=settings.rag_embedding_dimensions
    )
    return VectorRetrievalService(
        embedder,
        vector_store,
        top_k=settings.rag_top_k,
        similarity_threshold=settings.rag_similarity_threshold,
    )
