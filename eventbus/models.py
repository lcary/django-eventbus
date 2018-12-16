from enum import Enum

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class ModelEventTypeChoice(Enum):
    CREATION = 'Model Object Creation'
    MODIFICATION = 'Model Object Modification'
    DELETION = 'Model Object Deletion'

    @classmethod
    def get_choices(cls):
        return [(tag, tag.value) for tag in cls]


class Event(models.Model):
    """
    A EventMessage is created for every event consumed or produced by the
    django-eventbus producers and consumers.
    """
    topic = models.CharField(max_length=255)
    message = models.BinaryField()
    processed = models.DateTimeField()

    class Meta:
        abstract = True


class EventMessage(Event):
    """
    A EventMessage is created for every event consumed or produced by the
    django-eventbus producers and consumers.
    """


class ModelEventMessage(Event):
    """
    A ModelEvent is created for every event consumed or produced by the
    django-eventbus ModelEvent producers and consumers. This allows an additional
    level of information within the application for tracking, retriggering,
    and subscribing (e.g. with Django signals) events.
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    event_type = models.CharField(
        max_length=1,
        blank=True,
        null=True,
        choices=ModelEventTypeChoice.get_choices())
