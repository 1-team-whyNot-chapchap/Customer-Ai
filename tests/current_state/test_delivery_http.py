from dataclasses import replace
from uuid import uuid4

import httpx
import pytest

from chapchap_customer_ai.contracts.models import UserRole
from chapchap_customer_ai.current_state.delivery_http import (
    DeliveryWireContract,
    DomainCurrentStateTransport,
    HttpDeliveryCurrentStateTransport,
)
from chapchap_customer_ai.current_state.models import TransportOutcome
from chapchap_customer_ai.security.models import AuthenticatedContext, AuthenticatedSubject

CONTRACT = DeliveryWireContract("X-Test-Service", "X-Test-Subject", "delivery.status.read")
DATA = {"status": "DELIVERING", "delayStatus": "UNKNOWN", "statusChangedAt": None}


class Credentials:
    def headers(self, context, *, scope, timeout_seconds):
        assert context.subject.user_id == 42
        return {"X-Test-Service": "test-service", "X-Test-Subject": "test-signed-subject"}


def context():
    return AuthenticatedContext(
        "customer-service",
        AuthenticatedSubject(
            42, UserRole.CUSTOMER, frozenset({"delivery.status.read"}), uuid4(), 501
        ),
    )


def invoke(client, *, contract=CONTRACT, ctx=None, credentials=None, arguments=None):
    return HttpDeliveryCurrentStateTransport(
        client, "https://delivery.internal", contract, credentials or Credentials()
    ).invoke(
        "get_current_delivery_state",
        arguments or {},
        ctx or context(),
        required_scope="delivery.status.read",
        timeout_seconds=1,
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
        "x-test-service": "test-service",
        "x-test-subject": "test-signed-subject",
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
        (404, None, "TEST_NO_CURRENT", TransportOutcome.BUSINESS_NOT_FOUND),
        (404, DATA, "TEST_NO_CURRENT", TransportOutcome.CONTRACT_ERROR),
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
        result = invoke(client, contract=replace(CONTRACT, not_found_code="TEST_NO_CURRENT"))
    assert result.outcome == outcome
    assert not result.retryable and len(calls) == 1


def test_unconfirmed_not_found_and_scope_are_not_inferred():
    with httpx.Client(
        transport=httpx.MockTransport(
            lambda req: httpx.Response(
                404, json={"code": "TEST_NO_CURRENT", "message": "test", "data": None}
            )
        )
    ) as client:
        assert invoke(client).outcome == TransportOutcome.CONTRACT_ERROR
    calls = []
    with httpx.Client(transport=httpx.MockTransport(lambda req: calls.append(req))) as client:
        assert (
            invoke(
                client, contract=replace(CONTRACT, provider_scope="delivery.current.read")
            ).outcome
            == TransportOutcome.FORBIDDEN
        )
        ctx = context()
        assert (
            invoke(client, ctx=replace(ctx, subject=replace(ctx.subject, user_id=True))).outcome
            == TransportOutcome.FORBIDDEN
        )
        assert invoke(client, arguments={"userId": 999}).outcome == TransportOutcome.CONTRACT_ERROR
    assert not calls


@pytest.mark.parametrize(
    "error,outcome",
    [
        (httpx.ReadTimeout("private"), TransportOutcome.TIMEOUT),
        (httpx.ConnectError("private"), TransportOutcome.UNAVAILABLE),
        (PermissionError("private"), TransportOutcome.FORBIDDEN),
        (ValueError("private"), TransportOutcome.CONTRACT_ERROR),
    ],
)
def test_credentials_failure_never_sends_request(error, outcome):
    class BrokenCredentials:
        def headers(self, *args, **kwargs):
            raise error

    calls = []
    with httpx.Client(transport=httpx.MockTransport(lambda req: calls.append(req))) as client:
        assert invoke(client, credentials=BrokenCredentials()).outcome == outcome
    assert not calls


def test_missing_delivery_transport_is_unavailable():
    result = DomainCurrentStateTransport().invoke(
        "get_current_delivery_state",
        {},
        context(),
        required_scope="delivery.status.read",
        timeout_seconds=1,
    )
    assert result.outcome == TransportOutcome.UNAVAILABLE
