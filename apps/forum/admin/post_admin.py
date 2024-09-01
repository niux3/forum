from django.contrib import admin
from forum.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...
