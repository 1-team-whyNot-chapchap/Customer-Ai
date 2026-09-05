import math

import pytest

from chapchap_customer_ai.rag.embeddings import MultilingualE5SmallEmbedder
from chapchap_customer_ai.rag.models import RagCoreError, RagFailureCode


class FakeEncoder:
    def __init__(self, dimensions: int = 3, *, error: Exception | None = None) -> None:
        self.dimensions = dimensions
        self.error = error
        self.calls: list[tuple[list[str], bool, bool]] = []

    def encode(
        self,
        sentences: list[str],
        *,
        normalize_embeddings: bool,
        convert_to_numpy: bool,
    ) -> list[list[float]]:
        self.calls.append((sentences, normalize_embeddings, convert_to_numpy))
        if self.error is not None:
            raise self.error
        return [[1.0 / math.sqrt(self.dimensions)] * self.dimensions for _ in sentences]


def test_e5_uses_distinct_prefixes_and_normalized_embeddings() -> None:
    encoder = FakeEncoder()
    embedder = MultilingualE5SmallEmbedder(encoder, dimensions=3)

    passages = embedder.embed_passages(["환불 정책", "배송 정책"])
    query = embedder.embed_query("환불할 수 있나요?")

    assert len(passages) == 2
    assert len(query) == 3
    assert encoder.calls == [
        (["passage: 환불 정책", "passage: 배송 정책"], True, False),
        (["query: 환불할 수 있나요?"], True, False),
    ]


def test_e5_rejects_wrong_dimensions_and_provider_failure() -> None:
    wrong_dimensions = MultilingualE5SmallEmbedder(FakeEncoder(dimensions=2), dimensions=3)
    failed = MultilingualE5SmallEmbedder(
        FakeEncoder(error=RuntimeError("provider details must not leak")), dimensions=3
    )

    with pytest.raises(RagCoreError) as dimension_error:
        wrong_dimensions.embed_query("query")
    with pytest.raises(RagCoreError) as provider_error:
        failed.embed_query("query")

    assert dimension_error.value.code == RagFailureCode.EMBEDDING_UNAVAILABLE
    assert provider_error.value.code == RagFailureCode.EMBEDDING_UNAVAILABLE
    assert "provider details" not in str(provider_error.value)


def test_e5_rejects_blank_input() -> None:
    embedder = MultilingualE5SmallEmbedder(FakeEncoder(), dimensions=3)

    with pytest.raises(ValueError, match="query"):
        embedder.embed_query("  ")
    with pytest.raises(ValueError, match="passage"):
        embedder.embed_passages(["valid", "  "])
