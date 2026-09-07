from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Protocol


class Clock(Protocol):
    """JWT 수명 검증에 사용할 현재 시각을 제공한다."""

    def now_epoch_seconds(self) -> int: ...


@dataclass(frozen=True, slots=True)
class SystemClock:
    """UTC epoch seconds 기준의 시스템 시각을 제공한다."""

    def now_epoch_seconds(self) -> int:
        return int(datetime.now(UTC).timestamp())
