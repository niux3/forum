from django import forms
from forum.models import Topic, Board


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'forum',
            'subject',
            'message',
        ]
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
        }

    forum = forms.ModelChoiceField(queryset=Board.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    message = forms.CharField(max_length=4000, widget=forms.Textarea(attrs={
        'class': 'form-control'
    }), help_text="la longueur max. est de 4000 caractères")
