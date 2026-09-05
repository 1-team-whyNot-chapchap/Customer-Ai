from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor


class ThreadPoolSummaryJobScheduler:
    def __init__(self, *, max_workers: int = 2) -> None:
        if max_workers <= 0:
            raise ValueError("max_workers must be positive")
        self._executor = ThreadPoolExecutor(
            max_workers=max_workers, thread_name_prefix="consultation-summary"
        )

    def submit(self, task: Callable[[], None]) -> None:
        self._executor.submit(task)
