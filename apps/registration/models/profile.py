from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from registration.models import Theme


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, related_name='profile')
    bio = models.TextField(max_length=8192, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.CharField(max_length=16, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    newsletter = models.BooleanField(default=False, blank=True, null=True)
    private_message = models.BooleanField(default=True, blank=True, null=True)
    show_email = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
