from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('forum:index')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "votre compte utilisateur a bien été modifié")
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, "Une erreur est survenue lors de votre modification")
        return self.render_to_response(self.get_context_data(form=form))
