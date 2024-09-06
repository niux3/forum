from django.db.models import Count
from forum.views import TopicList


class TopicsWichUserReplied(TopicList):
    def get_queryset(self):
        queryset = self.board.topics.filter(posts__created_by=self.request.user).annotate(replies=Count('posts') - 1).order_by('-updated')
        return queryset
