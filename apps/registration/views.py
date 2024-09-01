from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib import messages
from registration.forms import SignupForm


class Signup(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Vous êtes connecté !")
        return redirect('boards:index')

    def form_invalid(self, form):
        messages.error(self.request, "Une erreur est survenue lors de la tentative d'inscription")
        return self.render_to_response(self.get_context_data(form=form))
