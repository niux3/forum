from django import forms


class SeachForm(forms.Form):
    q = forms.CharField(label="terme recherché", widget=forms.TextInput(attrs={
        'class': 'form-control'
    }), required=True)
