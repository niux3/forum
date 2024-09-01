from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from forum.models import Topic


class TopicDetail(DetailView):
    template_name = 'forum/show_post.html'

    def get_object(self):
        topic = get_object_or_404(
            Topic,
            board__pk=self.kwargs.get('id'),
            board__slug=self.kwargs.get('slug'), 
            pk=self.kwargs.get('id_post'), 
            slug=self.kwargs.get('slug_post')
        )
        topic.views += 1
        topic.save()
        return topic

