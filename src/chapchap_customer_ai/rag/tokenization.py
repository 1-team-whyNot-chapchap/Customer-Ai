from dataclasses import dataclass
from typing import Protocol


class TokenCounter(Protocol):
    """활성 RAG 런타임에서 선택한 토크나이저로 토큰 수를 계산한다."""

    def count(self, text: str) -> int: ...


class EncoderTokenizer(Protocol):
    def encode(self, text: str, *, add_special_tokens: bool) -> list[int]: ...


@dataclass(frozen=True, slots=True)
class MultilingualE5TokenCounter:
    """확정된 임베딩 모델과 짝을 이루는 토크나이저로 청크 토큰 수를 계산한다."""

    tokenizer: EncoderTokenizer

    model_id = "intfloat/multilingual-e5-small"

    @classmethod
    def from_pretrained(cls) -> "MultilingualE5TokenCounter":
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained(cls.model_id)
        return cls(tokenizer)

    def count(self, text: str) -> int:
        return len(self.tokenizer.encode(text, add_special_tokens=False))
