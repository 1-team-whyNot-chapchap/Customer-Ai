from collections.abc import Sequence
from dataclasses import dataclass, field
from datetime import UTC, datetime
from threading import Lock
from typing import Protocol


@dataclass(frozen=True, slots=True)
class ReplayEntry:
    key: str
    expires_at: int


class ReplayStore(Protocol):
    def reserve(self, entries: Sequence[ReplayEntry], now: int) -> bool: ...


class Clock(Protocol):
    def now_epoch_seconds(self) -> int: ...


@dataclass(frozen=True, slots=True)
class SystemClock:
    def now_epoch_seconds(self) -> int:
        return int(datetime.now(UTC).timestamp())


@dataclass(slots=True)
class InMemoryReplayStore:
    """단일 프로세스 참조 구현. 운영 다중 인스턴스에는 분산 구현이 필요하다."""

    _entries: dict[str, int] = field(default_factory=dict)
    _lock: Lock = field(default_factory=Lock)

    def reserve(self, entries: Sequence[ReplayEntry], now: int) -> bool:
        if not entries or len({entry.key for entry in entries}) != len(entries):
            raise ValueError("replay entries must be non-empty and unique")
        if any(not entry.key or entry.expires_at <= now for entry in entries):
            raise ValueError("replay entries must have a future expiry")

        with self._lock:
            expired = [key for key, expires_at in self._entries.items() if expires_at <= now]
            for key in expired:
                del self._entries[key]
            if any(entry.key in self._entries for entry in entries):
                return False
            self._entries.update({entry.key: entry.expires_at for entry in entries})
            return True
