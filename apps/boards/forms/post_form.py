from django import forms
from boards.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'message',
        ]
