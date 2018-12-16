import abc
import threading
from typing import Any, Callable

AnyCallable = Callable[[Any], Any]


class TaskScheduler(abc.ABC):
    @abc.abstractmethod
    def start(self, task: AnyCallable) -> None:
        pass


class BackgroundThread(TaskScheduler):
    def start(self, task: AnyCallable) -> None:
        thread = threading.Thread(target=task)
        thread.daemon = True
        thread.start()
