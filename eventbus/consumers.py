import abc
import logging
from typing import Any, Callable

from eventbus.backends.kafka import AvroConsumerBackend
from eventbus.schedulers import BackgroundThread

log = logging.getLogger(__name__)

AnyCallable = Callable[[Any], Any]


class InfiniteEventConsumer(abc.ABC):
    """
    Interface for a consumer that never stops consuming.

    Requires overriding the `consume()` method.
    Requires a `backend_class` attribute to be configured.
    Requires a `scheduler_class` attribute to be configured.
    """
    catch_exceptions = True

    @property
    def backend_class(self):
        raise NotImplementedError

    @property
    def scheduler_class(self):
        raise NotImplementedError

    @abc.abstractmethod
    def consume(self, message: Any) -> Any:
        """
        Method that requires override and runs on every message consumed.
        """
        pass

    def start(self) -> None:
        """
        Schedule the consumption of messages in an infinite loop.
        """
        self.scheduler_class.start(self.consume_forever)

    def consume_forever(self):
        """
        Consume messages in an infinite loop.
        """
        backend_class = self.backend_class()
        backend_class.subscribe()
        while True:
            try:
                message = backend_class.get_message()
            except Exception as e:
                if self.catch_exceptions:
                    log.error(e)
                else:
                    raise e
            else:
                if message:
                    self.consume(message)


class AvroConsumerThread(InfiniteEventConsumer, metaclass=abc.ABCMeta):
    """
    Interface for an Avro message consumer that runs
    on a background thread.

    Requires overriding the `consume()` method.
    """
    backend_class = AvroConsumerBackend
    scheduler_class = BackgroundThread
