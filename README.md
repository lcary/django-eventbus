django-eventbus
===============

The django-eventbus library is a reusable Django app that can be used
to implement the publish-subscribe architecture pattern.

WIP Notice
----------

This is a work in progress application, starting from documentation
and proceeding to library development. This notice will be removed once
the library is finally implemented.

Documentation
-------------

Online documentation is available at https://django-eventbus.readthedocs.io/.

Requirements
------------

Python 3.

Installation
------------

To install `django-eventbus`, run:
```
pip install django-eventbus
```

Configuration
-------------

1. Add `django-eventbus` into your `INSTALLED_APPS`:

```python
    INSTALLED_APPS = (
        ...
        'eventbus',
    )
```

2. Add eventbus backend settings to your `settings.py`:

```python
    EVENTBUS_BACKEND = {
        'backend': 'eventbus.backends.KafkaBackend',  # default
        'backend_settings': {
            'broker_hosts': ['127.0.0.1:9092'],
            'schema_registry_url': 'http://localhost:8081',
        }
    }
```

3. Create `django-eventbus` database tables by running:

```
python manage.py migrate
```

Usage
-----


Admin Integration
-----------------
