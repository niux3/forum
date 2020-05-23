from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignupForm


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
