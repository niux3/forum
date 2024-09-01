from django.contrib import admin
from django.apps import apps
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

for app_name, app_object in apps.app_configs.items():
    if hasattr(app_object, 'url_root'):
        # try:
        included = include(f'{app_name}.urls', namespace=app_object.name)
        route = path(app_object.url_root, included)
        urlpatterns.append(route)
        print('>', app_name, 'urls loaded')
        # except ImportError as e:
            # #TODO logger
            # print(f'The app "{app_name}" has no "urls" module.')
