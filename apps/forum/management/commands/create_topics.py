from random import choice, randint
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from forum.models import Board, Post, Topic
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker('fr-FR')
        boards = Board.objects.all()
        users = User.objects.all()
        for board in boards:
            for _ in range(randint(30, 50)):
                user = choice(users)
                subject = fake.paragraph(nb_sentences=1)
                topic = Topic()
                topic.board = board
                topic.starter = user
                topic.subject = subject
                topic.slug = slugify(subject)
                topic.save()

                post = Post()
                post.topic = topic
                post.message = ''.join([
                    f"{fake.paragraph(nb_sentences=randint(5, 40))}\n\n" 
                    for _ in range(randint(3, 20))
                ])
                post.created_by = user
                post.save()
        print('done !')
