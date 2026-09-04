class RuntimeNotReadyError(RuntimeError):
    """연동 의존성이 활성화 조건을 통과하지 못했을 때 발생한다."""


def require_runtime_ready(component: str) -> None:
    raise RuntimeNotReadyError(
        f"{component} is not activated. "
        "Complete the Customer-Service contract and security tests first."
    )
