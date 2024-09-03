from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from forum.models import Board, Post
from forum.forms import TopicForm


class TopicCreate(LoginRequiredMixin, CreateView):
    template_name = 'forum/create.html'
    form_class = TopicForm

    def form_valid(self, form):
        user = self.request.user
        topic = form.save(commit=False)
        topic.slug = slugify(form.cleaned_data.get('subject'))
        topic.board = form.cleaned_data.get('forum')
        topic.starter = user
        topic.save()

        post = Post.objects.create(
            message=form.cleaned_data.get('message'),
            topic=topic,
            created_by=user
        )
        
        messages.success(self.request, "Votre sujet vient d'être bien pris en compte.")
        return redirect('forum:show_topic', **{
            'slug': form.cleaned_data.get('forum').slug,
            'id': form.cleaned_data.get('forum').id,
            'id_post': topic.id,
            'slug_post': topic.slug
        })

    def form_invalid(self, form):
        messages.error(self.request, "Une erreur est survenue lors du l'enregistrement de votre sujet")
        return self.render_to_response(self.get_context_data(form=form))
