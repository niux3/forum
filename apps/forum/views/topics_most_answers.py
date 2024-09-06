from django.db.models import Count
from forum.views import TopicList


class TopicsMostAnswers(TopicList):
    def get_queryset(self):
        queryset = self.board.topics.annotate(replies=Count('posts') - 1).order_by('-replies')
        return queryset
