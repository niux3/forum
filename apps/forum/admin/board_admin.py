from django.contrib import admin
from forum.models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name', ]
    }
