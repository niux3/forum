from django import forms
from django.contrib.auth import get_user_model
from registration.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'user', ]

    # birth_date = forms.CharField(widget=forms.DateInput(attrs={
        # 'type': 'date'
    # }))

    newsletter = forms.CharField(widget=forms.CheckboxInput())
    private_message = forms.CharField(widget=forms.CheckboxInput())
    show_email = forms.CharField(widget=forms.CheckboxInput())
