from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Language, User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.TextInput()
    last_name = forms.TextInput()

    class meta:
        model = User
        fields = ( "first_name", "last_name", "username", "email", "password1", "password2")

             
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'last_ name': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'username': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
        }



    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user