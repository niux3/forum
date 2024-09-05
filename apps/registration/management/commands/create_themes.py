from django.core.management.base import BaseCommand
from django.conf import settings
from registration.models import Theme


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        root = settings.BASE_DIR
        themes_folder = root / 'apps' / 'core' / 'static' / 'css' / 'themes'
        for theme in themes_folder.glob('*.css'):
            Theme(name=theme.stem.lower()).save()
        print('Done !')
