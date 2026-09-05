import time
from collections.abc import Callable, Sequence
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from types import MappingProxyType

from chapchap_customer_ai.consultation.models import (
    Capability,
    StateAvailability,
    StateErrorCode,
    StateFact,
)
from chapchap_customer_ai.contracts.models import UserRole
from chapchap_customer_ai.current_state.models import (
    CapabilityBinding,
    CurrentStateRequestError,
    TransportOutcome,
    TransportResult,
)
from chapchap_customer_ai.current_state.normalization import ToolResultNormalizer
from chapchap_customer_ai.current_state.ports import CurrentStateTransport
from chapchap_customer_ai.current_state.registry import CAPABILITY_REGISTRY
from chapchap_customer_ai.security.models import AuthenticatedContext

EMPTY_TOOL_ARGUMENTS = MappingProxyType({})


@dataclass(frozen=True, slots=True)
class CurrentStateAdapter:
    transport: CurrentStateTransport
    normalizer: ToolResultNormalizer = field(default_factory=ToolResultNormalizer)
    monotonic: Callable[[], float] = time.monotonic

    def fetch(
        self,
        capabilities: Sequence[Capability],
        context: AuthenticatedContext,
        *,
        timeout_seconds: float,
    ) -> Sequence[StateFact]:
        requested = tuple(capabilities)
        if timeout_seconds <= 0:
            raise ValueError("Current-State timeout must be positive")
        if not 1 <= len(requested) <= 2:
            raise CurrentStateRequestError("One or two unique capabilities are required.")
        if any(not isinstance(capability, Capability) for capability in requested):
            raise CurrentStateRequestError("An unregistered capability was requested.")
        if len(set(requested)) != len(requested):
            raise CurrentStateRequestError("One or two unique capabilities are required.")

        bindings = tuple(CAPABILITY_REGISTRY.get(capability) for capability in requested)
        if any(binding is None for binding in bindings):
            raise CurrentStateRequestError("An unregistered capability was requested.")
        approved_bindings = tuple(binding for binding in bindings if binding is not None)

        if not self._context_is_authorized(context, approved_bindings):
            return tuple(
                StateFact(binding.capability, StateAvailability.FORBIDDEN)
                for binding in approved_bindings
            )

        deadline = self.monotonic() + timeout_seconds
        if len(approved_bindings) == 1:
            return (self._fetch_one(approved_bindings[0], context, deadline),)
        with ThreadPoolExecutor(max_workers=2, thread_name_prefix="current-state") as executor:
            futures = tuple(
                executor.submit(self._fetch_one, binding, context, deadline)
                for binding in approved_bindings
            )
            return tuple(future.result() for future in futures)

    @staticmethod
    def _context_is_authorized(
        context: AuthenticatedContext, bindings: Sequence[CapabilityBinding]
    ) -> bool:
        return (
            context.service_subject == "customer-service"
            and context.subject.role in {UserRole.CUSTOMER, UserRole.RIDER}
            and all(
                binding.required_scope in context.subject.allowed_ai_scopes
                for binding in bindings
            )
        )

    def _fetch_one(
        self,
        binding: CapabilityBinding,
        context: AuthenticatedContext,
        deadline: float,
    ) -> StateFact:
        for attempt in range(2):
            remaining = deadline - self.monotonic()
            if remaining <= 0:
                return StateFact(binding.capability, StateAvailability.TIMEOUT)
            try:
                result = self.transport.invoke(
                    binding.tool_name,
                    EMPTY_TOOL_ARGUMENTS,
                    context,
                    required_scope=binding.required_scope,
                    timeout_seconds=remaining,
                )
            except TimeoutError:
                return StateFact(binding.capability, StateAvailability.TIMEOUT)
            except PermissionError:
                return StateFact(binding.capability, StateAvailability.FORBIDDEN)
            except ConnectionError:
                result = TransportResult(TransportOutcome.UNAVAILABLE, retryable=True)
            except Exception:
                return StateFact(
                    binding.capability,
                    None,
                    error_code=StateErrorCode.CONTRACT_ERROR,
                )
            if not isinstance(result, TransportResult):
                return StateFact(
                    binding.capability,
                    None,
                    error_code=StateErrorCode.CONTRACT_ERROR,
                )
            if self.monotonic() >= deadline:
                return StateFact(binding.capability, StateAvailability.TIMEOUT)
            if (
                result.outcome == TransportOutcome.UNAVAILABLE
                and result.retryable
                and attempt == 0
            ):
                continue
            return self._normalize_transport_result(binding.capability, result)
        return StateFact(binding.capability, StateAvailability.UNAVAILABLE)

    def _normalize_transport_result(
        self, capability: Capability, result: TransportResult
    ) -> StateFact:
        if result.outcome == TransportOutcome.SUCCESS and result.payload is not None:
            return self.normalizer.normalize(capability, result.payload)
        availability = {
            TransportOutcome.BUSINESS_NOT_FOUND: StateAvailability.NOT_FOUND,
            TransportOutcome.FORBIDDEN: StateAvailability.FORBIDDEN,
            TransportOutcome.UNAVAILABLE: StateAvailability.UNAVAILABLE,
            TransportOutcome.TIMEOUT: StateAvailability.TIMEOUT,
        }.get(result.outcome)
        if availability is not None:
            return StateFact(capability, availability)
        return StateFact(capability, None, error_code=StateErrorCode.CONTRACT_ERROR)
