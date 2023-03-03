from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import LanguageOrder, User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.TextInput()
    last_name = forms.TextInput()

    class meta:
        model = User
        fields = [ "firstname", "lastname", "username", "email", "password1", "password2" ]

             
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
        fields = ('first_name', 'last_name', 'title', 'language', 'country', 'city')


class LanguageForm(forms.ModelForm):
    # please pursue train of thought here when light returns and give an hour to rest framework after
    # creating a new coursera account with the new email
    pass

