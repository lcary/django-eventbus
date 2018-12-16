django-eventbus
===============

The django-eventbus library is a reusable Django app that can be used
to implement the publish-subscribe architecture pattern.

WIP Notice
----------

This is a work in progress application, starting from documentation
and proceeding to library development. This notice will be removed once
the library is finally implemented.

Setup
-----

Install via pip:
```
pip install django-eventbus
```

Add to `INSTALLED_APPS` in your Django settings file:
```
INSTALLED_APPS = [
    ...
    'eventbus'
]
```
This will ensure the django-eventbus migrations are run during
`manage.py migrate` in order to create the `modelevent` table.

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

Admin Dashboards
----------------

Document using `Events` admin views, including admin views for tracking
produced and consumed events, discussing retries, and examining success
and failure statuses.

Document using `EventManager` admin view, including monitoring consumer
processes, and starting/stopping event processes.
