from dataclasses import dataclass
from typing import Any

import pytest

from chapchap_customer_ai.core.settings import Settings
from chapchap_customer_ai.security.jwt_verifier import create_internal_security_verifier
from chapchap_customer_ai.security.keys import (
    JwksVerificationKeyResolver,
    StaticVerificationKeyResolver,
)
from chapchap_customer_ai.security.models import AuthFailureCode, InternalAuthError
from chapchap_customer_ai.security.replay import InMemoryReplayStore


@dataclass
class SigningKey:
    key: str


class FakeJwkClient:
    def __init__(self, *, error: Exception | None = None) -> None:
        self.error = error
        self.requested_key_id: str | None = None

    def get_signing_key(self, key_id: str) -> SigningKey:
        self.requested_key_id = key_id
        if self.error is not None:
            raise self.error
        return SigningKey("public-key")


def test_jwks_resolver_selects_issuer_and_key_id() -> None:
    client = FakeJwkClient()
    resolver = JwksVerificationKeyResolver({"issuer": client})  # type: ignore[arg-type]

    assert resolver.resolve("issuer", "key-1") == "public-key"
    assert client.requested_key_id == "key-1"


def test_jwks_resolver_hides_provider_errors() -> None:
    resolver = JwksVerificationKeyResolver(  # type: ignore[arg-type]
        {"issuer": FakeJwkClient(error=RuntimeError("sensitive provider detail"))}
    )

    with pytest.raises(InternalAuthError) as error:
        resolver.resolve("issuer", "key-1")

    assert error.value.code == AuthFailureCode.KEY_UNAVAILABLE
    assert "sensitive provider detail" not in str(error.value)


@pytest.mark.parametrize(
    ("service_url", "subject_url"),
    [
        (None, None),
        ("http://auth.internal/jwks", "https://customer.internal/jwks"),
        ("https://user:password@auth.internal/jwks", "https://customer.internal/jwks"),
        ("https://auth.internal/jwks#fragment", "https://customer.internal/jwks"),
    ],
)
def test_runtime_factory_rejects_missing_or_untrusted_jwks_urls(
    service_url: str | None,
    subject_url: str | None,
) -> None:
    settings = Settings(
        service_jwks_url=service_url,
        subject_assertion_jwks_url=subject_url,
    )

    with pytest.raises(InternalAuthError) as error:
        create_internal_security_verifier(settings, InMemoryReplayStore())

    assert error.value.code == AuthFailureCode.KEY_UNAVAILABLE


def test_runtime_factory_builds_only_with_both_https_jwks_urls(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    resolver = StaticVerificationKeyResolver({})
    captured: dict[str, Any] = {}

    def fake_from_urls(
        cls: type[JwksVerificationKeyResolver],
        urls_by_issuer: dict[str, str],
        *,
        timeout_seconds: float,
        cache_lifespan_seconds: int,
    ) -> StaticVerificationKeyResolver:
        captured.update(
            urls=urls_by_issuer,
            timeout=timeout_seconds,
            lifespan=cache_lifespan_seconds,
        )
        return resolver

    monkeypatch.setattr(JwksVerificationKeyResolver, "from_urls", classmethod(fake_from_urls))
    settings = Settings(
        service_jwks_url="https://auth.internal/jwks",
        subject_assertion_jwks_url="https://customer.internal/jwks",
        jwks_timeout_seconds=3.0,
        jwks_cache_lifespan_seconds=600,
    )

    verifier = create_internal_security_verifier(settings, InMemoryReplayStore())

    assert verifier.key_resolver is resolver
    assert captured == {
        "urls": {
            "chapchap-auth-service": "https://auth.internal/jwks",
            "chapchap-customer-service": "https://customer.internal/jwks",
        },
        "timeout": 3.0,
        "lifespan": 600,
    }


@pytest.mark.parametrize(
    "override",
    [
        {"service_jwt_issuer": "other-auth"},
        {"subject_assertion_issuer": "other-service"},
        {"service_jwt_audience": "other-audience"},
    ],
)
def test_runtime_factory_rejects_unapproved_trust_contract(override: dict[str, str]) -> None:
    settings = Settings(
        service_jwks_url="https://auth.internal/jwks",
        subject_assertion_jwks_url="https://customer.internal/jwks",
        **override,
    )

    with pytest.raises(InternalAuthError) as error:
        create_internal_security_verifier(settings, InMemoryReplayStore())

    assert error.value.code == AuthFailureCode.INVALID_TOKEN


def test_runtime_factory_rejects_in_memory_replay_store_outside_local_or_test() -> None:
    settings = Settings(
        environment="production",
        service_jwks_url="https://auth.internal/jwks",
        subject_assertion_jwks_url="https://customer.internal/jwks",
    )

    with pytest.raises(InternalAuthError, match="Distributed replay protection"):
        create_internal_security_verifier(settings, InMemoryReplayStore())
