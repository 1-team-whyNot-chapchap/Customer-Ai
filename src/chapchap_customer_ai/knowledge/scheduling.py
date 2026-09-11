from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor


class ThreadPoolJobScheduler:
    def __init__(self, *, max_workers: int = 2) -> None:
        if max_workers <= 0:
            raise ValueError("max_workers must be positive")
        self._executor = ThreadPoolExecutor(
            max_workers=max_workers, thread_name_prefix="knowledge-processing"
        )

    def submit(self, task: Callable[[], None]) -> None:
        self._executor.submit(task)

    def close(self) -> None:
        self._executor.shutdown(wait=True, cancel_futures=False)
