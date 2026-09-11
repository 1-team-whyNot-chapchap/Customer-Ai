import re
from io import BytesIO

import pytest
from pypdf import PdfWriter
from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject

from chapchap_customer_ai.rag.chunking import (
    DEFAULT_MAX_TOKENS,
    DEFAULT_MIN_TOKENS,
    HybridPolicyV1Chunker,
)
from chapchap_customer_ai.rag.extraction import TextDocumentExtractor
from chapchap_customer_ai.rag.models import KnowledgeContext, RagCoreError, RagFailureCode
from chapchap_customer_ai.rag.services import RagCoreService


class WordCounter:
    def count(self, text: str) -> int:
        return len(re.findall(r"\S+", text))


def make_pdf_bytes(*, encrypted: bool = False, with_text: bool = True) -> bytes:
    writer = PdfWriter()
    page = writer.add_blank_page(width=612, height=792)
    if with_text:
        font = DictionaryObject(
            {
                NameObject("/Type"): NameObject("/Font"),
                NameObject("/Subtype"): NameObject("/Type1"),
                NameObject("/BaseFont"): NameObject("/Helvetica"),
            }
        )
        font_reference = writer._add_object(font)
        page[NameObject("/Resources")] = DictionaryObject(
            {NameObject("/Font"): DictionaryObject({NameObject("/F1"): font_reference})}
        )
        stream = DecodedStreamObject()
        stream.set_data(b"BT /F1 12 Tf 72 720 Td (Refund policy) Tj ET")
        page[NameObject("/Contents")] = writer._add_object(stream)
    if encrypted:
        writer.encrypt("secret")
    output = BytesIO()
    writer.write(output)
    return output.getvalue()


@pytest.fixture
def service() -> RagCoreService:
    return RagCoreService(
        TextDocumentExtractor(), HybridPolicyV1Chunker(WordCounter(), min_tokens=3, max_tokens=5)
    )


@pytest.fixture
def context() -> KnowledgeContext:
    return KnowledgeContext(
        101, "HYBRID_POLICY_V1", "refund-policy", "REFUND", "2026.09", "2026-09-03T00:00:00Z"
    )


def test_hybrid_policy_defaults_match_the_approved_policy() -> None:
    assert DEFAULT_MIN_TOKENS == 128
    assert DEFAULT_MAX_TOKENS == 512


def test_markdown_sections_do_not_merge_across_headings(
    service: RagCoreService, context: KnowledgeContext
) -> None:
    chunks = service.build_chunks(
        context, b"# Refund\none two three\n\n# Delivery\nfour five six", "text/markdown"
    )

    assert [chunk.section_path for chunk in chunks] == [("Refund",), ("Delivery",)]
    assert [chunk.text for chunk in chunks] == ["one two three", "four five six"]


def test_oversized_paragraph_splits_at_sentence_boundaries(
    service: RagCoreService, context: KnowledgeContext
) -> None:
    chunks = service.build_chunks(
        context, b"one two three. four five six. seven eight nine.", "text/plain"
    )

    assert [chunk.text for chunk in chunks] == [
        "one two three.",
        "four five six.",
        "seven eight nine.",
    ]


def test_same_input_makes_stable_chunk_ids(
    service: RagCoreService, context: KnowledgeContext
) -> None:
    first = service.build_chunks(context, b"one two three", "text/plain")
    second = service.build_chunks(context, b"one two three", "text/plain")
    changed_version = service.build_chunks(
        KnowledgeContext(
            102, "HYBRID_POLICY_V1", "refund-policy", "REFUND", "2026.09", "2026-09-03T00:00:00Z"
        ),
        b"one two three",
        "text/plain",
    )

    assert first[0].chunk_id == second[0].chunk_id
    assert first[0].chunk_id != changed_version[0].chunk_id


def test_empty_and_unsupported_documents_are_rejected(
    service: RagCoreService, context: KnowledgeContext
) -> None:
    with pytest.raises(RagCoreError) as empty_error:
        service.build_chunks(context, b"   ", "text/plain")
    with pytest.raises(RagCoreError) as unsupported_error:
        service.build_chunks(context, b"binary", "image/png")

    assert empty_error.value.code == RagFailureCode.TEXT_EXTRACTION_FAILED
    assert unsupported_error.value.code == RagFailureCode.UNSUPPORTED_DOCUMENT


def test_pdf_text_is_extracted_into_page_sections(
    service: RagCoreService, context: KnowledgeContext
) -> None:
    chunks = service.build_chunks(context, make_pdf_bytes(), "application/pdf")

    assert [chunk.section_path for chunk in chunks] == [("page-1",)]
    assert chunks[0].text == "Refund policy"


def test_encrypted_pdf_is_rejected(service: RagCoreService, context: KnowledgeContext) -> None:
    with pytest.raises(RagCoreError) as encrypted_error:
        service.build_chunks(context, make_pdf_bytes(encrypted=True), "application/pdf")

    assert encrypted_error.value.code == RagFailureCode.ENCRYPTED_DOCUMENT


def test_pdf_without_extractable_text_is_rejected(
    service: RagCoreService, context: KnowledgeContext
) -> None:
    with pytest.raises(RagCoreError) as empty_error:
        service.build_chunks(context, make_pdf_bytes(with_text=False), "application/pdf")

    assert empty_error.value.code == RagFailureCode.TEXT_EXTRACTION_FAILED
