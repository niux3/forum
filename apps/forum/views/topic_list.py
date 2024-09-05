from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Count
from django.views.generic import ListView
from django.http import Http404
from django.utils.http import urlencode
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
        self.has_filter = len(self.request.GET) == 1 and self.attribute_querystring in self.request.GET.keys()

    def get_queryset(self):
        queryset = self.board.topics.order_by('-updated').annotate(replies=Count('posts') - 1)
        if self.has_filter:
            print(self.board.topics.filter(posts__created_by=self.request.user))
            querysets = {
                self.filters['most_popular']: self.board.topics.order_by('-views').annotate(replies=Count('posts') - 1),
                self.filters['most_answers']: self.board.topics.annotate(replies=Count('posts') - 1).order_by('-replies'),
                self.filters['user']: self.board.topics.filter(posts__created_by=self.request.user).annotate(replies=Count('posts') - 1).order_by('-updated') if self.request.user.is_authenticated else None,
            }
            filter_name = self.request.GET.get(self.attribute_querystring)
            if filter_name == self.filters['user'] and not self.request.user.is_authenticated:
                raise Http404()
            queryset = querysets[filter_name]
        return queryset

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        base_url = reverse_lazy('forum:topics', kwargs={
            'id': self.board.id,
            'slug': self.board.slug
        })

        actives = {
            'base': 'active' if self.request.get_full_path() == base_url else '',
        }

        for k, v in self.filters.items():
            if self.has_filter:
                url = ("%s?%s=%s") % (base_url, self.attribute_querystring, v)
                actives[k] = 'active' if self.request.get_full_path().replace('%20', ' ') == url else ''
            else:
                actives[k] = ''

        ctx['board'] = self.board
        ctx['filters'] = self.filters
        ctx['attribute_querystring'] = self.attribute_querystring
        ctx['active'] = actives
        return ctx
