from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from forum.forms.private_message_form import PrivateMessageForm
from forum.models.private_message import PrivateMessage


class PrivateMessageEdit(LoginRequiredMixin, CreateView):
    template_name = 'forum/private_message_edit.html'
    form_class = PrivateMessageForm

    def form_valid(self, form):
        to_user = get_object_or_404(User, pk=self.kwargs.get('id'))
        mp = form.save(commit=False)
        mp.from_user = self.request.user
        mp.to_user = to_user
        mp.save()

        messages.success(self.request, "Votre sujet vient d'être bien pris en compte.")
        return redirect('forum:index')

    def form_invalid(self, form):
        messages.error(self.request, "Une erreur est survenue lors du l'enregistrement de votre message privé")
        return self.render_to_response(self.get_context_data(form=form))
