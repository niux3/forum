from itertools import chain
from django.views.generic import ListView
from forum.models import Topic, Post


class TopicSearch(ListView):
    model = Topic
    paginate_by = 30
    template_name = 'forum/search_topics.html'

    def get_queryset(self):
        additionnal = None
        params = {
            'subject__contains': self.request.GET.get('q')
        }
        if self.request.GET.get('boards') != '':
            params['board'] = self.request.GET.get('boards')
        if self.request.GET.get('users') != '':
            params['starter'] = self.request.GET.get('users')
        if self.request.GET.get('search_in') != '' and self.request.GET.get('search_in') == 'topics_posts':
            additionnal = Post.objects.filter(message__contains=self.request.GET.get('q'))
        queryset = Topic.objects.filter(**params)
        return queryset if additionnal is not None else queryset
