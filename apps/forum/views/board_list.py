from django.views.generic import ListView
from forum.models import Board


class BoardList(ListView):
    template_name = 'forum/home.html'
    model = Board
