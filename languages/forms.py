from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import LanguageOrder, User, Language


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.TextInput()
    last_name = forms.TextInput()

    class meta:
        model = User
        fields = [ "firstname", "lastname", "username", "email", "password1", "password2", ]

             
        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'lastname': forms.TextInput(attrs={
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
        user.firstname = self.cleaned_data['first_name']
        user.lastname = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class LanguageOrderForm(forms.ModelForm):
    class Meta:
        model = LanguageOrder
        fields = ('first_name', 'last_name', 'title', 'language', 'country',)

    widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'language': forms.Textarea(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'country': forms.FileInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'city': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
        }

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ( 'category', 'title', 'description_field', 'image',)

    widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'description_field': forms.Textarea(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
        }
    