from django.views.generic import ListView
from forum.models import Topic


class LastTopicsList(ListView):
    model = Topic
    template_name = 'forum/last_topics.html'

    def get_queryset(self):
        max_topic = 30
        queryset = Topic.objects.all().order_by('-updated')[:max_topic]
        if self.kwargs.get('categories') and self.request.user.is_authenticated and self.kwargs.get('categories').startswith('mes'):
            queryset = Topic.objects.filter(starter=self.request.user).order_by('-updated')[:max_topic]
        return queryset
