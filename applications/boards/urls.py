from django.urls import path
from . import views


app_name = "boards"
urlpatterns = [
    path('', views.index, name="index"),
    path('<str:slug>-<int:id>/index.html', views.topics, name="topics"),
    path('<str:slug>-<int:id>/nouveau-sujet.html', views.create, name="create"),
    path('<str:slug>-<int:id>/<str:slug_post>-<int:id_post>.html', views.show_topic, name='show_topic'),
    path('reponse/<str:slug>-<int:id>/<str:slug_post>-<int:id_post>.html', views.reply_topic, name='reply_topic'),
]