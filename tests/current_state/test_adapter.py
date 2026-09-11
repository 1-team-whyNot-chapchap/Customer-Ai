from collections.abc import Mapping
from dataclasses import dataclass, field
from threading import Barrier
from uuid import uuid4

import pytest

from chapchap_customer_ai.consultation.models import (
    Capability,
    StateAvailability,
    StateErrorCode,
)
from chapchap_customer_ai.contracts.models import UserRole
from chapchap_customer_ai.current_state.adapter import CurrentStateAdapter
from chapchap_customer_ai.current_state.models import (
    CurrentStateRequestError,
    TransportOutcome,
    TransportResult,
)
from chapchap_customer_ai.security.models import AuthenticatedContext, AuthenticatedSubject

PAYMENT_PAYLOAD = {
    "availability": "AVAILABLE",
    "status": "SUCCESS",
    "paymentType": "REGULAR_PAYMENT",
    "amount": 12900,
    "occurredAt": "2026-08-31T09:00:00+09:00",
}
DELIVERY_PAYLOAD = {
    "availability": "AVAILABLE",
    "status": "DELIVERING",
    "delayStatus": "UNKNOWN",
}


def context(
    scopes: tuple[str, ...],
    *,
    service_subject: str = "customer-service",
    role: UserRole = UserRole.CUSTOMER,
) -> AuthenticatedContext:
    return AuthenticatedContext(
        service_subject,
        AuthenticatedSubject(42, role, frozenset(scopes), uuid4(), 501),
    )


@dataclass
class RecordingTransport:
    results: list[TransportResult | Exception]
    calls: list[tuple[str, Mapping[str, object], AuthenticatedContext, str, float]] = field(
        default_factory=list
    )

    def invoke(
        self,
        tool_name,
        arguments,
        security_context,
        *,
        required_scope,
        timeout_seconds,
    ):
        self.calls.append(
            (tool_name, arguments, security_context, required_scope, timeout_seconds)
        )
        result = self.results.pop(0)
        if isinstance(result, Exception):
            raise result
        return result


def test_approved_capability_uses_empty_arguments_and_signed_context() -> None:
    security_context = context(("subscription.payment.read",))
    transport = RecordingTransport([TransportResult(TransportOutcome.SUCCESS, PAYMENT_PAYLOAD)])

    fact = CurrentStateAdapter(transport).fetch(
        (Capability.PAYMENT_CURRENT,), security_context, timeout_seconds=3.0
    )[0]

    tool, arguments, passed_context, scope, timeout = transport.calls[0]
    assert tool == "get_current_payment_state"
    assert dict(arguments) == {}
    assert "userId" not in arguments
    assert passed_context is security_context
    assert scope == "subscription.payment.read"
    assert 0 < timeout <= 3.0
    assert fact.availability == StateAvailability.AVAILABLE


@pytest.mark.parametrize(
    "security_context",
    [
        context(()),
        context(("subscription.payment.read",), service_subject="another-service"),
        context(("subscription.payment.read",), role=UserRole.ADMIN),
    ],
)
def test_missing_scope_wrong_service_and_admin_are_forbidden_before_transport(
    security_context: AuthenticatedContext,
) -> None:
    transport = RecordingTransport([])

    facts = CurrentStateAdapter(transport).fetch(
        (Capability.PAYMENT_CURRENT,), security_context, timeout_seconds=3.0
    )

    assert facts[0].availability == StateAvailability.FORBIDDEN
    assert transport.calls == []


@pytest.mark.parametrize(
    "capabilities",
    [
        (),
        (Capability.PAYMENT_CURRENT, Capability.PAYMENT_CURRENT),
        (
            Capability.PAYMENT_CURRENT,
            Capability.REFUND_RECENT,
            Capability.SUBSCRIPTION_CURRENT,
        ),
        ("CAP-UNREGISTERED",),
    ],
)
def test_invalid_or_unregistered_capability_sets_are_rejected(capabilities) -> None:
    transport = RecordingTransport([])

    with pytest.raises(CurrentStateRequestError):
        CurrentStateAdapter(transport).fetch(
            capabilities,
            context(("subscription.payment.read",)),
            timeout_seconds=3.0,
        )

    assert transport.calls == []


@pytest.mark.parametrize(
    ("result", "availability", "error_code"),
    [
        (
            TransportResult(TransportOutcome.BUSINESS_NOT_FOUND),
            StateAvailability.NOT_FOUND,
            None,
        ),
        (TransportResult(TransportOutcome.FORBIDDEN), StateAvailability.FORBIDDEN, None),
        (TransportResult(TransportOutcome.UNAVAILABLE), StateAvailability.UNAVAILABLE, None),
        (TransportResult(TransportOutcome.TIMEOUT), StateAvailability.TIMEOUT, None),
        (TransportResult(TransportOutcome.CONTRACT_ERROR), None, StateErrorCode.CONTRACT_ERROR),
    ],
)
def test_transport_outcomes_preserve_runtime_meaning(result, availability, error_code) -> None:
    transport = RecordingTransport([result])

    fact = CurrentStateAdapter(transport).fetch(
        (Capability.PAYMENT_CURRENT,),
        context(("subscription.payment.read",)),
        timeout_seconds=3.0,
    )[0]

    assert fact.availability == availability
    assert fact.error_code == error_code
    assert fact.safe_answer is None


@pytest.mark.parametrize(
    "arguments",
    [
        ("SUCCESS", PAYMENT_PAYLOAD, False),
        (TransportOutcome.SUCCESS, ["raw"], False),
        (TransportOutcome.SUCCESS, PAYMENT_PAYLOAD, 1),
        (TransportOutcome.TIMEOUT, {"status": "FAILED"}, False),
        (TransportOutcome.TIMEOUT, None, True),
    ],
)
def test_transport_result_rejects_ambiguous_or_leaking_shapes(arguments) -> None:
    with pytest.raises(ValueError):
        TransportResult(*arguments)


def test_only_explicit_business_not_found_becomes_not_found() -> None:
    transport = RecordingTransport(
        [TransportResult(TransportOutcome.SUCCESS, {**PAYMENT_PAYLOAD, "status": "UNKNOWN"})]
    )

    fact = CurrentStateAdapter(transport).fetch(
        (Capability.PAYMENT_CURRENT,),
        context(("subscription.payment.read",)),
        timeout_seconds=3.0,
    )[0]

    assert fact.availability is None
    assert fact.error_code == StateErrorCode.CONTRACT_ERROR


def test_malformed_transport_return_is_contract_error() -> None:
    transport = RecordingTransport(["raw response"])

    fact = CurrentStateAdapter(transport).fetch(
        (Capability.PAYMENT_CURRENT,),
        context(("subscription.payment.read",)),
        timeout_seconds=3.0,
    )[0]

    assert fact.availability is None
    assert fact.error_code == StateErrorCode.CONTRACT_ERROR


def test_subscription_never_retries_unavailable_or_connection_reset() -> None:
    retryable = RecordingTransport(
        [
            TransportResult(TransportOutcome.UNAVAILABLE, retryable=True),
            TransportResult(TransportOutcome.SUCCESS, PAYMENT_PAYLOAD),
        ]
    )
    reset = RecordingTransport(
        [ConnectionError("private endpoint"), TransportResult(TransportOutcome.UNAVAILABLE)]
    )

    recovered = CurrentStateAdapter(retryable).fetch(
        (Capability.PAYMENT_CURRENT,),
        context(("subscription.payment.read",)),
        timeout_seconds=3.0,
    )[0]
    unavailable = CurrentStateAdapter(reset).fetch(
        (Capability.PAYMENT_CURRENT,),
        context(("subscription.payment.read",)),
        timeout_seconds=3.0,
    )[0]

    assert recovered.availability == StateAvailability.UNAVAILABLE
    assert unavailable.availability == StateAvailability.UNAVAILABLE
    assert len(retryable.calls) == len(reset.calls) == 1


def test_delivery_keeps_existing_single_retry_policy() -> None:
    transport = RecordingTransport([
        TransportResult(TransportOutcome.UNAVAILABLE, retryable=True),
        TransportResult(TransportOutcome.SUCCESS, DELIVERY_PAYLOAD),
    ])
    fact = CurrentStateAdapter(transport).fetch(
        (Capability.DELIVERY_CURRENT,), context(("delivery.status.read",)), timeout_seconds=3,
    )[0]
    assert fact.availability == StateAvailability.AVAILABLE
    assert len(transport.calls) == 2


@pytest.mark.parametrize(
    ("error", "availability", "error_code"),
    [
        (TimeoutError("private"), StateAvailability.TIMEOUT, None),
        (PermissionError("private"), StateAvailability.FORBIDDEN, None),
        (RuntimeError("raw tool body"), None, StateErrorCode.CONTRACT_ERROR),
    ],
)
def test_transport_exceptions_are_reduced_without_raw_details(
    error: Exception,
    availability: StateAvailability | None,
    error_code: StateErrorCode | None,
) -> None:
    transport = RecordingTransport([error])

    fact = CurrentStateAdapter(transport).fetch(
        (Capability.PAYMENT_CURRENT,),
        context(("subscription.payment.read",)),
        timeout_seconds=3.0,
    )[0]

    assert fact.availability == availability
    assert fact.error_code == error_code
    assert "private" not in str(fact)
    assert "raw tool body" not in str(fact)
    assert len(transport.calls) == 1


class ParallelTransport:
    def __init__(self) -> None:
        self.barrier = Barrier(2)
        self.calls: list[str] = []

    def invoke(
        self,
        tool_name,
        arguments,
        security_context,
        *,
        required_scope,
        timeout_seconds,
    ):
        self.calls.append(tool_name)
        self.barrier.wait(timeout=1.0)
        payload = PAYMENT_PAYLOAD if "payment" in tool_name else DELIVERY_PAYLOAD
        return TransportResult(TransportOutcome.SUCCESS, payload)


def test_two_independent_capabilities_run_in_parallel_and_preserve_order() -> None:
    transport = ParallelTransport()

    facts = CurrentStateAdapter(transport).fetch(
        (Capability.PAYMENT_CURRENT, Capability.DELIVERY_CURRENT),
        context(("subscription.payment.read", "delivery.status.read")),
        timeout_seconds=3.0,
    )

    assert tuple(fact.capability for fact in facts) == (
        Capability.PAYMENT_CURRENT,
        Capability.DELIVERY_CURRENT,
    )
    assert all(fact.availability == StateAvailability.AVAILABLE for fact in facts)
