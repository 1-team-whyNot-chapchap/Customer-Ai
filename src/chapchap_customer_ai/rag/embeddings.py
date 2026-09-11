import math
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol

from chapchap_customer_ai.rag.models import RagCoreError, RagFailureCode


class SentenceEncoder(Protocol):
    def encode(
        self,
        sentences: list[str],
        *,
        normalize_embeddings: bool,
        convert_to_numpy: bool,
    ) -> Sequence[Sequence[float]]: ...


class EmbeddingModel(Protocol):
    dimensions: int

    def embed_passages(self, texts: Sequence[str]) -> tuple[tuple[float, ...], ...]: ...

    def embed_query(self, text: str) -> tuple[float, ...]: ...


@dataclass(frozen=True, slots=True)
class MultilingualE5SmallEmbedder:
    encoder: SentenceEncoder
    dimensions: int = 384

    model_id = "intfloat/multilingual-e5-small"
    passage_prefix = "passage: "
    query_prefix = "query: "

    @classmethod
    def from_pretrained(cls, dimensions: int = 384) -> "MultilingualE5SmallEmbedder":
        try:
            from sentence_transformers import SentenceTransformer

            return cls(SentenceTransformer(cls.model_id), dimensions=dimensions)
        except Exception as error:
            raise RagCoreError(
                RagFailureCode.EMBEDDING_UNAVAILABLE,
                "The local embedding model could not be loaded.",
            ) from error

    def embed_passages(self, texts: Sequence[str]) -> tuple[tuple[float, ...], ...]:
        if any(not text.strip() for text in texts):
            raise ValueError("passage text must not be blank")
        return self._encode([f"{self.passage_prefix}{text}" for text in texts])

    def embed_query(self, text: str) -> tuple[float, ...]:
        if not text.strip():
            raise ValueError("query text must not be blank")
        return self._encode([f"{self.query_prefix}{text}"])[0]

    def _encode(self, texts: list[str]) -> tuple[tuple[float, ...], ...]:
        if not texts:
            return ()
        try:
            raw_vectors = self.encoder.encode(
                texts,
                normalize_embeddings=True,
                convert_to_numpy=False,
            )
            vectors = tuple(tuple(float(value) for value in vector) for vector in raw_vectors)
        except Exception as error:
            raise RagCoreError(
                RagFailureCode.EMBEDDING_UNAVAILABLE,
                "The local embedding model failed to encode text.",
            ) from error

        if len(vectors) != len(texts):
            raise RagCoreError(
                RagFailureCode.EMBEDDING_UNAVAILABLE,
                "The embedding model returned an unexpected vector count.",
            )
        if any(
            len(vector) != self.dimensions or any(not math.isfinite(value) for value in vector)
            for vector in vectors
        ):
            raise RagCoreError(
                RagFailureCode.EMBEDDING_UNAVAILABLE,
                f"Embedding vectors must contain {self.dimensions} finite values.",
            )
        return vectors
