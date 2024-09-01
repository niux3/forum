from django.contrib import admin
from forum.models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    ...
