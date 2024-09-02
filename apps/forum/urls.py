from django.urls import path, re_path
from forum.apps import ForumConfig
from forum.views import (
    BoardList,
    TopicList,
    TopicDetail,
    TopicCreate,
    TopicReply,
    PostEdit,
    LastTopicsList,
)

app_name = ForumConfig.name
urlpatterns = [
    path('', BoardList.as_view(), name='index'),
    re_path(r'^(?P<categories>(derniers|mes)-sujets).html$', LastTopicsList.as_view(), name='last_topics'),
    path('<str:slug>-<int:id>/index.html', TopicList.as_view(), name='topics'),
    path('<str:slug>-<int:id>/<str:slug_post>-<int:id_post>.html', TopicDetail.as_view(), name='show_topic'),
    path('<str:slug>-<int:id>/nouveau-sujet.html', TopicCreate.as_view(), name='create'),
    path('<str:slug>-<int:id>/reponse/<str:slug_post>-<int:id_post>.html', TopicReply.as_view(), name='reply_topic'),
    path('<str:slug>-<int:id>/editer/<str:slug_post>-<int:id_post>-<int:id_message>.html', PostEdit.as_view(), name='edit_post'),
]
