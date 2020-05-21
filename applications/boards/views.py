from django.shortcuts import render
from django.http import HttpResponse
from .models import Board


def index(request):
    context = {
        'boards': Board.objects.all()
    }
    return render(request, 'home.html', context)