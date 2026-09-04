from dataclasses import dataclass
from enum import StrEnum


class RagFailureCode(StrEnum):
    TEXT_EXTRACTION_FAILED = "TEXT_EXTRACTION_FAILED"
    UNSUPPORTED_DOCUMENT = "UNSUPPORTED_DOCUMENT"
    ENCRYPTED_DOCUMENT = "ENCRYPTED_DOCUMENT"
    CHUNK_PROFILE_INVALID = "CHUNK_PROFILE_INVALID"


class RagCoreError(ValueError):
    def __init__(self, code: RagFailureCode, message: str) -> None:
        super().__init__(message)
        self.code = code


@dataclass(frozen=True, slots=True)
class KnowledgeContext:
    knowledge_version_id: int
    chunk_profile: str
    document_key: str
    category: str
    version: str
    effective_from: str

    def __post_init__(self) -> None:
        if self.knowledge_version_id <= 0:
            raise ValueError("knowledge_version_id must be positive")
        if self.chunk_profile != "HYBRID_POLICY_V1":
            raise RagCoreError(
                RagFailureCode.CHUNK_PROFILE_INVALID,
                "Only HYBRID_POLICY_V1 is supported.",
            )
        for field_name in ("document_key", "category", "version", "effective_from"):
            if not getattr(self, field_name).strip():
                raise ValueError(f"{field_name} must not be blank")


@dataclass(frozen=True, slots=True)
class DocumentSection:
    path: tuple[str, ...]
    text: str

    def __post_init__(self) -> None:
        if not self.path or any(not part.strip() for part in self.path):
            raise ValueError("path must contain non-blank section names")
        if not self.text.strip():
            raise ValueError("section text must not be blank")


@dataclass(frozen=True, slots=True)
class ExtractedDocument:
    sections: tuple[DocumentSection, ...]

    def __post_init__(self) -> None:
        if not self.sections:
            raise RagCoreError(
                RagFailureCode.TEXT_EXTRACTION_FAILED,
                "The document does not contain extractable text.",
            )


@dataclass(frozen=True, slots=True)
class ChunkDraft:
    section_path: tuple[str, ...]
    text: str


@dataclass(frozen=True, slots=True)
class KnowledgeChunk:
    chunk_id: str
    knowledge_version_id: int
    chunk_profile: str
    document_key: str
    category: str
    version: str
    effective_from: str
    section_path: tuple[str, ...]
    ordinal: int
    text: str


@dataclass(frozen=True, slots=True)
class RagEvidence:
    knowledge_version_id: int
    chunk_id: str
    retrieval_rank: int
    retrieval_score: float

    def __post_init__(self) -> None:
        if self.knowledge_version_id <= 0:
            raise ValueError("knowledge_version_id must be positive")
        if not self.chunk_id.strip():
            raise ValueError("chunk_id must not be blank")
        if self.retrieval_rank <= 0:
            raise ValueError("retrieval_rank must be positive")
        if not 0.0 <= self.retrieval_score <= 1.0:
            raise ValueError("retrieval_score must be between 0.0 and 1.0")
