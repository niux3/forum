from django import forms
from django.contrib.auth import get_user_model
from registration.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    user = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.HiddenInput,
        disabled=True
    )
