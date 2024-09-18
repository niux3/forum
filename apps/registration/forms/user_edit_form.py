from django import forms
from django.contrib.auth.models import User


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]
    email = forms.CharField(max_length=255, required=True, widget=forms.EmailInput())
