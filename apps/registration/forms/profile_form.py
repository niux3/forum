import re
from django import forms
from django.contrib.auth import get_user_model
from registration.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'user', ]

    birth_date = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'dd/mm/yyyy',
        'value': '11/11/1'
    }))

    newsletter = forms.CharField(widget=forms.CheckboxInput())
    private_message = forms.CharField(widget=forms.CheckboxInput())
    show_email = forms.CharField(widget=forms.CheckboxInput())

    def clean_birth_date(self):
        birth_date_value = self.cleaned_data['birth_date']
        date_pattern = re.compile(r'^\d{2}\/\d{2}\/\d{4}$')
        print('-> ', birth_date_value)
        print('=> ', date_pattern.search(birth_date_value))
        if date_pattern.search(birth_date_value) is None:
            raise forms.ValidationError("la date d'anniversaire n'est pas correcte (dd/mm/yyyy)")

        return birth_date_value
