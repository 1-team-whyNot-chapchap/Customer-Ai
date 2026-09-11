from dataclasses import replace
from uuid import uuid4

import httpx
import pytest
from pydantic import SecretStr

from chapchap_customer_ai.contracts.models import UserRole
from chapchap_customer_ai.current_state.delivery_http import (
    DomainCurrentStateTransport,
    HttpDeliveryCurrentStateTransport,
)
from chapchap_customer_ai.current_state.models import TransportOutcome
from chapchap_customer_ai.security.models import AuthenticatedContext, AuthenticatedSubject

DATA = {"status": "DELIVERING", "delayStatus": "UNKNOWN", "statusChangedAt": None}


def context():
    return AuthenticatedContext(
        "customer-service",
        AuthenticatedSubject(
            42, UserRole.CUSTOMER, frozenset({"delivery.status.read"}), uuid4(), 501
        ),
    )


def invoke(client, *, ctx=None, arguments=None, timeout_seconds=1):
    return HttpDeliveryCurrentStateTransport(
        client, "https://delivery.internal", SecretStr("delivery-test-key")
    ).invoke(
        "get_current_delivery_state",
        {} if arguments is None else arguments,
        ctx or context(),
        required_scope="delivery.status.read",
        timeout_seconds=timeout_seconds,
    )


def test_exact_path_and_only_explicit_credentials():
    seen = []

    def handler(req):
        seen.append(req)
        return httpx.Response(200, json={"code": "00", "message": "SUCCESS", "data": DATA})

    with httpx.Client(
        transport=httpx.MockTransport(handler),
        cookies={"user": "999"},
        auth=("private", "private"),
        params={"userId": 999},
        headers={"X-Internal-Secret": "private"},
    ) as client:
        result = invoke(client)
    assert result.outcome == TransportOutcome.SUCCESS
    assert result.payload == {"availability": "AVAILABLE", **DATA}
    assert len(seen) == 1
    assert str(seen[0].url) == "https://delivery.internal/internal/deliveries/current"
    assert dict(seen[0].headers) == {
        "host": "delivery.internal",
        "accept": "application/json",
        "x-internal-service": "customer-ai",
        "x-internal-api-key": "delivery-test-key",
        "x-internal-scope": "delivery.status.read",
        "x-user-id": "42",
        "x-user-role": "CUSTOMER",
    }


@pytest.mark.parametrize(
    "status,data,code,outcome",
    [
        (200, DATA, "00", TransportOutcome.SUCCESS),
        (200, {**DATA, "status": "DELIVERED"}, "00", TransportOutcome.CONTRACT_ERROR),
        (200, {**DATA, "address": "private"}, "00", TransportOutcome.CONTRACT_ERROR),
        (
            200,
            {**DATA, "statusChangedAt": "2026-09-07T10:00:00"},
            "00",
            TransportOutcome.CONTRACT_ERROR,
        ),
        (200, None, "00", TransportOutcome.CONTRACT_ERROR),
        (404, None, "ROUTE_404", TransportOutcome.CONTRACT_ERROR),
        (404, None, "DELIVERY_036", TransportOutcome.BUSINESS_NOT_FOUND),
        (404, DATA, "DELIVERY_036", TransportOutcome.CONTRACT_ERROR),
        (400, None, "DELIVERY_038", TransportOutcome.CONTRACT_ERROR),
        (409, None, "DELIVERY_037", TransportOutcome.CONTRACT_ERROR),
        (401, None, "", TransportOutcome.FORBIDDEN),
        (403, None, "", TransportOutcome.FORBIDDEN),
        (503, None, "", TransportOutcome.UNAVAILABLE),
        (302, None, "", TransportOutcome.CONTRACT_ERROR),
    ],
)
def test_failure_classification(status, data, code, outcome):
    calls = []

    def handler(req):
        calls.append(req)
        return httpx.Response(status, json={"code": code, "message": "test", "data": data})

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        result = invoke(client)
    assert result.outcome == outcome
    assert not result.retryable and len(calls) == 1


@pytest.mark.parametrize(
    "changes",
    [
        {"user_id": True},
        {"user_id": "42"},
        {"user_id": 0},
        {"user_id": -1},
        {"user_id": 2**63},
        {"role": UserRole.RIDER},
        {"allowed_ai_scopes": frozenset({"delivery.current.read"})},
    ],
)
def test_invalid_subject_never_sends(changes):
    calls = []
    ctx = context()
    with httpx.Client(transport=httpx.MockTransport(lambda req: calls.append(req))) as client:
        result = invoke(client, ctx=replace(ctx, subject=replace(ctx.subject, **changes)))
    assert result.outcome == TransportOutcome.FORBIDDEN
    assert not calls


def test_tool_identity_and_caller_are_not_user_controlled():
    calls = []
    with httpx.Client(transport=httpx.MockTransport(lambda req: calls.append(req))) as client:
        assert invoke(client, arguments={"userId": 999}).outcome == TransportOutcome.CONTRACT_ERROR
        assert invoke(client, arguments=[]).outcome == TransportOutcome.CONTRACT_ERROR
        assert (
            invoke(client, ctx=replace(context(), service_subject="other")).outcome
            == TransportOutcome.FORBIDDEN
        )
    assert not calls


@pytest.mark.parametrize(
    "error,outcome",
    [
        (httpx.ReadTimeout("private"), TransportOutcome.TIMEOUT),
        (httpx.ConnectError("private"), TransportOutcome.UNAVAILABLE),
        (ValueError("private"), TransportOutcome.CONTRACT_ERROR),
    ],
)
def test_network_failure_is_not_retried(error, outcome):
    calls = []

    def handler(req):
        calls.append(req)
        raise error

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        result = invoke(client)
    assert result.outcome == outcome
    assert not result.retryable and len(calls) == 1


@pytest.mark.parametrize("key", ["", " ", "key\\r\\nInjected: value", "한글"])
def test_invalid_key_is_rejected_without_disclosure(key):
    with httpx.Client() as client, pytest.raises(ValueError) as error:
        HttpDeliveryCurrentStateTransport(client, "https://delivery.internal", SecretStr(key))
    assert "Injected" not in str(error.value)


@pytest.mark.parametrize("budget", [0.25, 8])
def test_timeout_uses_smaller_remaining_budget_and_two_second_cap(budget):
    def handler(req):
        assert all(0 < value <= min(budget, 2) for value in req.extensions["timeout"].values())
        return httpx.Response(200, json={"code": "00", "message": "SUCCESS", "data": DATA})

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        assert invoke(client, timeout_seconds=budget).outcome == TransportOutcome.SUCCESS


@pytest.mark.parametrize("budget", [0, -1, float("inf"), float("nan")])
def test_invalid_budget_never_sends(budget):
    calls = []
    with httpx.Client(transport=httpx.MockTransport(lambda req: calls.append(req))) as client:
        assert invoke(client, timeout_seconds=budget).outcome == TransportOutcome.TIMEOUT
    assert not calls


def test_expired_response_is_closed(monkeypatch):
    ticks = iter([0, 0, 3])
    monkeypatch.setattr(
        "chapchap_customer_ai.current_state.delivery_http.time.monotonic", lambda: next(ticks)
    )
    response = httpx.Response(200, json={"code": "00", "message": "SUCCESS", "data": DATA})
    with httpx.Client(transport=httpx.MockTransport(lambda req: response)) as client:
        assert invoke(client).outcome == TransportOutcome.TIMEOUT
    assert response.is_closed


@pytest.mark.parametrize(
    "url,allow,accepted",
    [
        ("https://delivery.internal", False, True),
        ("http://localhost:8083", True, True),
        ("http://localhost:8083", False, False),
        ("http://delivery.internal", True, False),
        ("https://delivery.internal/path", False, False),
        ("https://key@delivery.internal", False, False),
        ("https://delivery.internal?userId=1", False, False),
    ],
)
def test_origin_validation(url, allow, accepted):
    with httpx.Client() as client:
        if accepted:
            transport = HttpDeliveryCurrentStateTransport(client, url, SecretStr("test-key"), allow)
            assert "test-key" not in repr(transport)
        else:
            with pytest.raises(ValueError):
                HttpDeliveryCurrentStateTransport(client, url, SecretStr("test-key"), allow)


def test_missing_delivery_transport_is_unavailable():
    result = DomainCurrentStateTransport().invoke(
        "get_current_delivery_state",
        {},
        context(),
        required_scope="delivery.status.read",
        timeout_seconds=1,
    )
    assert result.outcome == TransportOutcome.UNAVAILABLE
