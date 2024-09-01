from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from boards.models import Board, Post
from boards.forms import TopicForm


class TopicCreate(LoginRequiredMixin, CreateView):
    template_name = 'boards/create.html'
    form_class = TopicForm

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.board = get_object_or_404(
            Board,
            pk=self.kwargs.get('id'), 
            slug=self.kwargs.get('slug')
        )

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['board'] = self.board
        return ctx

    def form_valid(self, form):
        user = self.request.user
        topic = form.save(commit=False)
        topic.slug = slugify(form.cleaned_data.get('subject'))
        topic.board = self.board
        topic.starter = user
        topic.save()

        post = Post.objects.create(
            message=form.cleaned_data.get('message'),
            topic=topic,
            created_by=user
        )
        
        messages.success(self.request, "Votre sujet vient d'être bien pris en compte.")

        return redirect('boards:topics', **{
            'slug': self.kwargs.get('slug'),
            'id': self.kwargs.get('id')
        })

    def form_invalid(self, form):
        messages.error(self.request, "Une erreur est survenue lors du l'enregistrement de votre sujet")
        return self.render_to_response(self.get_context_data(form=form))
