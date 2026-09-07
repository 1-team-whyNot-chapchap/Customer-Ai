"""Retrieval boundaries and parity with the frozen experimental implementation."""

import importlib.util
from pathlib import Path

import pytest

from chapchap_customer_ai.rag.local_policy_search import LocalSearchEngine


class Tokens:
    def encode(self, text, **kwargs):
        return text.split()


def chunk(cid, version=1, text="refund condition", ordinal=0, policy="POL-PAYMENT-012"):
    return {
        "chunk_id": cid,
        "knowledge_version_id": version,
        "document_key": "policy",
        "section_path": [policy],
        "ordinal": ordinal,
        "text": text,
    }


class Store:
    def __init__(self, ids):
        self.ids = ids

    def query(self, **kwargs):
        assert kwargs["where"] == {"knowledgeVersionId": {"$in": [1]}}
        return {"ids": [self.ids], "distances": [[0.1] * len(self.ids)]}

    def get(self, ids, **kwargs):
        assert ids, "An empty Chroma get must not be called"
        return {"ids": ids, "embeddings": [[1.0, 0.0] for _ in ids]}


def engine(chunks, hits, cls=LocalSearchEngine):
    return cls(Store(hits), chunks, Tokens(), {c["chunk_id"]: [1.0, 0.0] for c in chunks})


def test_parent_expansion_preserves_original_and_version_boundary():
    chunks = [chunk("a"), chunk("b", text="exception", ordinal=1), chunk("private", 2)]
    result = engine(chunks, ["a"]).search("refund", [1.0, 0.0], "R4", [1])
    assert [c["chunk_id"] for c in result["context"]] == ["a", "b"]
    assert result["context"][1]["text"] == "exception"
    assert "private" not in {c["chunkId"] for c in result["candidates"]}


def test_empty_candidates_return_no_evidence():
    result = engine([chunk("a")], []).search("unrelated", [1.0, 0.0], "R4", [1])
    assert result["decision"] == "NO_EVIDENCE"
    assert not result["context"]


@pytest.mark.parametrize("allowed", [[], [0], [True], [-1]])
def test_invalid_version_ids_rejected(allowed):
    with pytest.raises(ValueError, match="version IDs"):
        engine([chunk("a")], ["a"]).search("refund", [1.0, 0.0], "R4", allowed)


def test_forbidden_dense_result_rejected():
    with pytest.raises(ValueError, match="Disallowed"):
        engine([chunk("private", 2)], ["private"]).search("refund", [1.0, 0.0], "R1", [1])


def test_context_budget_records_omission():
    chunks = [chunk("large", text="token " * 6001), chunk("small", ordinal=1)]
    result = engine(chunks, ["large"]).search("refund", [1.0, 0.0], "R2", [1])
    assert result["omittedChunkIds"] == ["large"]
    assert result["contextTokens"] <= 6000


@pytest.mark.parametrize("method", ["R1", "R2", "R3", "R4"])
def test_runtime_matches_frozen_engine(method):
    path = Path(__file__).parents[1] / "scripts/benchmark_retrieval_engine.py"
    spec = importlib.util.spec_from_file_location("frozen_benchmark", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    chunks = [
        chunk("a"),
        chunk("b", text="refund exception", ordinal=1),
        chunk("c", policy="POL-SUB-001", text="subscription"),
    ]
    actual = engine(chunks, ["a", "c"]).search("refund", [1.0, 0.0], method, [1])
    expected = engine(chunks, ["a", "c"], module.LocalSearchEngine).search(
        "refund", [1.0, 0.0], method, [1]
    )
    assert actual == expected
