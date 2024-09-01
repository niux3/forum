from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect
from django.contrib import messages


class CustomPasswordChangeView(PasswordChangeView):
    success_url = 'forum:index'

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        messages.success(self.request, "Votre mot de passe vient d'être modifié")
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, "Une erreur est survenue lors de la modification de votre mot de passe")
        return self.render_to_response(self.get_context_data(form=form))

