from django.db.models import Count
from forum.views import TopicList


class TopicsMostRead(TopicList):
    def get_queryset(self):
        queryset = self.board.topics.order_by('-views').annotate(replies=Count('posts') - 1)
        return queryset
