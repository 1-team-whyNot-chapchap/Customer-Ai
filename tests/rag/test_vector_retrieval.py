from dataclasses import asdict
from pathlib import Path
from typing import Any

import pytest

from chapchap_customer_ai.rag.models import (
    KnowledgeChunk,
    RagCoreError,
    RagFailureCode,
)
from chapchap_customer_ai.rag.retrieval import VectorRetrievalService
from chapchap_customer_ai.rag.vector_store import (
    ChromaVectorStore,
    create_persistent_chroma_vector_store,
)


def make_chunk(chunk_id: str, version_id: int = 101) -> KnowledgeChunk:
    return KnowledgeChunk(
        chunk_id=chunk_id,
        knowledge_version_id=version_id,
        chunk_profile="HYBRID_POLICY_V1",
        document_key="refund-policy",
        category="REFUND",
        version="2026.09",
        effective_from="2026-09-03T00:00:00Z",
        section_path=("환불", "기한"),
        ordinal=1,
        text="환불은 결제일로부터 7일 이내 가능합니다.",
    )


class FakeCollection:
    def __init__(self) -> None:
        self.records: dict[str, dict[str, Any]] = {}
        self.query_result: dict[str, Any] = {
            "ids": [[]],
            "documents": [[]],
            "metadatas": [[]],
            "distances": [[]],
        }
        self.query_call: dict[str, Any] | None = None
        self.failure: Exception | None = None

    def upsert(self, **kwargs: Any) -> None:
        if self.failure is not None:
            raise self.failure
        for index, chunk_id in enumerate(kwargs["ids"]):
            self.records[chunk_id] = {
                "embedding": kwargs["embeddings"][index],
                "document": kwargs["documents"][index],
                "metadata": kwargs["metadatas"][index],
            }

    def query(self, **kwargs: Any) -> dict[str, Any]:
        if self.failure is not None:
            raise self.failure
        self.query_call = kwargs
        return self.query_result


class FakeEmbedder:
    dimensions = 3

    def __init__(self) -> None:
        self.passages: list[str] = []
        self.query: str | None = None

    def embed_passages(self, texts: list[str]) -> tuple[tuple[float, ...], ...]:
        self.passages = list(texts)
        return tuple((1.0, 0.0, 0.0) for _ in texts)

    def embed_query(self, text: str) -> tuple[float, ...]:
        self.query = text
        return (1.0, 0.0, 0.0)


def test_same_stable_chunk_id_is_upserted_without_duplicates() -> None:
    collection = FakeCollection()
    service = VectorRetrievalService(FakeEmbedder(), ChromaVectorStore(collection))
    chunk = make_chunk("knowledge-101-stable")

    assert service.index([chunk]) == 1
    assert service.index([chunk]) == 1

    assert list(collection.records) == ["knowledge-101-stable"]
    metadata = collection.records[chunk.chunk_id]["metadata"]
    assert metadata == {
        "knowledgeVersionId": 101,
        "chunkProfile": "HYBRID_POLICY_V1",
        "documentKey": "refund-policy",
        "category": "REFUND",
        "version": "2026.09",
        "effectiveFrom": "2026-09-03T00:00:00Z",
        "sectionPath": '["환불", "기한"]',
        "ordinal": 1,
    }


def test_search_applies_version_filter_top_k_threshold_and_safe_evidence() -> None:
    collection = FakeCollection()
    chunk = make_chunk("knowledge-101-a")
    second = make_chunk("knowledge-102-b", 102)
    collection.query_result = {
        "ids": [[chunk.chunk_id, second.chunk_id, "knowledge-101-low"]],
        "documents": [[chunk.text, second.text, "threshold 아래 본문"]],
        "metadatas": [[
            ChromaVectorStore._metadata(chunk),
            ChromaVectorStore._metadata(second),
            ChromaVectorStore._metadata(make_chunk("knowledge-101-low")),
        ]],
        "distances": [[0.10, 0.25, 0.31]],
    }
    service = VectorRetrievalService(FakeEmbedder(), ChromaVectorStore(collection))

    results = service.retrieve("환불 정책", [101, 102])

    assert [result.evidence.retrieval_score for result in results] == [0.9, 0.75]
    assert [result.evidence.retrieval_rank for result in results] == [1, 2]
    assert collection.query_call == {
        "query_embeddings": [[1.0, 0.0, 0.0]],
        "n_results": 5,
        "where": {"knowledgeVersionId": {"$in": [101, 102]}},
        "include": ["documents", "metadatas", "distances"],
    }
    assert set(asdict(results[0].evidence)) == {
        "knowledge_version_id",
        "chunk_id",
        "retrieval_rank",
        "retrieval_score",
    }


def test_single_version_uses_equality_filter() -> None:
    collection = FakeCollection()
    service = VectorRetrievalService(FakeEmbedder(), ChromaVectorStore(collection))

    assert service.retrieve("정책", [101]) == ()
    assert collection.query_call is not None
    assert collection.query_call["where"] == {"knowledgeVersionId": 101}


def test_embedding_and_chroma_failures_are_fail_closed() -> None:
    collection = FakeCollection()
    collection.failure = RuntimeError("database detail")
    service = VectorRetrievalService(FakeEmbedder(), ChromaVectorStore(collection))

    with pytest.raises(RagCoreError) as error:
        service.index([make_chunk("knowledge-101-a")])

    assert error.value.code == RagFailureCode.VECTOR_STORE_UNAVAILABLE
    assert "database detail" not in str(error.value)


def test_malformed_or_disallowed_results_are_not_returned() -> None:
    collection = FakeCollection()
    collection.query_result = {
        "ids": [["knowledge-999-a"]],
        "documents": [["다른 버전 본문"]],
        "metadatas": [[ChromaVectorStore._metadata(make_chunk("knowledge-999-a", 999))]],
        "distances": [[0.1]],
    }
    service = VectorRetrievalService(FakeEmbedder(), ChromaVectorStore(collection))

    with pytest.raises(RagCoreError) as error:
        service.retrieve("정책", [101])

    assert error.value.code == RagFailureCode.VECTOR_STORE_UNAVAILABLE


def test_empty_version_allowlist_is_rejected_before_embedding() -> None:
    embedder = FakeEmbedder()
    service = VectorRetrievalService(embedder, ChromaVectorStore(FakeCollection()))

    with pytest.raises(ValueError, match="must not be empty"):
        service.retrieve("정책", [])

    assert embedder.query is None


@pytest.mark.parametrize("version_ids", [[True], [0], [-1]])
def test_invalid_version_allowlist_is_rejected(version_ids: list[int]) -> None:
    store = ChromaVectorStore(FakeCollection())

    with pytest.raises(ValueError, match="positive"):
        store.search((1.0, 0.0, 0.0), version_ids)


def test_invalid_query_embedding_is_rejected() -> None:
    store = ChromaVectorStore(FakeCollection())

    with pytest.raises(ValueError, match="finite"):
        store.search((float("nan"),), [101])


def test_persistent_chroma_requires_an_explicit_path() -> None:
    with pytest.raises(RagCoreError) as error:
        create_persistent_chroma_vector_store(None)

    assert error.value.code == RagFailureCode.VECTOR_STORE_UNAVAILABLE
    assert not Path("customer_ai_knowledge_v1").exists()


def test_adapter_round_trips_with_real_in_memory_chroma() -> None:
    import chromadb

    client = chromadb.Client()
    collection = client.create_collection(
        "vector_retrieval_contract_test",
        metadata={"hnsw:space": "cosine"},
    )
    store = ChromaVectorStore(collection)
    chunks = [make_chunk("knowledge-101-a"), make_chunk("knowledge-102-b", 102)]

    assert store.upsert(chunks, [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0)]) == 2
    assert store.upsert(chunks[:1], [(1.0, 0.0, 0.0)]) == 1
    assert collection.count() == 2

    results = store.search(
        (1.0, 0.0, 0.0),
        [101],
        top_k=5,
        similarity_threshold=0.70,
    )

    assert len(results) == 1
    assert results[0].evidence.chunk_id == "knowledge-101-a"
    assert results[0].evidence.retrieval_score == pytest.approx(1.0)
