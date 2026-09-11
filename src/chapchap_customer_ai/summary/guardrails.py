import re
from collections.abc import Sequence
from dataclasses import dataclass

from chapchap_customer_ai.contracts.models import ConsultationSummaryMessage


@dataclass(frozen=True, slots=True)
class SummaryGuardrails:
    max_messages: int = 100
    max_context_characters: int = 50_000
    max_summary_characters: int = 10_000

    _instruction_patterns = (
        re.compile(r"ignore\s+(all\s+)?previous", re.IGNORECASE),
        re.compile(r"이전\s*(지시|명령).*(무시|삭제)"),
        re.compile(r"(system|developer)\s*prompt", re.IGNORECASE),
        re.compile(r"시스템\s*프롬프트"),
    )
    _secret_patterns = (
        re.compile(r"authorization\s*:\s*bearer", re.IGNORECASE),
        re.compile(r"(reveal|show|print|출력|공개).*(token|토큰|secret|비밀|키)", re.IGNORECASE),
        re.compile(r"https?://[^\s]+/internal/", re.IGNORECASE),
    )

    def __post_init__(self) -> None:
        if min(
            self.max_messages,
            self.max_context_characters,
            self.max_summary_characters,
        ) <= 0:
            raise ValueError("summary guard limits must be positive")

    def input_is_safe(self, messages: Sequence[ConsultationSummaryMessage]) -> bool:
        if not messages or len(messages) > self.max_messages:
            return False
        texts = tuple(message.content for message in messages)
        if sum(len(text) for text in texts) > self.max_context_characters:
            return False
        return not self._high_risk(texts)

    def output_is_safe(self, summary: str) -> bool:
        return (
            bool(summary.strip())
            and len(summary) <= self.max_summary_characters
            and not self._high_risk((summary,))
        )

    def _high_risk(self, texts: Sequence[str]) -> bool:
        combined = "\n".join(texts)
        instruction_hits = sum(
            bool(pattern.search(combined)) for pattern in self._instruction_patterns
        )
        return any(pattern.search(combined) for pattern in self._secret_patterns) or (
            instruction_hits >= 2
        )
