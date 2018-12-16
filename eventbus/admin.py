from django.contrib import admin

from .models import EventMessage, ModelEventMessage


class EventMessageAdmin(admin.ModelAdmin):
    pass


class ModelEventMessageAdmin(admin.ModelAdmin):
    pass


admin.register(EventMessage, EventMessageAdmin)
admin.register(ModelEventMessage, ModelEventMessageAdmin)
