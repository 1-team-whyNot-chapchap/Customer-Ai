"""Subscription SUB-FN-018 read-only HTTP boundary. No automatic retries."""

import json
import math
from collections.abc import Mapping
from dataclasses import dataclass
from urllib.parse import urlsplit

import httpx

from chapchap_customer_ai.consultation.models import StateErrorCode
from chapchap_customer_ai.contracts.models import UserRole
from chapchap_customer_ai.current_state.models import TransportOutcome, TransportResult
from chapchap_customer_ai.current_state.normalization import ToolResultNormalizer
from chapchap_customer_ai.current_state.registry import CAPABILITY_REGISTRY
from chapchap_customer_ai.security.models import AuthenticatedContext
from chapchap_customer_ai.security.transport import allowed_url

_PATHS = {
    "get_current_payment_state": "payment",
    "get_recent_refund_result": "refund",
    "get_current_subscription_state": "subscription",
}
_BINDINGS = {binding.tool_name: binding for binding in CAPABILITY_REGISTRY.values()}
_MAX_RESPONSE_BYTES = 64 * 1024


def validate_subscription_origin(
    value: str, *, allow_loopback_http: bool = False, http_allowed_origins: tuple[str, ...] = ()
) -> str:
    try:
        parsed = urlsplit(value)
        port = parsed.port
        local_http = (
            allow_loopback_http
            and parsed.scheme == "http"
            and parsed.hostname in {"localhost", "127.0.0.1", "::1"}
        )
        if (
            not parsed.hostname
            or (not allowed_url(value, http_allowed_origins, origin_only=True) and not local_http)
            or parsed.username is not None
            or parsed.password is not None
            or parsed.path not in {"", "/"}
            or parsed.query
            or parsed.fragment
            or (port is not None and port <= 0)
            or any(character.isspace() for character in value)
        ):
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError(
            "Subscription origin must be HTTPS or explicitly allowed loopback HTTP."
        ) from None
    return value.rstrip("/")


@dataclass(frozen=True, slots=True)
class HttpSubscriptionCurrentStateTransport:
    client: httpx.Client
    base_url: str
    allow_loopback_http: bool = False
    http_allowed_origins: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "base_url",
            validate_subscription_origin(
                self.base_url,
                allow_loopback_http=self.allow_loopback_http,
                http_allowed_origins=self.http_allowed_origins,
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
        binding = _BINDINGS.get(tool_name)
        if (
            tool_name not in _PATHS
            or binding is None
            or not isinstance(arguments, Mapping)
            or arguments
        ):
            return TransportResult(TransportOutcome.CONTRACT_ERROR)
        subject = security_context.subject
        if (
            security_context.service_subject != "customer-service"
            or subject.role not in {UserRole.CUSTOMER, UserRole.RIDER}
            or type(subject.user_id) is not int
            or not 0 < subject.user_id <= 2**63 - 1
            or required_scope != binding.required_scope
            or required_scope not in subject.allowed_ai_scopes
        ):
            return TransportResult(TransportOutcome.FORBIDDEN)
        if not math.isfinite(timeout_seconds) or timeout_seconds <= 0:
            return TransportResult(TransportOutcome.TIMEOUT)

        # Construct a fresh request: caller/client default cookies, auth, query and
        # headers must never become Subscription identity or authentication.
        request = httpx.Request(
            "GET",
            f"{self.base_url}/api/subscription/internal/v1/current-state/{_PATHS[tool_name]}",
            headers={"X-User-Id": str(subject.user_id), "Accept": "application/json"},
            extensions={"timeout": httpx.Timeout(timeout_seconds).as_dict()},
        )
        try:
            response = self.client.send(request, auth=None, follow_redirects=False, stream=True)
            try:
                if response.status_code in {401, 403}:
                    return TransportResult(TransportOutcome.FORBIDDEN)
                if response.status_code >= 500:
                    return TransportResult(TransportOutcome.UNAVAILABLE)
                if response.status_code != 200:
                    return TransportResult(TransportOutcome.CONTRACT_ERROR)
                if (
                    response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
                    != "application/json"
                ):
                    return TransportResult(TransportOutcome.CONTRACT_ERROR)
                content = bytearray()
                for block in response.iter_bytes():
                    content.extend(block)
                    if len(content) > _MAX_RESPONSE_BYTES:
                        return TransportResult(TransportOutcome.CONTRACT_ERROR)
                envelope = json.loads(content)
            finally:
                response.close()
        except httpx.TimeoutException:
            return TransportResult(TransportOutcome.TIMEOUT)
        except httpx.TransportError:
            return TransportResult(TransportOutcome.UNAVAILABLE)
        except (ValueError, UnicodeError):
            return TransportResult(TransportOutcome.CONTRACT_ERROR)

        if (
            not isinstance(envelope, dict)
            or set(envelope) != {"code", "message", "data"}
            or envelope["code"] != "00"
            or not isinstance(envelope["message"], str)
        ):
            return TransportResult(TransportOutcome.CONTRACT_ERROR)
        data = envelope["data"]
        if data is None:
            return TransportResult(TransportOutcome.BUSINESS_NOT_FOUND)
        if not isinstance(data, dict) or "availability" in data:
            return TransportResult(TransportOutcome.CONTRACT_ERROR)
        payload = {"availability": "AVAILABLE", **data}
        normalized = ToolResultNormalizer().normalize(binding.capability, payload)
        if normalized.error_code == StateErrorCode.CONTRACT_ERROR:
            return TransportResult(TransportOutcome.CONTRACT_ERROR)
        return TransportResult(TransportOutcome.SUCCESS, payload)
