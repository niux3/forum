from django.contrib import admin
from boards.models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    ...
