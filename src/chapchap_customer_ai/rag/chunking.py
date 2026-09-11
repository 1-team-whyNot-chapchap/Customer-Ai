import re
from dataclasses import dataclass

from chapchap_customer_ai.rag.models import (
    ChunkDraft,
    DocumentSection,
    ExtractedDocument,
    RagCoreError,
    RagFailureCode,
)
from chapchap_customer_ai.rag.tokenization import TokenCounter

DEFAULT_MIN_TOKENS = 128
DEFAULT_MAX_TOKENS = 512
_SENTENCE_BOUNDARY = re.compile(r"(?<=[.!?…。！？])\s+")
_PARAGRAPH_BOUNDARY = re.compile(r"\n\s*\n+")


@dataclass(frozen=True, slots=True)
class HybridPolicyV1Chunker:
    token_counter: TokenCounter
    min_tokens: int = DEFAULT_MIN_TOKENS
    max_tokens: int = DEFAULT_MAX_TOKENS

    def __post_init__(self) -> None:
        if self.min_tokens <= 0 or self.max_tokens < self.min_tokens:
            raise RagCoreError(
                RagFailureCode.CHUNK_PROFILE_INVALID,
                "Chunk token bounds must be positive and ordered.",
            )

    def chunk(self, document: ExtractedDocument) -> tuple[ChunkDraft, ...]:
        drafts: list[ChunkDraft] = []
        for section in document.sections:
            drafts.extend(self._chunk_section(section))
        return tuple(drafts)

    def _chunk_section(self, section: DocumentSection) -> list[ChunkDraft]:
        units: list[str] = []
        for paragraph in _PARAGRAPH_BOUNDARY.split(section.text):
            normalized = self._normalize(paragraph)
            if not normalized:
                continue
            if self.token_counter.count(normalized) <= self.max_tokens:
                units.append(normalized)
            else:
                units.extend(self._split_oversized_paragraph(normalized))

        packed = self._pack(units)
        merged = self._merge_small_neighbors(packed)
        return [ChunkDraft(section.path, text) for text in merged]

    def _split_oversized_paragraph(self, paragraph: str) -> list[str]:
        sentences = [
            sentence.strip() for sentence in _SENTENCE_BOUNDARY.split(paragraph) if sentence.strip()
        ]
        units: list[str] = []
        for sentence in sentences:
            if self.token_counter.count(sentence) <= self.max_tokens:
                units.append(sentence)
            else:
                units.extend(self._split_at_word_boundaries(sentence))
        return self._pack(units)

    def _split_at_word_boundaries(self, text: str) -> list[str]:
        words = text.split()
        if not words:
            return []

        pieces: list[str] = []
        buffer: list[str] = []
        for word in words:
            candidate = " ".join([*buffer, word])
            if self.token_counter.count(candidate) <= self.max_tokens:
                buffer.append(word)
                continue
            if not buffer:
                raise RagCoreError(
                    RagFailureCode.TEXT_EXTRACTION_FAILED,
                    "A single token exceeds the configured chunk limit.",
                )
            pieces.append(" ".join(buffer))
            buffer = [word]
        if buffer:
            pieces.append(" ".join(buffer))
        return pieces

    def _pack(self, units: list[str]) -> list[str]:
        chunks: list[str] = []
        buffer = ""
        for unit in units:
            candidate = self._join(buffer, unit)
            if not buffer or self.token_counter.count(candidate) <= self.max_tokens:
                buffer = candidate
                continue
            chunks.append(buffer)
            buffer = unit
        if buffer:
            chunks.append(buffer)
        return chunks

    def _merge_small_neighbors(self, chunks: list[str]) -> list[str]:
        merged = list(chunks)
        index = 0
        while index < len(merged) - 1:
            candidate = self._join(merged[index], merged[index + 1])
            if (
                self.token_counter.count(merged[index]) < self.min_tokens
                and self.token_counter.count(candidate) <= self.max_tokens
            ):
                merged[index + 1] = candidate
                merged.pop(index)
                continue
            index += 1
        return merged

    @staticmethod
    def _join(left: str, right: str) -> str:
        return f"{left}\n\n{right}" if left else right

    @staticmethod
    def _normalize(text: str) -> str:
        return re.sub(r"[ \t]+", " ", text).strip()
