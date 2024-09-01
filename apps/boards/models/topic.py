from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey('Board', related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject
