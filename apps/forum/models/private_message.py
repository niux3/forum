from django.db import models
from django.contrib.auth.models import User


class PrivateMessage(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='private_message_from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='private_message_to_user')
    message = models.TextField(max_length=8192)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"({self.created}) {self.from_user.username} -> {self.to_user.username}"

