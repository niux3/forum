from random import choice, randint
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from forum.models import Post, Topic
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker('fr-FR')
        topics = Topic.objects.all()
        users = User.objects.all()

        for topic in topics:
            for _ in range(randint(0, 3)):
                post = Post()
                post.topic = topic
                post.created_by = choice(users)
                post.message = fake.paragraph(nb_sentences=randint(5, 10))
                post.save()

