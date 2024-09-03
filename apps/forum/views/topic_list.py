from pprint import pprint
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.views.generic import ListView
from django.http import Http404
from forum.models import Board, Topic


class TopicList(ListView):
    template_name = 'forum/topics.html'
    paginate_by = 30

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.board = get_object_or_404(
            Board, 
            pk=self.kwargs.get('id'), 
            slug=self.kwargs.get('slug')
        )
        self.attribute_querystring = 'filtre'
        self.filters = {
            'most_popular': 'les plus lus',
            'most_answers': 'les plus repondu',
            'user': 'utilisateur'
        }

    def get_queryset(self):
        queryset = self.board.topics.order_by('-updated').annotate(replies=Count('posts') - 1)
        querysets = {
            self.filters['most_popular']: self.board.topics.order_by('-views').annotate(replies=Count('posts') - 1),
            self.filters['most_answers']: self.board.topics.annotate(replies=Count('posts') - 1).order_by('-replies'),
            self.filters['user']: self.board.topics.filter(starter=self.request.user).annotate(replies=Count('posts') - 1).order_by('-updated'),
        }
        if len(self.request.GET) == 1:
            if self.attribute_querystring in self.request.GET.keys():
                filter_name = self.request.GET.get(self.attribute_querystring)
                if filter_name == self.filters['user'] and not self.request.user.is_authenticated:
                    raise Http404()
                queryset = querysets[filter_name]
            else:
                raise Http404()
        return queryset

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['board'] = self.board
        ctx['filters'] = self.filters
        ctx['attribute_querystring'] = self.attribute_querystring
        return ctx
