from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Protocol

from jwt import PyJWKClient

from chapchap_customer_ai.security.models import (
    AuthFailureCode,
    InternalAuthError,
)


class VerificationKeyResolver(Protocol):
    def resolve(self, issuer: str, key_id: str) -> Any: ...


@dataclass(frozen=True, slots=True)
class StaticVerificationKeyResolver:
    """테스트와 격리 환경용 resolver. 운영에서는 JWKS 기반 Port 구현으로 교체한다."""

    keys: Mapping[tuple[str, str], Any]

    def resolve(self, issuer: str, key_id: str) -> Any:
        try:
            return self.keys[(issuer, key_id)]
        except KeyError:
            raise InternalAuthError(
                AuthFailureCode.KEY_UNAVAILABLE,
                401,
                "A trusted verification key is unavailable.",
            ) from None


@dataclass(frozen=True, slots=True)
class JwksVerificationKeyResolver:
    clients: Mapping[str, PyJWKClient]

    @classmethod
    def from_urls(
        cls,
        urls_by_issuer: Mapping[str, str],
        *,
        timeout_seconds: float = 5.0,
        cache_lifespan_seconds: int = 300,
    ) -> "JwksVerificationKeyResolver":
        if not urls_by_issuer:
            raise ValueError("at least one issuer JWKS URL is required")
        return cls(
            {
                issuer: PyJWKClient(
                    url,
                    cache_keys=False,
                    cache_jwk_set=True,
                    lifespan=cache_lifespan_seconds,
                    timeout=timeout_seconds,
                )
                for issuer, url in urls_by_issuer.items()
            }
        )

    def resolve(self, issuer: str, key_id: str) -> Any:
        client = self.clients.get(issuer)
        if client is None:
            raise InternalAuthError(
                AuthFailureCode.KEY_UNAVAILABLE,
                401,
                "A trusted verification key is unavailable.",
            )
        try:
            return client.get_signing_key(key_id).key
        except Exception:
            raise InternalAuthError(
                AuthFailureCode.KEY_UNAVAILABLE,
                401,
                "A trusted verification key is unavailable.",
            ) from None
