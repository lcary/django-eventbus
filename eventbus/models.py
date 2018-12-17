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


class EventTopic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class EventMessage(models.Model):
    """
    A EventMessage is created for every event consumed or produced by the
    django-eventbus producers and consumers.
    """
    topic = models.ForeignKey(EventTopic, on_delete=models.CASCADE)
    data = models.TextField()
    processed = models.DateTimeField()
    success = models.BooleanField()

    class Meta:
        abstract = True


class ConsumerEvent(EventMessage):
    """
    A ConsumerEvent is created for every event consumed by the
    django-eventbus consumers.
    """


class ProducerEvent(EventMessage):
    """
    A ProducerEvent is created for every event produced by the
    django-eventbus producers.
    """


class ModelEvent(models.Model):
    """
    A ModelEvent is created for every event consumed or produced by the
    django-eventbus ModelEvent producers and consumers.
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    message = models.ForeignKey(EventMessage, on_delete=models.CASCADE)
    event_type = models.CharField(
        max_length=1,
        choices=ModelEventTypeChoice.get_choices())

    class Meta:
        abstract = True


class ConsumerModelEvent(ModelEvent):
    """
    A ConsumerModelEvent is created for every event consumed by the
    django-eventbus consumers.
    """
    message = models.ForeignKey(ConsumerEvent, on_delete=models.CASCADE)


class ProducerModelEvent(ModelEvent):
    """
    A ProducerModelEvent is created for every event produced by the
    django-eventbus producers.
    """
    message = models.ForeignKey(ProducerEvent, on_delete=models.CASCADE)
