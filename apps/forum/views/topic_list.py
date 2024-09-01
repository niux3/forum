from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.views.generic import ListView
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

    def get_queryset(self):
        return self.board.topics.order_by('-updated').annotate(replies=Count('posts') - 1)

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['board'] = self.board
        return ctx
