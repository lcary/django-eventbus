API Reference
=============

There are 2 primary interfaces used in this library:
 1. `Producer`: an object that that has a `.produce()` method.
 2. `Consumer`: an object that that has a `.consume()` method.

Model Event Messaging
---------------------

A `ModelEvent` is created for every event consumed or produced by the
django-eventbus producers and consumers. This allows an additional level
of information within the application for tracking, retriggering, and
subscribing (e.g. with Django signals) events.

At the highest-level, a `ModelEvent` features a `model` and a `message`,
both of which are saved to the database after producing and consuming
events, with an automatically generated identifier for the event.
Additionally, a `type` field exists on the model describing the type
of event ('create', 'delete', or 'update').

Message Serializers
-------------------

The `MessageSerializer` provides an interface for converting
Python datatypes to a specific message format, and vice versa.

The `MessageSerializer` has a `serialize()` and `deserialize()`
method, both of which are optional. However, the `serialize()`
method is called by producers, and the `deserialize()` method
is called by consumers.

Custom Messaging
----------------

The `Producer` and `Consumer` classes are useful
for implementing custom producers and consumers for any kind of
data.

#### Producer

A custom producer must implement the `.produce()` method.

Configure a custom message producer:
```python
from eventbus import Producer

class MyProducer(Producer):

    def produce(self, data):
        ...
```

To use a message producer elsewhere in your code, call:
```python
producer = Producer()
producer.produce(data)
```

The backends for producers and consumers use the `EVENTBUS['backend_class']`
setting by default, but can be overridden at the class level if desired.

For producers:
```python
from eventbus import Producer
from eventbus.backends import KafkaBackend


class MyProducer(Producer):
	backend_class = KafkaBackend
	...
```

#### Consumer

Similar to producers a custom consumer must implement the `.consume()` method.

```python
from eventbus import Consumer

class MyConsumer(Consumer):

    def consume(self, message):
        ...
```

Any processing logic that you would want to perform on a consumed message
can be implemented here.

Consumers can also override the default `EVENTBUS['backend_class']`
setting at the class level if desired.

```python
from eventbus import Consumer
from eventbus.backends import KafkaBackend


class MyConsumer(Consumer):
	backend_class = KafkaBackend
	...
```

To use a consumer, you can call the consume method directly:

```python
consumer = Consumer()
data = consumer.consume()
```

Or to consume in the background:

```python
from eventbus.consumers import BackgroundConsumerThread


class   

```
