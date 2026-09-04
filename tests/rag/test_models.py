import pytest

from chapchap_customer_ai.rag.models import KnowledgeContext, RagCoreError, RagEvidence


def test_knowledge_context_rejects_non_positive_version_id() -> None:
    with pytest.raises(ValueError, match="positive"):
        KnowledgeContext(
            0, "HYBRID_POLICY_V1", "refund", "REFUND", "2026.09", "2026-09-03T00:00:00Z"
        )


def test_knowledge_context_rejects_unknown_chunk_profile() -> None:
    with pytest.raises(RagCoreError) as error:
        KnowledgeContext(1, "CUSTOM", "refund", "REFUND", "2026.09", "2026-09-03T00:00:00Z")

    assert error.value.code == "CHUNK_PROFILE_INVALID"


def test_evidence_allows_only_external_trace_fields() -> None:
    evidence = RagEvidence(101, "knowledge-101-hash", 1, 0.84)

    assert evidence.knowledge_version_id == 101
    assert evidence.retrieval_score == 0.84
