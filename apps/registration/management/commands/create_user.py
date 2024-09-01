from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker('fr-FR')
        for _ in range(25):
            profile = fake.simple_profile()
            user = User.objects.create_user(profile['username'], password='123456')
            user.email = profile['mail']
            user.save()
            print('*' * 80)
            print(f'username : {profile["username"]}')
            print(f'password : 123456')
            print(f'simple user created')

        admin = User.objects.create_user('admin', password='admin')
        admin.is_superuser = True
        admin.is_staff = True
        admin.save()
        print('*' * 80)
        print(f'username : admin')
        print(f'password : admin')
        print(f'super user created')
