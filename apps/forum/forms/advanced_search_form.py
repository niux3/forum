from django import forms
from django.contrib.auth.models import User
from forum.models import Board


class AdvancedSeachForm(forms.Form):
    boards = forms.ModelChoiceField(label='catégories', queryset=Board.objects.all(), required=False)
    # search_in = forms.MultipleChoiceField(label='Rechercher dans', choices=(
        # ('', 'choisir une option'),
        # ('topics', 'sujets'),
        # ('topics_posts', 'sujets et réponses')
    # ), widget=forms.Select(attrs={'class': 'form-check-input'}), required=False, initial=0)
    users = forms.ModelChoiceField(label="membres", queryset=User.objects.all(), required=False)
