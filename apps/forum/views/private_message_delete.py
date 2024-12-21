from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from forum.models import PrivateMessage


class PrivateMessageDelete(LoginRequiredMixin, DeleteView):
    model = PrivateMessage
    success_url = reverse_lazy('forum:private_message_list')

    def get(self, request, *args, **kwargs):
        messages.success(self.request, "Votre message a bien été supprimé")
        return self.delete(request, *args, **kwargs)
