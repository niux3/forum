from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils.text import slugify
from .models import Board, Topic, Post
from .forms import NewTopicForm


def index(request):
    context = {
        'boards': Board.objects.all()
    }
    return render(request, 'boards/home.html', context)


def topics(request, id, slug):
    context = {
        'board': get_object_or_404(Board, pk=id, slug=slug)
    }
    return render(request, 'boards/topics.html', context)


def create(request, id, slug):
    board = get_object_or_404(Board, pk=id, slug=slug)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.slug = slugify(form.cleaned_data.get('subject'))
            topic.board = board
            topic.starter = user
            topic.save()

            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('boards:topics', id=id, slug=slug)
    else:
        form = NewTopicForm()
    context = {
        'board': board,
        'form': form
    }
    return render(request, 'boards/create.html', context)
