import hashlib
import json
import re
from dataclasses import dataclass

from chapchap_customer_ai.rag.chunking import HybridPolicyV1Chunker
from chapchap_customer_ai.rag.extraction import TextDocumentExtractor
from chapchap_customer_ai.rag.models import KnowledgeChunk, KnowledgeContext


@dataclass(frozen=True, slots=True)
class RagCoreService:
    extractor: TextDocumentExtractor
    chunker: HybridPolicyV1Chunker

    def build_chunks(
        self,
        context: KnowledgeContext,
        content: bytes,
        content_type: str,
    ) -> tuple[KnowledgeChunk, ...]:
        document = self.extractor.extract(content, content_type)
        drafts = self.chunker.chunk(document)
        return tuple(
            KnowledgeChunk(
                chunk_id=self._stable_chunk_id(context, draft.section_path, ordinal, draft.text),
                knowledge_version_id=context.knowledge_version_id,
                chunk_profile=context.chunk_profile,
                document_key=context.document_key,
                category=context.category,
                version=context.version,
                effective_from=context.effective_from,
                section_path=draft.section_path,
                ordinal=ordinal,
                text=draft.text,
            )
            for ordinal, draft in enumerate(drafts, start=1)
        )

    @staticmethod
    def _stable_chunk_id(
        context: KnowledgeContext,
        section_path: tuple[str, ...],
        ordinal: int,
        text: str,
    ) -> str:
        payload = {
            "chunkProfile": context.chunk_profile,
            "knowledgeVersionId": context.knowledge_version_id,
            "normalizedText": re.sub(r"\s+", " ", text).strip(),
            "ordinal": ordinal,
            "sectionPath": list(section_path),
        }
        digest = hashlib.sha256(
            json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode(
                "utf-8"
            )
        ).hexdigest()
        return f"knowledge-{context.knowledge_version_id}-{digest}"
