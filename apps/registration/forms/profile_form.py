import re
import datetime
from django import forms
from django.contrib.auth import get_user_model
from registration.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'user', ]

    birth_date = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'dd/mm/yyyy',
    }))

    newsletter = forms.CharField(widget=forms.CheckboxInput())
    private_message = forms.CharField(widget=forms.CheckboxInput())
    show_email = forms.CharField(widget=forms.CheckboxInput())

    def clean_birth_date(self):
        birth_date_value = self.cleaned_data['birth_date']
        date_pattern = re.compile(r'^(?P<day>\d{2})\/(?P<month>\d{2})\/(?P<year>\d{4})$')
        msg = "la date d'anniversaire n'est pas correcte (dd/mm/yyyy)"
        def validate_date(values, msg):
            d, m, y = values
            try:
                datetime.date.fromisoformat(f'{y}-{m}-{d}')
            except ValueError:
                raise forms.ValidationError(msg)

        if birth_date_value != '':
            if date_pattern.search(birth_date_value) is None:
                raise forms.ValidationError(msg)
            validate_date(date_pattern.findall(birth_date_value).pop(), msg)
        return birth_date_value
