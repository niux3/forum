from django.views.generic import ListView
from boards.models import Board


class BoardList(ListView):
    template_name = 'boards/home.html'
    model = Board
