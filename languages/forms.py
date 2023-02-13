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
