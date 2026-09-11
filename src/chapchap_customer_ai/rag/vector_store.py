import json
import math
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

from chapchap_customer_ai.rag.models import (
    KnowledgeChunk,
    RagCoreError,
    RagEvidence,
    RagFailureCode,
    RetrievedKnowledge,
)


class ChromaCollection(Protocol):
    def upsert(self, **kwargs: Any) -> None: ...

    def query(self, **kwargs: Any) -> Mapping[str, Any]: ...


@dataclass(frozen=True, slots=True)
class ChromaVectorStore:
    collection: ChromaCollection

    def upsert(
        self,
        chunks: Sequence[KnowledgeChunk],
        embeddings: Sequence[Sequence[float]],
    ) -> int:
        if not chunks:
            return 0
        if len(chunks) != len(embeddings):
            raise ValueError("chunks and embeddings must have the same length")
        if len({chunk.chunk_id for chunk in chunks}) != len(chunks):
            raise ValueError("chunk ids must be unique within one upsert request")

        try:
            self.collection.upsert(
                ids=[chunk.chunk_id for chunk in chunks],
                embeddings=[list(vector) for vector in embeddings],
                documents=[chunk.text for chunk in chunks],
                metadatas=[self._metadata(chunk) for chunk in chunks],
            )
        except Exception as error:
            raise RagCoreError(
                RagFailureCode.VECTOR_STORE_UNAVAILABLE,
                "Knowledge chunks could not be stored.",
            ) from error
        return len(chunks)

    def search(
        self,
        query_embedding: Sequence[float],
        allowed_knowledge_version_ids: Sequence[int],
        *,
        top_k: int = 5,
        similarity_threshold: float = 0.70,
    ) -> tuple[RetrievedKnowledge, ...]:
        version_ids = tuple(dict.fromkeys(allowed_knowledge_version_ids))
        if not version_ids or any(
            isinstance(version_id, bool) or not isinstance(version_id, int) or version_id <= 0
            for version_id in version_ids
        ):
            raise ValueError("allowed knowledge version ids must be positive and non-empty")
        if not query_embedding or any(
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(float(value))
            for value in query_embedding
        ):
            raise ValueError("query embedding must contain finite numeric values")
        if top_k <= 0:
            raise ValueError("top_k must be positive")
        if not 0.0 <= similarity_threshold <= 1.0:
            raise ValueError("similarity_threshold must be between 0.0 and 1.0")

        where: dict[str, Any]
        if len(version_ids) == 1:
            where = {"knowledgeVersionId": version_ids[0]}
        else:
            where = {"knowledgeVersionId": {"$in": list(version_ids)}}

        try:
            result = self.collection.query(
                query_embeddings=[list(query_embedding)],
                n_results=top_k,
                where=where,
                include=["documents", "metadatas", "distances"],
            )
            rows = self._rows(result)
        except RagCoreError:
            raise
        except Exception as error:
            raise RagCoreError(
                RagFailureCode.VECTOR_STORE_UNAVAILABLE,
                "Knowledge retrieval failed.",
            ) from error

        retrieved: list[RetrievedKnowledge] = []
        allowed = set(version_ids)
        for chunk_id, document, metadata, distance in rows:
            score = self._similarity(distance)
            if score < similarity_threshold:
                continue
            knowledge_version_id = self._positive_int(metadata, "knowledgeVersionId")
            if knowledge_version_id not in allowed:
                raise self._invalid_result("Chroma returned a disallowed knowledge version.")
            if self._text(metadata, "chunkProfile") != "HYBRID_POLICY_V1":
                raise self._invalid_result("Chroma returned an unsupported chunk profile.")
            section_path = self._section_path(metadata)
            evidence = RagEvidence(
                knowledge_version_id=knowledge_version_id,
                chunk_id=chunk_id,
                retrieval_rank=len(retrieved) + 1,
                retrieval_score=score,
            )
            retrieved.append(
                RetrievedKnowledge(
                    text=document,
                    section_path=section_path,
                    document_key=self._text(metadata, "documentKey"),
                    category=self._text(metadata, "category"),
                    version=self._text(metadata, "version"),
                    effective_from=self._text(metadata, "effectiveFrom"),
                    evidence=evidence,
                )
            )
        return tuple(retrieved)

    @staticmethod
    def _metadata(chunk: KnowledgeChunk) -> dict[str, str | int]:
        return {
            "knowledgeVersionId": chunk.knowledge_version_id,
            "chunkProfile": chunk.chunk_profile,
            "documentKey": chunk.document_key,
            "category": chunk.category,
            "version": chunk.version,
            "effectiveFrom": chunk.effective_from,
            "sectionPath": json.dumps(chunk.section_path, ensure_ascii=False),
            "ordinal": chunk.ordinal,
        }

    @classmethod
    def _rows(
        cls, result: Mapping[str, Any]
    ) -> tuple[tuple[str, str, Mapping[str, Any], float], ...]:
        try:
            ids = result["ids"][0]
            documents = result["documents"][0]
            metadatas = result["metadatas"][0]
            distances = result["distances"][0]
        except (KeyError, IndexError, TypeError) as error:
            raise cls._invalid_result("Chroma returned a malformed result.") from error
        if not (len(ids) == len(documents) == len(metadatas) == len(distances)):
            raise cls._invalid_result("Chroma result fields have different lengths.")
        if any(
            not isinstance(chunk_id, str)
            or not chunk_id.strip()
            or not isinstance(document, str)
            or not document.strip()
            or not isinstance(metadata, Mapping)
            for chunk_id, document, metadata in zip(ids, documents, metadatas, strict=True)
        ):
            raise cls._invalid_result("Chroma returned invalid chunk fields.")
        return tuple(zip(ids, documents, metadatas, distances, strict=True))

    @classmethod
    def _similarity(cls, distance: Any) -> float:
        if isinstance(distance, bool) or not isinstance(distance, (int, float)):
            raise cls._invalid_result("Chroma distance must be numeric.")
        numeric_distance = float(distance)
        if not math.isfinite(numeric_distance):
            raise cls._invalid_result("Chroma distance must be finite.")
        return min(1.0, max(0.0, 1.0 - numeric_distance))

    @classmethod
    def _positive_int(cls, metadata: Mapping[str, Any], key: str) -> int:
        value = metadata.get(key)
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise cls._invalid_result(f"Chroma metadata {key} must be a positive integer.")
        return value

    @classmethod
    def _text(cls, metadata: Mapping[str, Any], key: str) -> str:
        value = metadata.get(key)
        if not isinstance(value, str) or not value.strip():
            raise cls._invalid_result(f"Chroma metadata {key} must be non-blank text.")
        return value

    @classmethod
    def _section_path(cls, metadata: Mapping[str, Any]) -> tuple[str, ...]:
        try:
            raw = json.loads(cls._text(metadata, "sectionPath"))
        except json.JSONDecodeError as error:
            raise cls._invalid_result("Chroma sectionPath is not valid JSON.") from error
        if not isinstance(raw, list) or not raw or any(
            not isinstance(part, str) or not part.strip() for part in raw
        ):
            raise cls._invalid_result("Chroma sectionPath is invalid.")
        return tuple(raw)

    @staticmethod
    def _invalid_result(message: str) -> RagCoreError:
        return RagCoreError(RagFailureCode.VECTOR_STORE_UNAVAILABLE, message)


def create_persistent_chroma_vector_store(
    persist_directory: Path | None,
    collection_name: str = "customer_ai_knowledge_v1",
) -> ChromaVectorStore:
    if persist_directory is None:
        raise RagCoreError(
            RagFailureCode.VECTOR_STORE_UNAVAILABLE,
            "Chroma persistence is not configured.",
        )
    try:
        import chromadb

        client = chromadb.PersistentClient(path=str(persist_directory))
        collection = client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"},
        )
        if not collection.metadata or collection.metadata.get("hnsw:space") != "cosine":
            raise ValueError("The Chroma collection is not configured for cosine distance.")
    except Exception as error:
        raise RagCoreError(
            RagFailureCode.VECTOR_STORE_UNAVAILABLE,
            "The persistent Chroma collection could not be initialized.",
        ) from error
    return ChromaVectorStore(collection)
