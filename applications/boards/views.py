from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.utils import timezone
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Board, Topic, Post
from .forms import NewTopicForm, PostForm


def index(request):
    context = {
        'boards': Board.objects.all()
    }
    return render(request, 'boards/home.html', context)


def topics(request, id, slug):
    board = get_object_or_404(Board, pk=id, slug=slug)
    topics = board.topics.order_by('-updated').annotate(replies=Count('posts') - 1)
    page = request.GET.get('page', 1)
    paginator = Paginator(topics, 10)

    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)

    context = {
        'board': board,
        'topics': topics
    }
    return render(request, 'boards/topics.html', context)


@login_required
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


def show_topic(request, slug, id, slug_post, id_post):
    topic = get_object_or_404(Topic, board__pk=id,board__slug=slug, pk=id_post, slug=slug_post)
    topic.views += 1
    topic.save()
    return render(request, 'boards/show_post.html', {'topic': topic})


@login_required
def reply_topic(request, slug, id, slug_post, id_post):
    topic = get_object_or_404(Topic, board__pk=id,board__slug=slug, pk=id_post, slug=slug_post)
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.topic = topic
        post.created_by = request.user
        post.save()
        return redirect('boards:show_topic', slug=slug, id=id, slug_post=slug_post, id_post=id_post)
    context = {
        'topic': topic,
        'form': form
    }
    return render(request, 'boards/reply_topic.html', context)


@login_required
def edit_post(request, slug, id, slug_post, id_post, id_message):
    post = get_object_or_404(Post, pk=id_message)
    topic = get_object_or_404(Topic, board__pk=id, board__slug=slug, pk=id_post, slug=slug_post)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        row = form.save(commit=False)
        row.created_by = request.user
        row.topic = topic
        row.updated = timezone.now()
        row.save()
        return redirect('boards:show_topic', slug=slug, id=id, slug_post=slug_post, id_post=id_post)
    context = {
        'form': form,
        'topic': topic
    }
    return render(request, 'boards/reply_topic.html', context)