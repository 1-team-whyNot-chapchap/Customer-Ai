"""Token boundary regression. No network or embedding-model download."""
import pytest
from chapchap_customer_ai.rag.chunking import HybridPolicyV1Chunker
from chapchap_customer_ai.rag.models import (
    DocumentSection, ExtractedDocument, RagCoreError, RagFailureCode,
)

class CharacterCounter:
    def count(self, text: str) -> int:
        return len(text)


def chunk(text, max_tokens=16):
    return HybridPolicyV1Chunker(CharacterCounter(), min_tokens=4, max_tokens=max_tokens).chunk(
        ExtractedDocument((DocumentSection(("정책",), text),))
    )


@pytest.mark.parametrize("text", ["x" * 17, "ok " + "x" * 17,
                                  "ok " + "x" * 17 + " end", "ok fine " + "x" * 17])
def test_oversized_word_is_rejected_regardless_of_position(text):
    with pytest.raises(RagCoreError) as caught:
        chunk(text)
    assert caught.value.code == RagFailureCode.TEXT_EXTRACTION_FAILED


@pytest.mark.parametrize("text", ["alpha beta gamma delta", "alpha. beta. gamma. delta.",
                                  "one\n\ntwo\n\nthree\n\nfour", "가나다 라마바 사아자 차카타",
                                  "x" * 16, "ok " + "x" * 16])
def test_valid_words_never_produce_oversized_chunks(text):
    chunks = chunk(text)
    assert chunks
    assert all(0 < len(c.text) <= 16 for c in chunks)
    assert " ".join(" ".join(c.text.split()) for c in chunks) == " ".join(text.split())


def test_section_boundaries_are_preserved():
    document = ExtractedDocument((DocumentSection(("A",), "short"),
                                  DocumentSection(("B",), "other")))
    chunks = HybridPolicyV1Chunker(CharacterCounter()).chunk(document)
    assert [c.section_path for c in chunks] == [("A",), ("B",)]
