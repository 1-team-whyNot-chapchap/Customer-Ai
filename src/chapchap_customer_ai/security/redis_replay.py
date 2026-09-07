from collections.abc import Sequence
from dataclasses import dataclass
from hashlib import sha256
from typing import Protocol
from urllib.parse import urlsplit

from chapchap_customer_ai.core.settings import Settings
from chapchap_customer_ai.security.replay import InMemoryReplayStore, ReplayEntry, ReplayStore


class RedisReplayClient(Protocol):
    def eval(self, script: str, numkeys: int, *keys_and_args: object) -> object: ...

    def close(self) -> object: ...


_RESERVE_SCRIPT = """
for index = 1, #KEYS do
  if redis.call('EXISTS', KEYS[index]) == 1 then
    return 0
  end
end
for index = 1, #KEYS do
  redis.call('SET', KEYS[index], '1', 'EXAT', ARGV[index], 'NX')
end
return 1
""".strip()


@dataclass(frozen=True, slots=True)
class RedisReplayStore:
    """여러 Runtime이 공유하는 Redis 기반 원자적 replay 저장소다."""

    client: RedisReplayClient
    key_prefix: str = "chapchap:customer-ai:replay"

    def __post_init__(self) -> None:
        if not self.key_prefix or any(character.isspace() for character in self.key_prefix):
            raise ValueError("replay key prefix must be non-empty and contain no whitespace")

    def reserve(self, entries: Sequence[ReplayEntry], now: int) -> bool:
        if not entries or len({entry.key for entry in entries}) != len(entries):
            raise ValueError("replay entries must be non-empty and unique")
        if any(not entry.key or entry.expires_at <= now for entry in entries):
            raise ValueError("replay entries must have a future expiry")

        keys = tuple(self._redis_key(entry.key) for entry in entries)
        expirations = tuple(entry.expires_at for entry in entries)
        result = self.client.eval(_RESERVE_SCRIPT, len(keys), *keys, *expirations)
        if result not in {0, 1, False, True}:
            raise RuntimeError("replay store returned an invalid reservation result")
        return bool(result)

    def close(self) -> None:
        self.client.close()

    def _redis_key(self, value: str) -> str:
        digest = sha256(value.encode("utf-8")).hexdigest()
        return f"{self.key_prefix}:{digest}"


def create_replay_store(settings: Settings) -> ReplayStore:
    """환경 계약에 따라 replay 저장소를 만들고 운영에서는 Redis를 강제한다."""

    if settings.replay_redis_url:
        _validate_redis_url(settings.replay_redis_url, settings.environment)
        from redis import Redis

        client = Redis.from_url(
            settings.replay_redis_url,
            socket_connect_timeout=settings.replay_redis_socket_timeout_seconds,
            socket_timeout=settings.replay_redis_socket_timeout_seconds,
            retry_on_timeout=False,
            decode_responses=False,
        )
        return RedisReplayStore(client, settings.replay_key_prefix)
    if settings.environment.lower() in {"local", "test"}:
        return InMemoryReplayStore()
    raise RuntimeError("Distributed replay protection is not configured.")


def _validate_redis_url(url: str, environment: str) -> None:
    try:
        parsed = urlsplit(url)
    except (TypeError, ValueError):
        raise RuntimeError("Replay Redis URL is invalid.") from None
    allowed_schemes = (
        {"redis", "rediss"} if environment.lower() in {"local", "test"} else {"rediss"}
    )
    if parsed.scheme not in allowed_schemes or not parsed.hostname or parsed.fragment:
        raise RuntimeError("Replay Redis URL is invalid.")
