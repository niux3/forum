from django import forms
from django.contrib.auth import get_user_model
from registration.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'user', ]
