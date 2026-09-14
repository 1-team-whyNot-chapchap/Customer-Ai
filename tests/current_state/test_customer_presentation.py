from datetime import datetime

import pytest

from chapchap_customer_ai.consultation.models import Capability, StateErrorCode
from chapchap_customer_ai.current_state.contracts import (
    DelayStatus,
    DeliveryStatus,
    PaymentStatus,
    PaymentType,
    RefundStatus,
    SubscriptionStatus,
)
from chapchap_customer_ai.current_state.normalization import ToolResultNormalizer
from chapchap_customer_ai.current_state.presentation import customer_time
from tests.current_state.test_contracts_and_normalization import (
    DELIVERY,
    PAYMENT,
    REFUND,
    SUBSCRIPTION,
)


@pytest.mark.parametrize('capability,payload,field,codes', [
    (Capability.PAYMENT_CURRENT, PAYMENT, 'status', PaymentStatus),
    (Capability.PAYMENT_CURRENT, PAYMENT, 'paymentType', PaymentType),
    (Capability.REFUND_RECENT, REFUND, 'status', RefundStatus),
    (Capability.SUBSCRIPTION_CURRENT, SUBSCRIPTION, 'status', SubscriptionStatus),
    (Capability.DELIVERY_CURRENT, DELIVERY, 'status', DeliveryStatus),
    (Capability.DELIVERY_CURRENT, DELIVERY, 'delayStatus', DelayStatus),
    (Capability.REFUND_RECENT, REFUND, 'refundType', (
        'SETTING_CHANGE_REDUCTION', 'CANCELLATION_BEFORE_START',
        'NEXT_PERIOD_FULL_CANCELLATION', 'DELIVERY_PARTIAL_CANCELLATION',
        'FUTURE_INTERNAL_CODE',
    )),
])
def test_every_domain_code_is_hidden_in_customer_answer(capability, payload, field, codes):
    for code in codes:
        candidate = {**payload, field: code}
        if capability == Capability.REFUND_RECENT and code == 'COMPLETED':
            candidate.update(completedAt='2026-08-31T14:00:00+09:00',
                             refundedAmount=20000, unprocessedAmount=0)
        fact = ToolResultNormalizer().normalize(capability, candidate)
        assert fact.safe_answer
        assert str(code) not in fact.safe_answer
        assert not any(character.isascii() and character.isalpha()
                       for character in fact.safe_answer)
        # Presentation does not rewrite the internal contract.
        assert dict(fact.values)[field] == code


@pytest.mark.parametrize('value,expected', [
    ('2026-09-12T15:20:00Z', '2026년 9월 13일 오전 12시 20분'),
    ('2026-09-13T03:00:00Z', '2026년 9월 13일 오후 12시 00분'),
    ('2026-09-13T00:20:00+09:00', '2026년 9월 13일 오전 12시 20분'),
])
def test_customer_time_uses_kst_across_date_and_noon_boundaries(value, expected):
    assert customer_time(datetime.fromisoformat(value)) == expected


def test_unknown_delay_is_not_presented_as_on_time_and_missing_time_is_omitted():
    fact = ToolResultNormalizer().normalize(Capability.DELIVERY_CURRENT, {
        **DELIVERY, 'delayStatus': 'UNKNOWN', 'statusChangedAt': None,
    })
    assert '지연 여부는 아직 확인할 수 없어요' in fact.safe_answer
    assert '시각' not in fact.safe_answer


def test_failed_payment_is_not_presented_as_completed():
    fact = ToolResultNormalizer().normalize(Capability.PAYMENT_CURRENT, {
        **PAYMENT, 'status': 'FAILED', 'amount': 15900,
    })
    assert '실패' in fact.safe_answer
    assert '완료' not in fact.safe_answer
    assert '15,900원' in fact.safe_answer


@pytest.mark.parametrize('capability,payload,field', [
    (Capability.PAYMENT_CURRENT, PAYMENT, 'status'),
    (Capability.PAYMENT_CURRENT, PAYMENT, 'paymentType'),
    (Capability.REFUND_RECENT, REFUND, 'status'),
    (Capability.SUBSCRIPTION_CURRENT, SUBSCRIPTION, 'status'),
    (Capability.DELIVERY_CURRENT, DELIVERY, 'status'),
    (Capability.DELIVERY_CURRENT, DELIVERY, 'delayStatus'),
])
def test_new_unapproved_codes_fail_closed(capability, payload, field):
    fact = ToolResultNormalizer().normalize(capability, {**payload, field: 'INTERNAL_NEW_CODE'})
    assert fact.error_code == StateErrorCode.CONTRACT_ERROR
    assert fact.safe_answer is None
    assert not fact.values
