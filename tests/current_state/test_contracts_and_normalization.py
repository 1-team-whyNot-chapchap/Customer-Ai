from copy import deepcopy

import pytest
from pydantic import ValidationError

from chapchap_customer_ai.consultation.models import (
    Capability,
    StateAvailability,
    StateErrorCode,
)
from chapchap_customer_ai.current_state.contracts import (
    CurrentDeliveryState,
    CurrentPaymentState,
    CurrentSubscriptionState,
    RecentRefundResult,
)
from chapchap_customer_ai.current_state.normalization import ToolResultNormalizer
from chapchap_customer_ai.current_state.registry import CAPABILITY_REGISTRY

PAYMENT = {
    "availability": "AVAILABLE",
    "status": "RETRY_WAITING",
    "paymentType": "REGULAR_PAYMENT",
    "amount": 12900,
    "occurredAt": "2026-08-31T09:00:00+09:00",
}


def test_capability_registry_contains_only_confirmed_read_tools_and_is_immutable() -> None:
    assert {
        capability.value: (binding.tool_name, binding.required_scope)
        for capability, binding in CAPABILITY_REGISTRY.items()
    } == {
        "CAP-PAYMENT-CURRENT": (
            "get_current_payment_state",
            "subscription.payment.read",
        ),
        "CAP-REFUND-RECENT": (
            "get_recent_refund_result",
            "subscription.refund.read",
        ),
        "CAP-SUBSCRIPTION-CURRENT": (
            "get_current_subscription_state",
            "subscription.status.read",
        ),
        "CAP-DELIVERY-CURRENT": (
            "get_current_delivery_state",
            "delivery.status.read",
        ),
    }
    with pytest.raises(TypeError):
        CAPABILITY_REGISTRY[Capability.PAYMENT_CURRENT] = None
REFUND = {
    "availability": "AVAILABLE",
    "status": "REVIEW_REQUIRED",
    "refundType": "DELIVERY_PARTIAL_CANCELLATION",
    "requestedAmount": 20000,
    "refundedAmount": 12000,
    "unprocessedAmount": 8000,
    "requestedAt": "2026-08-31T13:55:00+09:00",
    "completedAt": None,
}
SUBSCRIPTION = {"availability": "AVAILABLE", "status": "CANCELLATION_SCHEDULED"}
DELIVERY = {
    "availability": "AVAILABLE",
    "status": "DELIVERING",
    "delayStatus": "NOT_DELAYED",
    "statusChangedAt": "2026-08-31T14:00:00+09:00",
}


@pytest.mark.parametrize(
    ("model", "payload", "statuses"),
    [
        (
            CurrentPaymentState,
            PAYMENT,
            ("PROCESSING", "SUCCESS", "RETRY_WAITING", "RETRY_STOPPED", "FAILED"),
        ),
        (
            RecentRefundResult,
            REFUND,
            ("PENDING", "FAILED", "REVIEW_REQUIRED"),
        ),
        (
            CurrentSubscriptionState,
            SUBSCRIPTION,
            (
                "AWAITING_CONFIRMATION",
                "SCHEDULED",
                "IN_PROGRESS",
                "CANCELLATION_SCHEDULED",
                "PAYMENT_FAILED",
                "CANCELED_BEFORE_START",
                "ENDED",
            ),
        ),
        (CurrentDeliveryState, DELIVERY, ("READY", "DELIVERING", "COMPLETED", "FAILED")),
    ],
)
def test_all_confirmed_domain_statuses_are_accepted(model, payload, statuses) -> None:
    for status in statuses:
        candidate = deepcopy(payload)
        candidate["status"] = status
        model.model_validate(candidate)


def test_completed_refund_requires_completion_time() -> None:
    completed = deepcopy(REFUND)
    completed.update(
        {
            "status": "COMPLETED",
            "refundedAmount": 20000,
            "unprocessedAmount": 0,
            "completedAt": "2026-08-31T14:10:00+09:00",
        }
    )

    assert RecentRefundResult.model_validate(completed).completed_at is not None
    completed["completedAt"] = None
    with pytest.raises(ValidationError):
        RecentRefundResult.model_validate(completed)


@pytest.mark.parametrize(
    ("model", "payload", "field", "value"),
    [
        (CurrentPaymentState, PAYMENT, "status", "COMPLETED"),
        (CurrentPaymentState, PAYMENT, "statusChangedAt", "2026-08-31T09:00:00+09:00"),
        (CurrentPaymentState, PAYMENT, "occurredAt", "2026-08-31T09:00:00"),
        (RecentRefundResult, REFUND, "failureReasonCode", "PRIVATE"),
        (CurrentSubscriptionState, SUBSCRIPTION, "userId", 42),
        (CurrentDeliveryState, DELIVERY, "status", "DELIVERED"),
        (CurrentDeliveryState, DELIVERY, "delayStatus", "NORMAL"),
    ],
)
def test_unknown_status_extra_sensitive_field_and_naive_time_are_rejected(
    model, payload, field, value
) -> None:
    candidate = deepcopy(payload)
    candidate[field] = value

    with pytest.raises(ValidationError):
        model.model_validate(candidate)


def test_normalizer_creates_minimal_fact_without_subject_or_raw_payload() -> None:
    fact = ToolResultNormalizer().normalize(Capability.PAYMENT_CURRENT, PAYMENT)

    assert fact.availability == StateAvailability.AVAILABLE
    assert dict(fact.values) == {
        "status": "RETRY_WAITING",
        "paymentType": "REGULAR_PAYMENT",
        "amount": 12900,
        "occurredAt": "2026-08-31T09:00:00+09:00",
    }
    assert "user" not in str(fact.values).lower()
    assert "12900" in fact.safe_answer


def test_delivery_unknown_delay_and_missing_time_are_preserved() -> None:
    payload = {key: value for key, value in DELIVERY.items() if key != "statusChangedAt"}
    payload["delayStatus"] = "UNKNOWN"

    fact = ToolResultNormalizer().normalize(Capability.DELIVERY_CURRENT, payload)

    assert dict(fact.values)["delayStatus"] == "UNKNOWN"
    assert dict(fact.values)["statusChangedAt"] is None
    assert "NOT_DELAYED" not in fact.safe_answer


@pytest.mark.parametrize(
    "payload",
    [
        {**PAYMENT, "status": "UNKNOWN"},
        {key: value for key, value in PAYMENT.items() if key != "amount"},
        {**PAYMENT, "databaseId": 991},
    ],
)
def test_schema_failures_become_contract_error_without_business_data(payload) -> None:
    fact = ToolResultNormalizer().normalize(Capability.PAYMENT_CURRENT, payload)

    assert fact.availability is None
    assert fact.error_code == StateErrorCode.CONTRACT_ERROR
    assert fact.safe_answer is None
    assert fact.values == ()
