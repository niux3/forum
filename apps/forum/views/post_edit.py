from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.utils.html import escape
from forum.models import Topic, Post
from forum.forms import PostForm


class PostEdit(LoginRequiredMixin, UpdateView):
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

    def get_object(self, queryset=None):
        return get_object_or_404(
            Post, 
            pk=self.kwargs.get('id_message')
        )

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['topic'] = self.topic
        return ctx

    def form_valid(self, form):
        row = form.save(commit=False)
        row.message = escape(form.cleaned_data.get('message'))
        row.created_by = self.request.user
        row.topic = self.topic
        row.save()

        messages.success(self.request, "Votre post a bien été modifié")
        return redirect(
            'forum:show_topic', 
            slug=self.kwargs.get('slug'), 
            slug_post=self.kwargs.get('slug_post'), 
            id_post=self.kwargs.get('id_post')
        )
 
    def form_invalid(self, form):
        messages.error(self.request, "Une erreur est survenue lors du l'enregistrement de votre modification")
        return self.render_to_response(self.get_context_data(form=form))
