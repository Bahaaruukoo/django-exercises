from django import forms
from appTwo.models import users

class NewUserForm(forms.ModelForm):
    class Meta:
        model = users
        fields = '__all__'
