Installation
============

First, install via pip:
```
pip install django-eventbus
```

Then, add to `INSTALLED_APPS` in your Django settings file::
```python
INSTALLED_APPS = [
    ...
    'eventbus'
]
```
This will ensure the django-eventbus migrations are run.

To run migrations, run the typical `manage.py migrate` command.
This will create the `modelevent` table and allow you to begin
configuring your Django application to use `django-eventbus`.

Next page: [Quickstart](quickstart.md)
