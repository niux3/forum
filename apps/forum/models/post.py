from django.db import models
from django.utils.text import Truncator
from django.contrib.auth.models import User


class Post(models.Model):
    message = models.TextField()
    topic = models.ForeignKey('Topic', related_name='posts', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, auto_now=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return Truncator(self.message).chars(30)
