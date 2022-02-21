from django import forms
from django.core import validators

#custom validation
def check_for_Z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("NAME NEED TO START WITH 'Z'")

class FormName(forms.Form):
    name = forms.CharField()
    email= forms.EmailField()
    verify_email= forms.EmailField(label='Retype email')
    text = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("EMAILS MUST MUTCH")
