import re
from io import BytesIO

from pypdf import PdfReader

from chapchap_customer_ai.rag.models import (
    DocumentSection,
    ExtractedDocument,
    RagCoreError,
    RagFailureCode,
)

MARKDOWN_CONTENT_TYPE = "text/markdown"
TEXT_CONTENT_TYPE = "text/plain"
PDF_CONTENT_TYPE = "application/pdf"
_HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


class TextDocumentExtractor:
    """PDF, UTF-8 Markdown, 일반 텍스트를 문서 Section으로 정규화한다."""

    def extract(self, content: bytes, content_type: str) -> ExtractedDocument:
        normalized_content_type = content_type.split(";", maxsplit=1)[0].strip().lower()
        if normalized_content_type == MARKDOWN_CONTENT_TYPE:
            return self._extract_markdown(content)
        if normalized_content_type == TEXT_CONTENT_TYPE:
            return self._extract_plain_text(content)
        if normalized_content_type == PDF_CONTENT_TYPE:
            return self._extract_pdf(content)
        raise RagCoreError(
            RagFailureCode.UNSUPPORTED_DOCUMENT,
            f"Unsupported content type: {normalized_content_type}",
        )

    @staticmethod
    def _decode(content: bytes) -> str:
        try:
            text = content.decode("utf-8-sig")
        except UnicodeDecodeError as error:
            raise RagCoreError(
                RagFailureCode.TEXT_EXTRACTION_FAILED,
                "Knowledge text must be UTF-8 encoded.",
            ) from error
        return text.replace("\r\n", "\n").replace("\r", "\n").strip()

    def _extract_plain_text(self, content: bytes) -> ExtractedDocument:
        text = self._decode(content)
        if not text:
            raise RagCoreError(
                RagFailureCode.TEXT_EXTRACTION_FAILED,
                "The document does not contain extractable text.",
            )
        return ExtractedDocument((DocumentSection(("document",), text),))

    def _extract_markdown(self, content: bytes) -> ExtractedDocument:
        text = self._decode(content)
        if not text:
            raise RagCoreError(
                RagFailureCode.TEXT_EXTRACTION_FAILED,
                "The document does not contain extractable text.",
            )

        sections: list[DocumentSection] = []
        heading_stack: list[str] = []
        buffered_lines: list[str] = []

        def flush() -> None:
            section_text = "\n".join(buffered_lines).strip()
            if section_text:
                sections.append(DocumentSection(tuple(heading_stack or ["document"]), section_text))
            buffered_lines.clear()

        for line in text.split("\n"):
            heading = _HEADING_PATTERN.match(line)
            if heading is None:
                buffered_lines.append(line)
                continue

            flush()
            level = len(heading.group(1))
            heading_stack[level - 1 :] = [heading.group(2).strip()]

        flush()
        return ExtractedDocument(tuple(sections))

    def _extract_pdf(self, content: bytes) -> ExtractedDocument:
        try:
            reader = PdfReader(BytesIO(content))
            if reader.is_encrypted:
                raise RagCoreError(
                    RagFailureCode.ENCRYPTED_DOCUMENT,
                    "Encrypted PDF documents are not supported.",
                )
            sections = tuple(
                DocumentSection((f"page-{page_number}",), text)
                for page_number, page in enumerate(reader.pages, start=1)
                if (text := (page.extract_text() or "").strip())
            )
            return ExtractedDocument(sections)
        except RagCoreError:
            raise
        except Exception as error:
            raise RagCoreError(
                RagFailureCode.TEXT_EXTRACTION_FAILED,
                "Unable to extract text from the PDF document.",
            ) from error
