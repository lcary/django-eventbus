Quickstart
==========

Configuration Settings
----------------------

Select a backend and configure django-eventbus settings, e.g.:
```
EVENTBUS = {
    'backend_class': 'eventbus.backends.KafkaBackend',
    'backend_settings': {
        'broker_hosts': ['127.0.0.1:9092'],
        'schema_registry_url': 'http://localhost:8081',
    }
}
```

Optionally, add the django-eventbus urls to your `urls.py` file:
```
urlpatterns = [
    ...
    url(r'^eventbus/', eventbus.urls),
```

Kafka Messaging
---------------

Use the `AvroProducer` and `AvroConsumer` classes
to implement producers and consumers for Avro messages that
you want to produce to or consume from a Kafka queue.

#### Avro Producer

A custom producer must implement the `.produce()` method.

Configure a Kafka message producer:
```python
from eventbus import AvroProducer

class MyAvroProducer(AvroProducer):
	settings_key = 'my_avro_producer'

    def produce(self, data):
        ...
```

Note the `settings_key` above. This should correspond to a setting:
```
EVENTBUS

{
                'bootstrap.servers': self.settings.KAFKA_HOSTS,
                'schema.registry.url': self.settings.SCHEMA_REGISTRY_URL
            }
```

To use a message producer elsewhere in your code, call:
```python
producer = AvroProducer()
producer.produce(data)
```

The backends for producers and consumers use the `EVENTBUS['backend_class']`
setting by default, but can be overridden at the class level if desired.

For producers:
```python
from eventbus import AvroProducer
from eventbus.backends import KafkaBackend


class MyAvroProducer(AvroProducer):
	backend_class = KafkaBackend
	...
```

#### Avro Kafka Consumer

Similar to producers a custom consumer must implement the `.consume()` method.

```python
from eventbus import AvroConsumer

class MyAvroConsumer(AvroConsumer):

    def consume(self, message):
        ...
```

Any processing logic that you would want to perform on a consumed message
can be implemented here.

AvroConsumers can also override the default `EVENTBUS['backend_class']`
setting at the class level if desired.

```python
from eventbus import AvroConsumer
from eventbus.backends import KafkaBackend


class MyAvroConsumer(AvroConsumer):
	backend_class = KafkaBackend
	...
```

To use a consumer, you can call the consume method directly:

```python
consumer = AvroConsumer()
data = consumer.consume()
```

Or to consume in the background:

```python
from eventbus.consumers import BackgroundAvroConsumerThread


class   

```


Model Event Messaging
---------------------

`ModelEvent` messaging is useful for implementing standard
producers and consumers for model changes.

A `ModelEvent` is an object that can track the creation, modification,
or deletion of a Django model. Using the `ModelEventAvroProducer` and
`ModelEventAvroConsumer` classes, multiple services can quickly begin sharing
changes to models.

The `ModelEvent` classes should be used in the case of a service that requires
"Read Models". When a downstream service wants to be aware of changes to
particular models in an upstream service, the downstream service can implement
"Read Models" and reference the upstream models as database objects instead of
querying the upstream API.

#### ModelEventAvroProducer

#### ModelEventAvroConsumer


Admin Dashboards
----------------

Document using `Events` admin views, including admin views for tracking
produced and consumed events, discussing retries, and examining success
and failure statuses.

Document using `EventManager` admin view, including monitoring consumer
processes, and starting/stopping event processes.

The `ProducerEvent` and `ConsumerEvent` views show each event sent through
the queue.

Next page: [API Reference](api_ref.md)
