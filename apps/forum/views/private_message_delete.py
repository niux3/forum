from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from forum.models import PrivateMessage


class PrivateMessageDelete(LoginRequiredMixin, DeleteView):
    model = PrivateMessage

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs) # no template confirm

    def post(self, request, *args, **kwargs):
        count_message = PrivateMessage.objects.filter(to_user=request.user.id).count()
        url = 'forum:private_message_list' if count_message > 1 else 'forum:index'
        self.success_url = reverse_lazy(url)
        messages.success(self.request, "Votre message a bien été supprimé")
        return self.delete(request, *args, **kwargs)
