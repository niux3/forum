from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from forum.models import Board


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = [
            {
                "name": "Python",
                "description" : "Sujets généralistes ou relatifs à Python."
            },
            {
                "name": "Sémantique web et HTML",
                "description" : "Utiliser HTML au mieux pour structurer et décrire vos contenus."
            },
            {
                "name": "CSS et mise en forme, CSS3",
                "description" : "Utiliser les feuilles de styles pour habiller et mettre en page vos contenus."
            },
        ]
        for row in data:
            output = {**row, "slug": slugify(row['name'])}
            Board(**output).save()
        print('Done !')
