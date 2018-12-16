import logging
from typing import Any

from confluent_kafka import avro
from confluent_kafka.avro import AvroConsumer, AvroProducer

from eventbus.utils.settings import eventbus_settings

log = logging.getLogger(__name__)


class AvroConsumerBackend(object):
    """
    Backend for consuming Avro messages from a Kafka topic.
    """
    timeout = eventbus_settings.get_or_default('CONSUMER_TIMEOUT')

    def __init__(self, topic: str) -> None:
        self.topic = topic
        self._consumer = AvroConsumer(getattr(eventbus_settings, topic))

    def subscribe(self) -> None:
        self._consumer.subscribe([self.topic])

    def get_message(self) -> Any:
        message = self._consumer.poll(timeout=self.timeout)
        if message is None:
            return None
        if message.error():
            if message.error().code() == KafkaError._PARTITION_EOF:
                return None
            else:
                log.error(message.error())
                return None
        return message.value()

    @staticmethod
    def error_callback(err):
        log.error(err)


class AvroProducerBackend(object):
    """
    Backend for producing Avro messages to a Kafka topic.
    """
    timeout = eventbus_settings.get_or_default('PRODUCER_TIMEOUT')

    def __init__(self, topic: str, schema_path: str) -> None:
        self._topic = topic
        self._schema = avro.load(schema_path)
        self._producer = AvroProducer(
            getattr(eventbus_settings, topic), default_key_schema=self._schema)

    def produce(self, value: Any) -> None:
        """
        Produce a mesage to
        """
        self._producer.poll(self.timeout)
        self._producer.produce(
            topic=self._topic, value=value, value_schema=self._schema)
        self._producer.flush()
