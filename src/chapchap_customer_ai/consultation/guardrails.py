import json
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
        re.compile(r"(?:프롬프트|토큰|비밀\s*키).*(?:출력|공개|보여|알려)"),
    )

    def input_is_safe(self, message: str, conversation_context: Sequence[str]) -> bool:
        total_characters = len(message) + sum(len(item) for item in conversation_context)
        if total_characters > self.max_context_characters:
            return False
        return not self._high_risk((message,))

    def safe_context(self, conversation_context: Sequence[str]) -> tuple[str, ...]:
        """Discard unsafe history and its preceding context so split attacks and
        stale restricted topics cannot affect a subsequent, safe user turn.
        The original request is still size-checked and bound by its fingerprint.
        """
        safe = []
        skip_reply = False
        for raw in conversation_context:
            try:
                item = json.loads(raw)
            except (ValueError, TypeError):
                item = None
            content = item.get("content", raw) if isinstance(item, dict) else raw
            if not isinstance(content, str):
                continue
            if any(
                p.search(content)
                for p in (*self._instruction_patterns, *self._exfiltration_patterns)
            ):
                safe.clear()
                skip_reply = True
                continue
            if skip_reply:
                if not isinstance(item, dict) or item.get("sender") != "USER":
                    continue
                skip_reply = False
            safe.append(raw)
        return tuple(safe)

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

    def dialogue_output_is_safe(self, answer: str) -> bool:
        # Conversational generation has no facts. Prefer the approved fallback
        # over factual-looking business claims, even when a negative claim is true.
        return self.output_text_is_safe(answer) and not re.search(
            r"\d|https?://|\]\(|javascript:|data:|(?:^|\s)/[a-zA-Z]|"
            r"(?:조회|처리|취소|연결).*(?:완료|했|됐|되었)|"
            r"(?:이동|열어|연결).*(?:드릴|드렸|줄게)|"
            r"연결.*(?:수\s*(?:는\s*)?없|불가|불가능)|"
            r"연결.*(?:건|것).*아니|"
            r"(?:배송|결제|환불|구독).*(?:상태|완료|중|금액|원|일)|"
            r"(?:밥|식사|점심|저녁).*(?:먹었|했어요|했습니다)",
            answer,
        )

    def state_output_is_safe(self, answer: str) -> bool:
        # State tools use only the signed subject; they cannot accept identity
        # information collected in chat as an alternate search key.
        return self.output_text_is_safe(answer) and not re.search(
            r"(?:이메일|메일\s*주소|전화번호|비밀번호|계정\s*정보|아이디|서비스명|상품명).{0,80}"
            r"(?:알려|보내|입력|제공|말씀)|"
            r"(?:알려|보내|입력|제공|말씀).{0,40}(?:이메일|전화번호|비밀번호|아이디)|"
            r"(?:어떤|신청한|신청하신)\s*(?:서비스|상품).*(?:알려|말씀|확인해)",
            answer,
            re.DOTALL,
        )

    def policy_output_is_safe(self, answer: str) -> bool:
        # A policy-only turn neither performs a personal lookup nor connects
        # an agent. Reject action promises while allowing optional guidance.
        return self.output_text_is_safe(answer) and not re.search(
            r"연결(?:을)?\s*(?:도와\s*)?(?:해\s*)?(?:드릴게|드리겠|하겠|할게|했|됐|완료)|"
            r"조회된\s*(?:결제|구독|배송|환불)\s*(?:건|기록|내역|정보)(?:이|가)?\s*없",
            answer,
        )

    def _high_risk(self, texts: Sequence[str]) -> bool:
        combined = "\n".join(texts)
        instruction_hits = sum(
            bool(pattern.search(combined)) for pattern in self._instruction_patterns
        )
        exfiltration_hits = sum(
            bool(pattern.search(combined)) for pattern in self._exfiltration_patterns
        )
        return exfiltration_hits > 0 or instruction_hits >= 2
