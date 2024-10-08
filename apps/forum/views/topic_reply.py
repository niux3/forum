from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.utils.html import escape
from forum.forms import PostForm
from forum.models import Topic


class TopicReply(LoginRequiredMixin, CreateView):
    template_name = 'forum/reply_topic.html'
    form_class = PostForm

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.topic = get_object_or_404(
            Topic,
            board__slug=self.kwargs.get('slug'), 
            pk=self.kwargs.get('id_post'), 
            slug=self.kwargs.get('slug_post')
        )

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['topic'] = self.topic
        return ctx

    def form_valid(self, form):
        post = form.save(commit=False)
        post.message = escape(form.cleaned_data.get('message'))
        post.topic = self.topic
        post.created_by = self.request.user
        post.save()
        
        messages.success(self.request, "Votre réponse vient d'être bien prise en compte.")

        return redirect('forum:show_topic', **{
            'slug': self.kwargs.get('slug'),
            'slug_post': self.kwargs.get('slug_post'), 
            'id_post': self.kwargs.get('id_post')
        })

    def form_invalid(self, form):
        messages.error(self.request, "Une erreur est survenue lors du l'enregistrement de votre réponse")
        return self.render_to_response(self.get_context_data(form=form))
