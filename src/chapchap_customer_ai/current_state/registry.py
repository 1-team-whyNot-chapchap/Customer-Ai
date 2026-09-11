from types import MappingProxyType

from chapchap_customer_ai.consultation.models import Capability
from chapchap_customer_ai.current_state.models import CapabilityBinding

CAPABILITY_REGISTRY = MappingProxyType(
    {
        Capability.PAYMENT_CURRENT: CapabilityBinding(
            Capability.PAYMENT_CURRENT,
            "get_current_payment_state",
            "subscription.payment.read",
            "subscription-service",
        ),
        Capability.REFUND_RECENT: CapabilityBinding(
            Capability.REFUND_RECENT,
            "get_recent_refund_result",
            "subscription.refund.read",
            "subscription-service",
        ),
        Capability.SUBSCRIPTION_CURRENT: CapabilityBinding(
            Capability.SUBSCRIPTION_CURRENT,
            "get_current_subscription_state",
            "subscription.status.read",
            "subscription-service",
        ),
        Capability.DELIVERY_CURRENT: CapabilityBinding(
            Capability.DELIVERY_CURRENT,
            "get_current_delivery_state",
            "delivery.status.read",
            "delivery-service",
        ),
    }
)
