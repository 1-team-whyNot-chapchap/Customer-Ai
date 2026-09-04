class RuntimeNotReadyError(RuntimeError):
    """Raised when an integration dependency has not passed its activation conditions."""


def require_runtime_ready(component: str) -> None:
    raise RuntimeNotReadyError(
        f"{component} is not activated. "
        "Complete the Customer-Service contract and security tests first."
    )
