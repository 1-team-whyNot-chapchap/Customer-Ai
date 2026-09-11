import time
from collections.abc import Callable
from threading import Lock

import httpx
from pydantic import SecretStr

from chapchap_customer_ai.application.http_json import send_json
from chapchap_customer_ai.current_state.http import validate_subscription_origin


class ServiceTokenUnavailable(RuntimeError):
    pass


class AuthServiceCallbackTokenProvider:
    """Auth dev client_credentials contract, restricted to Customer callbacks."""

    def __init__(
        self,
        client: httpx.Client,
        base_url: str,
        client_id: str,
        client_secret: SecretStr,
        *,
        timeout_seconds: float = 3,
        http_allowed_origins: tuple[str, ...] = (),
        monotonic: Callable[[], float] = time.monotonic,
    ):
        self._origin = validate_subscription_origin(
            base_url, http_allowed_origins=http_allowed_origins
        )
        if not client_id or not client_id.strip() or not client_secret.get_secret_value().strip():
            raise ValueError("Callback client credentials are required")
        if not 0 < timeout_seconds <= 10:
            raise ValueError("Invalid token timeout")
        self._client = client
        self._client_id = client_id
        self._secret = client_secret
        self._timeout = timeout_seconds
        self._clock = monotonic
        self._lock = Lock()
        self._token: str | None = None
        self._expires_at = 0.0

    def get_token(self) -> str:
        with self._lock:
            now = self._clock()
            if self._token is not None and now < self._expires_at:
                return self._token
            self._token = None
            try:
                request = httpx.Request(
                    "POST",
                    f"{self._origin}/internal/v1/service-tokens",
                    headers={"Accept": "application/json"},
                    data={
                        "grant_type": "client_credentials",
                        "client_id": self._client_id,
                        "client_secret": self._secret.get_secret_value(),
                        "audience": "chapchap-customer-service",
                        "scope": "customer-ai.callback",
                    },
                    extensions={"timeout": httpx.Timeout(self._timeout).as_dict()},
                )
                body = send_json(self._client, request)
                if not isinstance(body, dict) or set(body) != {
                    "access_token",
                    "token_type",
                    "expires_in",
                    "scope",
                }:
                    raise ValueError
                token, ttl = body["access_token"], body["expires_in"]
                if (
                    not isinstance(token, str)
                    or not token
                    or len(token) > 16384
                    or any(ord(c) <= 32 or ord(c) > 126 for c in token)
                    or type(ttl) is not int
                    or not 1 <= ttl <= 300
                    or body["token_type"] != "Bearer"
                    or body["scope"] != "customer-ai.callback"
                ):
                    raise ValueError
                # Count network time against TTL; refresh early without extending expiry.
                expires_at = now + ttl - min(10, ttl * 0.1)
                if self._clock() >= expires_at:
                    raise ValueError
                self._expires_at = expires_at
                self._token = token
                return token
            except Exception:
                raise ServiceTokenUnavailable("Callback service token is unavailable") from None
