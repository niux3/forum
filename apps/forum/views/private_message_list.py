from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from forum.models import PrivateMessage


class PrivateMessageList(LoginRequiredMixin, ListView):
    template_name = 'forum/private_message_list.html'
    paginate_by = 30

    def get_queryset(self):
        current_user = get_object_or_404(User, pk=self.request.user.id)
        return PrivateMessage.objects.filter(to_user=current_user).order_by('-created')
