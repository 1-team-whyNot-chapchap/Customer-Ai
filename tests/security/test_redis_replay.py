from dataclasses import dataclass, field

import pytest

from chapchap_customer_ai.core.settings import Settings
from chapchap_customer_ai.security.redis_replay import RedisReplayStore, create_replay_store
from chapchap_customer_ai.security.replay import InMemoryReplayStore, ReplayEntry


@dataclass
class FakeRedisClient:
    result: object = 1
    calls: list[tuple[str, int, tuple[object, ...]]] = field(default_factory=list)
    closed: bool = False

    def eval(self, script: str, numkeys: int, *keys_and_args: object) -> object:
        self.calls.append((script, numkeys, keys_and_args))
        return self.result

    def close(self) -> None:
        self.closed = True


def test_redis_store_reserves_multiple_entries_atomically_until_each_expiry() -> None:
    client = FakeRedisClient()
    store = RedisReplayStore(client, "test:replay")

    assert store.reserve(
        [ReplayEntry("service:secret-jti", 120), ReplayEntry("subject:jti", 130)], 100
    )

    script, key_count, arguments = client.calls[0]
    keys = arguments[:key_count]
    expirations = arguments[key_count:]
    assert key_count == 2
    assert expirations == (120, 130)
    assert all(str(key).startswith("test:replay:") for key in keys)
    assert all("secret-jti" not in str(key) and "subject:jti" not in str(key) for key in keys)
    assert "EXISTS" in script and "EXAT" in script


def test_redis_store_rejects_replay_and_invalid_entries() -> None:
    client = FakeRedisClient(result=0)
    store = RedisReplayStore(client)

    assert not store.reserve([ReplayEntry("service:jti", 120)], 100)
    with pytest.raises(ValueError):
        store.reserve([], 100)
    with pytest.raises(ValueError):
        store.reserve([ReplayEntry("same", 120), ReplayEntry("same", 130)], 100)
    with pytest.raises(ValueError):
        store.reserve([ReplayEntry("expired", 100)], 100)


def test_redis_store_closes_its_client() -> None:
    client = FakeRedisClient()
    RedisReplayStore(client).close()
    assert client.closed


def test_replay_factory_allows_memory_only_for_local_or_test() -> None:
    assert isinstance(create_replay_store(Settings(environment="local")), InMemoryReplayStore)
    assert isinstance(create_replay_store(Settings(environment="test")), InMemoryReplayStore)

    with pytest.raises(RuntimeError, match="Distributed replay protection"):
        create_replay_store(Settings(environment="production"))


def test_production_replay_store_requires_tls_redis_url() -> None:
    with pytest.raises(RuntimeError, match="Redis URL"):
        create_replay_store(
            Settings(environment="production", replay_redis_url="redis://redis.internal:6379/0")
        )
