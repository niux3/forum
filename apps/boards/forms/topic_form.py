from django import forms
from boards.models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'subject',
            'message',
        ]
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
        }
    message = forms.CharField(max_length=4000, widget=forms.Textarea(), help_text="la longueur max. est de 4000 caractères")


