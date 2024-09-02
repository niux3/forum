from django.db import models
from django.contrib.auth.models import User
from forum.models import Post


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey('Board', related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject

    def get_last_post(self):
        return Post.objects.filter(topic=self).order_by('-updated').first()

    def get_post_count(self):
        return Post.objects.filter(topic=self).count() - 1

    def get_post(self):
        return Post.objects.get(id=self.id)

