import json
from dataclasses import replace
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from uuid import uuid4

import httpx
import pytest

from chapchap_customer_ai.consultation.models import Capability, StateAvailability
from chapchap_customer_ai.contracts.models import UserRole
from chapchap_customer_ai.core.settings import Settings
from chapchap_customer_ai.current_state.http import HttpSubscriptionCurrentStateTransport
from chapchap_customer_ai.current_state.models import TransportOutcome
from chapchap_customer_ai.current_state.registry import CAPABILITY_REGISTRY
from chapchap_customer_ai.current_state.runtime import create_subscription_current_state_runtime
from chapchap_customer_ai.security.models import AuthenticatedContext, AuthenticatedSubject

PAYMENT = {
    "status": "RETRY_WAITING", "paymentType": "REGULAR_PAYMENT", "amount": 12900,
    "occurredAt": "2026-08-31T09:00:00+09:00",
}
REFUND = {
    "status": "REVIEW_REQUIRED", "refundType": "DELIVERY_PARTIAL_CANCELLATION",
    "requestedAmount": 20000, "refundedAmount": 12000, "unprocessedAmount": 8000,
    "requestedAt": "2026-08-31T13:55:00+09:00", "completedAt": None,
}


def context(capability=Capability.PAYMENT_CURRENT):
    return AuthenticatedContext("customer-service", AuthenticatedSubject(
        42, UserRole.CUSTOMER, frozenset({CAPABILITY_REGISTRY[capability].required_scope}),
        uuid4(), 501,
    ))


def invoke(client, *, capability=Capability.PAYMENT_CURRENT, security_context=None, arguments=None):
    binding = CAPABILITY_REGISTRY[capability]
    return HttpSubscriptionCurrentStateTransport(client, "https://subscription.internal").invoke(
        binding.tool_name, {} if arguments is None else arguments,
        context(capability) if security_context is None else security_context,
        required_scope=binding.required_scope, timeout_seconds=1.0,
    )


@pytest.mark.parametrize(("capability", "path", "data"), [
    (Capability.PAYMENT_CURRENT, "payment", PAYMENT),
    (Capability.REFUND_RECENT, "refund", REFUND),
    (Capability.SUBSCRIPTION_CURRENT, "subscription", {"status": "ENDED"}),
])
def test_exact_contract_and_no_inherited_authentication(capability, path, data):
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(200, json={"code": "00", "message": "SUCCESS", "data": data})

    with httpx.Client(
        transport=httpx.MockTransport(handler), headers={"X-Internal-Secret": "private"},
        cookies={"session": "private"}, auth=("private", "private"),
        params={"userId": "999"}, follow_redirects=True,
    ) as client:
        result = invoke(client, capability=capability)

    assert result.outcome == TransportOutcome.SUCCESS
    assert result.payload == {"availability": "AVAILABLE", **data}
    assert len(requests) == 1
    request = requests[0]
    assert request.method == "GET"
    assert request.url.path == f"/api/subscription/internal/v1/current-state/{path}"
    assert not request.url.query and not request.content
    assert dict(request.headers) == {
        "host": "subscription.internal", "x-user-id": "42", "accept": "application/json",
    }
    assert request.extensions["timeout"]["read"] == 1.0


@pytest.mark.parametrize(("status", "body", "expected"), [
    (200, {"code": "00", "message": "SUCCESS", "data": None},
     TransportOutcome.BUSINESS_NOT_FOUND),
    (200, {"code": "00", "message": "SUCCESS"}, TransportOutcome.CONTRACT_ERROR),
    (200, {"code": "COMMON_099", "message": "error", "data": None},
     TransportOutcome.CONTRACT_ERROR),
    (200, {"code": 0, "message": "SUCCESS", "data": None}, TransportOutcome.CONTRACT_ERROR),
    (200, {"code": "00", "message": "SUCCESS", "data": []}, TransportOutcome.CONTRACT_ERROR),
    (200, {"code": "00", "message": "SUCCESS", "data": {**PAYMENT, "amount": True}},
     TransportOutcome.CONTRACT_ERROR),
    (200, {"code": "00", "message": "SUCCESS", "data": {**PAYMENT, "userId": 42}},
     TransportOutcome.CONTRACT_ERROR),
    (200, {"code": "00", "message": "SUCCESS", "data": {"availability": "NOT_FOUND"}},
     TransportOutcome.CONTRACT_ERROR),
    (401, {}, TransportOutcome.FORBIDDEN), (403, {}, TransportOutcome.FORBIDDEN),
    (400, {}, TransportOutcome.CONTRACT_ERROR), (404, {}, TransportOutcome.CONTRACT_ERROR),
    (302, {}, TransportOutcome.CONTRACT_ERROR), (500, {}, TransportOutcome.UNAVAILABLE),
    (503, {}, TransportOutcome.UNAVAILABLE),
])
def test_failure_is_not_business_not_found_and_never_retried(status, body, expected):
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(status, json=body, headers={"Location": "https://other.internal"})

    with httpx.Client(transport=httpx.MockTransport(handler), follow_redirects=True) as client:
        result = invoke(client)
    assert result.outcome == expected
    assert result.payload is None and not result.retryable
    assert len(requests) == 1


@pytest.mark.parametrize(("error", "expected"), [
    (httpx.ConnectError("private endpoint"), TransportOutcome.UNAVAILABLE),
    (httpx.ReadTimeout("private endpoint"), TransportOutcome.TIMEOUT),
])
def test_transport_failure_has_no_raw_details(error, expected):
    calls = []

    def handler(request):
        calls.append(request)
        raise error

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        result = invoke(client)
    assert result.outcome == expected and not result.retryable
    assert "private" not in repr(result)
    assert len(calls) == 1


@pytest.mark.parametrize("user_id", [0, -1, True, "42", 2**63])
def test_invalid_subject_never_reaches_http(user_id):
    original = context()
    forbidden = replace(original, subject=replace(original.subject, user_id=user_id))
    with httpx.Client(transport=httpx.MockTransport(lambda _: pytest.fail("HTTP was called"))) \
            as client:
        assert invoke(client, security_context=forbidden).outcome == TransportOutcome.FORBIDDEN


@pytest.mark.parametrize("security_context", [
    replace(context(), service_subject="unknown"),
    replace(context(), subject=replace(context().subject, role=UserRole.ADMIN)),
    replace(context(), subject=replace(context().subject, allowed_ai_scopes=frozenset())),
])
def test_untrusted_context_never_reaches_http(security_context):
    with httpx.Client(transport=httpx.MockTransport(lambda _: pytest.fail("HTTP was called"))) \
            as client:
        result = invoke(client, security_context=security_context)
        assert result.outcome == TransportOutcome.FORBIDDEN


def test_arguments_and_unconfirmed_delivery_are_not_forwarded():
    with httpx.Client(transport=httpx.MockTransport(lambda _: pytest.fail("HTTP was called"))) \
            as client:
        assert invoke(client, arguments={"userId": 999}).outcome == TransportOutcome.CONTRACT_ERROR
        assert invoke(client, capability=Capability.DELIVERY_CURRENT).outcome \
            == TransportOutcome.CONTRACT_ERROR


@pytest.mark.parametrize("body", [b"not-json", b"x" * (64 * 1024 + 1)],
                         ids=["invalid-json", "oversized"])
def test_invalid_or_oversized_response_is_rejected(body):
    with httpx.Client(transport=httpx.MockTransport(lambda _: httpx.Response(
        200, content=body, headers={"content-type": "application/json"}
    ))) as client:
        assert invoke(client).outcome == TransportOutcome.CONTRACT_ERROR


@pytest.mark.parametrize("origin", [
    "http://subscription.internal", "https://user:secret@subscription.internal",
    "https://subscription.internal/path", "https://subscription.internal?userId=42",
    "https://subscription.internal#fragment", "https://subscription.internal:invalid",
])
def test_runtime_rejects_untrusted_origin_without_echoing_it(origin):
    with pytest.raises(ValueError) as failure:
        create_subscription_current_state_runtime(Settings(
            _env_file=None, subscription_current_state_base_url=origin,
        ))
    assert origin not in str(failure.value)


def test_runtime_adapter_calls_subscription_once_on_server_failure_and_closes(caplog):
    caplog.set_level("INFO", logger="chapchap_customer_ai.current_state")
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(503)

    with create_subscription_current_state_runtime(Settings(
        _env_file=None, subscription_current_state_base_url="https://subscription.internal",
    ), transport=httpx.MockTransport(handler)) as runtime:
        fact = runtime.adapter.fetch((Capability.PAYMENT_CURRENT,), context(), timeout_seconds=1)[0]
        assert fact.availability == StateAvailability.UNAVAILABLE
        assert len(requests) == 1
    assert runtime.client.is_closed
    assert len(caplog.records) == 1
    recorded = json.loads(caplog.records[0].message)
    assert recorded["availability"] == "UNAVAILABLE"
    assert "requestId" in recorded and "userId" not in recorded


def test_real_loopback_http_round_trip():
    requests = []

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            requests.append((self.path, self.headers.get("X-User-Id")))
            body = json.dumps({"code": "00", "message": "SUCCESS", "data": PAYMENT}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        with create_subscription_current_state_runtime(Settings(
            _env_file=None,
            subscription_current_state_base_url=f"http://127.0.0.1:{server.server_port}",
            subscription_current_state_allow_loopback_http=True,
        )) as runtime:
            fact = runtime.adapter.fetch(
                (Capability.PAYMENT_CURRENT,), context(), timeout_seconds=2,
            )[0]
        assert fact.availability == StateAvailability.AVAILABLE
        assert requests == [("/api/subscription/internal/v1/current-state/payment", "42")]
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
