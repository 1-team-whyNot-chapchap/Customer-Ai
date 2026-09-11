from urllib.parse import parse_qs

import httpx
import pytest
from pydantic import SecretStr

from chapchap_customer_ai.security.service_tokens import (
    AuthServiceCallbackTokenProvider,
    ServiceTokenUnavailable,
)


def token_body(**changes):
    return {
        "access_token": "test-token",
        "token_type": "Bearer",
        "expires_in": 300,
        "scope": "customer-ai.callback",
        **changes,
    }


def test_auth_contract_cache_and_refresh_without_default_identity():
    calls = []
    clock = [0.0]

    def handler(req):
        calls.append(req)
        return httpx.Response(200, json=token_body(access_token=f"token-{len(calls)}"))

    with httpx.Client(
        transport=httpx.MockTransport(handler),
        auth=("private", "private"),
        cookies={"private": "value"},
        params={"userId": 999},
    ) as client:
        provider = AuthServiceCallbackTokenProvider(
            client,
            "https://auth.internal",
            "ai-test",
            SecretStr("test-secret"),
            monotonic=lambda: clock[0],
        )
        assert provider.get_token() == "token-1"
        clock[0] = 289
        assert provider.get_token() == "token-1"
        clock[0] = 290
        assert provider.get_token() == "token-2"
    assert len(calls) == 2
    assert str(calls[0].url) == "https://auth.internal/internal/v1/service-tokens"
    assert "authorization" not in calls[0].headers and "cookie" not in calls[0].headers
    assert parse_qs(calls[0].content.decode()) == {
        "grant_type": ["client_credentials"],
        "client_id": ["ai-test"],
        "client_secret": ["test-secret"],
        "audience": ["chapchap-customer-service"],
        "scope": ["customer-ai.callback"],
    }


@pytest.mark.parametrize(
    "changes",
    [
        {"expires_in": True},
        {"expires_in": 0},
        {"expires_in": 301},
        {"expires_in": "300"},
        {"scope": "admin"},
        {"token_type": "Basic"},
        {"access_token": "token\nprivate"},
        {"access_token": ""},
        {"raw": "private"},
    ],
)
def test_rejects_invalid_auth_response(changes):
    with httpx.Client(
        transport=httpx.MockTransport(lambda req: httpx.Response(200, json=token_body(**changes)))
    ) as client:
        provider = AuthServiceCallbackTokenProvider(
            client, "https://auth.internal", "test", SecretStr("private")
        )
        with pytest.raises(ServiceTokenUnavailable) as error:
            provider.get_token()
    assert "private" not in str(error.value)


def test_refresh_failure_never_reuses_expired_token():
    clock = [0]
    calls = []

    def handler(req):
        calls.append(req)
        return httpx.Response(200, json=token_body()) if len(calls) == 1 else httpx.Response(503)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        provider = AuthServiceCallbackTokenProvider(
            client,
            "https://auth.internal",
            "test",
            SecretStr("private"),
            monotonic=lambda: clock[0],
        )
        assert provider.get_token() == "test-token"
        clock[0] = 300
        with pytest.raises(ServiceTokenUnavailable):
            provider.get_token()
