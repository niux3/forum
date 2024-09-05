from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from registration.forms import ProfileForm
from registration.models import Profile


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('forum:index')

    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            print('>>', profile_form.cleaned_data)
            user = form.save()
            profile_form.save(commit=False)
            profile_form.user = user
            profile_form.save()

            messages.success(self.request, "votre compte utilisateur a bien été modifié")
            return redirect(self.get_success_url())
        else:
            messages.error(self.request, "Une erreur est survenue lors de votre modification")
            return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['profile_form'] = ProfileForm(instance=self.request.user.profile)
        return ctx
