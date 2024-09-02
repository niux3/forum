from django.views.generic import ListView
from forum.models import Post


class LastPostList(ListView):
    model = Post
    template_name = 'forum/last_posts.html'

    def get_queryset(self):
        max_post = 30
        queryset = Post.objects.all().order_by('-updated')[:max_post]
        if self.kwargs.get('categories') and self.request.user.is_authenticated and self.kwargs.get('categories').startswith('mes'):
            queryset = Post.objects.filter(created_by=self.request.user).order_by('-updated')[:max_post]
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['prefix'] = 'Mes' if self.request.user.is_authenticated and self.kwargs.get('categories').startswith('mes') else 'Dernières'
        return ctx
