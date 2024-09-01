from django.urls import path
from forum.apps import ForumConfig
from forum.views import (
    BoardList,
    TopicList,
    TopicDetail,
    TopicCreate,
    TopicReply,
    PostEdit,
)


app_name = ForumConfig.name
urlpatterns = [
    path('', BoardList.as_view(), name="index"),
    path('<str:slug>-<int:id>/index.html', TopicList.as_view(), name="topics"),
    path('<str:slug>-<int:id>/<str:slug_post>-<int:id_post>.html', TopicDetail.as_view(), name='show_topic'),
    path('<str:slug>-<int:id>/nouveau-sujet.html', TopicCreate.as_view(), name="create"),
    path('<str:slug>-<int:id>/reponse/<str:slug_post>-<int:id_post>.html', TopicReply.as_view(), name='reply_topic'),
    path('<str:slug>-<int:id>/editer/<str:slug_post>-<int:id_post>-<int:id_message>.html', PostEdit.as_view(), name='edit_post'),
]
