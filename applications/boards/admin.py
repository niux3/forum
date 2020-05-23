from django.contrib import admin
from .models import Board, Post, Topic


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post)
admin.site.register(Topic)