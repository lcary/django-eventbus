import logging
from typing import Any

from eventbus.backends.kafka import AvroProducerBackend

logger = logging.getLogger(__name__)


class MessageProducer(object):
    """
    Class for producing messages to a queue.

    Requires a `backend_class` attribute to be configured.
    """

    @property
    def backend_class(self):
        raise NotImplementedError

    def produce(self, data):
        data = self.serialize(data)
        backend = self.backend_class()
        backend.produce(data)

    def serialize(self, data: Any) -> Any:
        """
        Overridable method that converts data into the correct message format.
        """
        return data


class AvroProducer(MessageProducer):
    """
    Class for producing Avro messages to a Kafka queue.
    """
    backend_class = AvroProducerBackend
