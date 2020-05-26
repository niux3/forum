from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView


def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('boards:index')
    context = {
        'form': form
    }
    return render(request, 'account/signup.html', context)


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'account/profile.html'
    success_url = reverse_lazy('boards:index')

    def get_object(self):
        return self.request.user

