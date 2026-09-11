import re
from collections.abc import Sequence
from dataclasses import dataclass

from chapchap_customer_ai.consultation.models import GroundedAnswerDraft
from chapchap_customer_ai.rag.models import RetrievedKnowledge


@dataclass(frozen=True, slots=True)
class ConsultationGuardrails:
    max_context_characters: int = 20_000

    _instruction_patterns = (
        re.compile(r"ignore\s+(all\s+)?previous", re.IGNORECASE),
        re.compile(r"이전\s*(지시|명령).*(무시|삭제)"),
        re.compile(r"(system|developer)\s*prompt", re.IGNORECASE),
        re.compile(r"시스템\s*프롬프트"),
    )
    _exfiltration_patterns = (
        re.compile(
            r"(reveal|show|print|출력|공개).*(prompt|프롬프트|token|토큰|secret|키)",
            re.IGNORECASE,
        ),
        re.compile(r"authorization\s*:\s*bearer", re.IGNORECASE),
        re.compile(r"https?://[^\s]+/internal/", re.IGNORECASE),
    )

    def input_is_safe(self, message: str, conversation_context: Sequence[str]) -> bool:
        total_characters = len(message) + sum(len(item) for item in conversation_context)
        if total_characters > self.max_context_characters:
            return False
        return not self._high_risk((message, *conversation_context))

    def safe_evidence(
        self, evidence: Sequence[RetrievedKnowledge]
    ) -> tuple[RetrievedKnowledge, ...]:
        safe = tuple(item for item in evidence if not self._high_risk((item.text,)))
        versions_by_document: dict[str, set[str]] = {}
        for item in safe:
            versions_by_document.setdefault(item.document_key, set()).add(item.version)
        if any(len(versions) > 1 for versions in versions_by_document.values()):
            return ()
        return safe

    def validate_draft(
        self,
        draft: GroundedAnswerDraft,
        evidence: Sequence[RetrievedKnowledge],
    ) -> tuple[RetrievedKnowledge, ...]:
        if self._high_risk((draft.answer,)):
            return ()
        by_id = {item.evidence.chunk_id: item for item in evidence}
        if not draft.used_chunk_ids or any(
            chunk_id not in by_id for chunk_id in draft.used_chunk_ids
        ):
            return ()
        return tuple(by_id[chunk_id] for chunk_id in draft.used_chunk_ids)

    def output_text_is_safe(self, answer: str) -> bool:
        return bool(answer.strip()) and not self._high_risk((answer,))

    def _high_risk(self, texts: Sequence[str]) -> bool:
        combined = "\n".join(texts)
        instruction_hits = sum(
            bool(pattern.search(combined)) for pattern in self._instruction_patterns
        )
        exfiltration_hits = sum(
            bool(pattern.search(combined)) for pattern in self._exfiltration_patterns
        )
        return exfiltration_hits > 0 or instruction_hits >= 2
