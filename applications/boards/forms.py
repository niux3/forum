from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(max_length=4000, widget=forms.Textarea(attrs={'class': 'form-control'}),help_text="la longueur max. est de 4000 caractères")
    class Meta:
        model = Topic
        fields = [
            'subject',
            'message',
        ]
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
        }
