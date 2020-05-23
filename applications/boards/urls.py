from django.urls import path
from . import views


app_name = "boards"
urlpatterns = [
    path('', views.index, name="index"),
    path('list-<int:id>-<str:slug>.html', views.topics, name="topics"),
    path('nouveau-sujet-<int:id>-<str:slug>.html', views.create, name="create"),
]