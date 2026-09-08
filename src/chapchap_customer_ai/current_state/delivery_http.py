"""Delivery's dedicated customer-ai current-state contract."""

import json
import math
import time
from collections.abc import Mapping
from dataclasses import dataclass

import httpx
from pydantic import SecretStr

from chapchap_customer_ai.consultation.models import Capability, StateErrorCode
from chapchap_customer_ai.contracts.models import UserRole
from chapchap_customer_ai.current_state.http import validate_subscription_origin
from chapchap_customer_ai.current_state.models import TransportOutcome, TransportResult
from chapchap_customer_ai.current_state.normalization import ToolResultNormalizer
from chapchap_customer_ai.current_state.ports import CurrentStateTransport
from chapchap_customer_ai.security.models import AuthenticatedContext


@dataclass(frozen=True, slots=True)
class HttpDeliveryCurrentStateTransport:
    client: httpx.Client
    base_url: str
    api_key: SecretStr
    allow_loopback_http: bool = False

    def __post_init__(self):
        key = self.api_key.get_secret_value()
        if not key or any(ord(c) < 33 or ord(c) > 126 for c in key):
            raise ValueError("Delivery API key must be nonempty printable ASCII without spaces")
        object.__setattr__(
            self,
            "base_url",
            validate_subscription_origin(
                self.base_url, allow_loopback_http=self.allow_loopback_http
            ),
        )

    def invoke(
        self,
        tool_name: str,
        arguments: Mapping[str, object],
        security_context: AuthenticatedContext,
        *,
        required_scope: str,
        timeout_seconds: float,
    ) -> TransportResult:
        if (
            tool_name != "get_current_delivery_state"
            or not isinstance(arguments, Mapping)
            or arguments
        ):
            return TransportResult(TransportOutcome.CONTRACT_ERROR)
        subject = security_context.subject
        if (
            security_context.service_subject != "customer-service"
            or subject.role != UserRole.CUSTOMER
            or type(subject.user_id) is not int
            or not 0 < subject.user_id <= 2**63 - 1
            or required_scope != "delivery.status.read"
            or required_scope not in subject.allowed_ai_scopes
        ):
            return TransportResult(TransportOutcome.FORBIDDEN)
        if not math.isfinite(timeout_seconds) or timeout_seconds <= 0:
            return TransportResult(TransportOutcome.TIMEOUT)
        deadline = time.monotonic() + min(timeout_seconds, 2.0)
        try:
            headers = {
                "X-Internal-Service": "customer-ai",
                "X-Internal-Api-Key": self.api_key.get_secret_value(),
                "X-Internal-Scope": "delivery.status.read",
                "X-User-Id": str(subject.user_id),
                "X-User-Role": "CUSTOMER",
            }
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                return TransportResult(TransportOutcome.TIMEOUT)
            request = httpx.Request(
                "GET",
                f"{self.base_url}/internal/deliveries/current",
                headers={**headers, "Accept": "application/json"},
                extensions={"timeout": httpx.Timeout(remaining).as_dict()},
            )
            response = self.client.send(request, auth=None, follow_redirects=False, stream=True)
            try:
                if time.monotonic() >= deadline:
                    return TransportResult(TransportOutcome.TIMEOUT)
                status = response.status_code
                if status in {401, 403}:
                    return TransportResult(TransportOutcome.FORBIDDEN)
                if status >= 500:
                    return TransportResult(TransportOutcome.UNAVAILABLE)
                if (
                    status not in {200, 404}
                    or response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
                    != "application/json"
                ):
                    return TransportResult(TransportOutcome.CONTRACT_ERROR)
                content = bytearray()
                for block in response.iter_bytes():
                    if time.monotonic() >= deadline:
                        return TransportResult(TransportOutcome.TIMEOUT)
                    content.extend(block)
                    if len(content) > 65536:
                        return TransportResult(TransportOutcome.CONTRACT_ERROR)
                envelope = json.loads(content)
            finally:
                response.close()
        except (TimeoutError, httpx.TimeoutException):
            return TransportResult(TransportOutcome.TIMEOUT)
        except PermissionError:
            return TransportResult(TransportOutcome.FORBIDDEN)
        except (ConnectionError, httpx.TransportError):
            return TransportResult(TransportOutcome.UNAVAILABLE)
        except Exception:
            return TransportResult(TransportOutcome.CONTRACT_ERROR)
        if (
            not isinstance(envelope, dict)
            or set(envelope) != {"code", "message", "data"}
            or not isinstance(envelope["message"], str)
        ):
            return TransportResult(TransportOutcome.CONTRACT_ERROR)
        if status == 404:
            if envelope["code"] == "DELIVERY_036" and envelope["data"] is None:
                return TransportResult(TransportOutcome.BUSINESS_NOT_FOUND)
            return TransportResult(TransportOutcome.CONTRACT_ERROR)
        if (
            envelope["code"] != "00"
            or not isinstance(envelope["data"], dict)
            or "availability" in envelope["data"]
        ):
            return TransportResult(TransportOutcome.CONTRACT_ERROR)
        payload = {"availability": "AVAILABLE", **envelope["data"]}
        normalized = ToolResultNormalizer().normalize(Capability.DELIVERY_CURRENT, payload)
        if normalized.error_code == StateErrorCode.CONTRACT_ERROR:
            return TransportResult(TransportOutcome.CONTRACT_ERROR)
        return TransportResult(TransportOutcome.SUCCESS, payload)


@dataclass(frozen=True, slots=True)
class DomainCurrentStateTransport:
    subscription: CurrentStateTransport | None = None
    delivery: CurrentStateTransport | None = None

    def invoke(self, tool_name, arguments, security_context, *, required_scope, timeout_seconds):
        if tool_name == "get_current_delivery_state":
            target = self.delivery
        elif tool_name in {
            "get_current_payment_state",
            "get_recent_refund_result",
            "get_current_subscription_state",
        }:
            target = self.subscription
        else:
            return TransportResult(TransportOutcome.CONTRACT_ERROR)
        if target is None:
            return TransportResult(TransportOutcome.UNAVAILABLE)
        return target.invoke(
            tool_name,
            arguments,
            security_context,
            required_scope=required_scope,
            timeout_seconds=timeout_seconds,
        )
