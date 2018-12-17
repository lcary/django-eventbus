from django.contrib import admin

from .models import (
    EventTopic,
    ConsumerEvent,
    ProducerEvent,
    ConsumerModelEvent,
    ProducerModelEvent)


@admin.register(EventTopic)
class EventTopicAdmin(admin.ModelAdmin):
    pass


@admin.register(ConsumerEvent)
class ConsumerEventAdmin(admin.ModelAdmin):
    pass


@admin.register(ProducerEvent)
class ProducerEventAdmin(admin.ModelAdmin):
    pass


@admin.register(ConsumerModelEvent)
class ConsumerModelEventAdmin(admin.ModelAdmin):
    pass


@admin.register(ProducerModelEvent)
class ProducerModelEventAdmin(admin.ModelAdmin):
    pass
