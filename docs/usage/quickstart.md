Quickstart
==========

Configuration Settings
----------------------

Select a backend and configure django-eventbus settings, e.g.:
```
EVENTBUS = {
    'backend': 'eventbus.backends.KafkaBackend',
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
    url(r'^events/', eventbus.urls),
```

Configure event consumers and producers next.

Producer Configuration
----------------------

TODO: document `EventProducer` API example usage.

Consumer Configuration
----------------------

TODO: document `EventConsumer` API example usage.

Model Events
------------

A `ModelEvent` is created for every event consumed or produced by the
django-eventbus producers and consumers. This allows an additional level
of information within the application for tracking, retriggering, and
subscribing (e.g. with Django signals) events.

At the highest-level, a `ModelEvent` features a `model` and a `message`,
both of which are saved to the database after producing and consuming
events, with an automatically generated identifier for the event.
Additionally, a `type` field exists on the model describing the type
of event ('create', 'delete', or 'update').

Admin Dashboards
----------------

Document using `Events` admin views, including admin views for tracking
produced and consumed events, discussing retries, and examining success
and failure statuses.

Document using `EventManager` admin view, including monitoring consumer
processes, and starting/stopping event processes.

Next page: [API Reference](api_ref.md)
