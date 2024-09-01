from django.contrib import admin
from boards.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...
