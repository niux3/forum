from django import forms
from django.contrib.auth import get_user_model
from forum.models import PrivateMessage


class PrivateMessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMessage
        exclude = [
            'from_user',
            'to_user',
            'created',
            'updated'
        ]
