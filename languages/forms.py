from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import LanguageOrder, User, Language
from notes.models import Post

# class SignupForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     first_name = forms.TextInput()
#     last_name = forms.TextInput()

#     class Meta:
#         model = User
#         fields = ( "first_name", "last_name", "username", "email", "password1", "password2")


        
#         widgets = {
#             'first_name': forms.TextInput(attrs={
#                 'class': 'w-full p-4 border border-gray-200'
#             }),
#             'last_ name': forms.TextInput(attrs={
#                 'class': 'w-full p-4 border border-gray-200'
#             }),
#             'username': forms.TextInput(attrs={
#                 'class': 'w-full p-4 border border-gray-200'
#             }),
#             'password1': forms.PasswordInput(attrs={
#                 'class': 'w-full p-4 border border-gray-200'
#             }),
#             'password2': forms.PasswordInput(attrs={
#                 'class': 'w-full p-4 border border-gray-200'
#             }),
#         }



#     def save(self, commit=True):
#         user = super(SignupForm, self).save(commit=False)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = [ "first_name", "last_name", "username", "email", "password1", "password2"]


        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200',
                'style': "max-width: 300px",
                'placeholder': "first name"
            }),

            'last_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'placeholder': "last name"
            }),

            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'placeholder': "email"
            }),

           'username': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'placeholder': "username"
            }),

            'password1': forms.PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                
                
            }),
        }

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class LanguageOrderForm(forms.ModelForm):
    class Meta:
        model = LanguageOrder
        fields = ('username', 'country', 'city',)

    widgets = {
            'username': forms.TextInput(attrs={
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


class NotesForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('day', 'slug', 'title', 'content',)

    widgets = {
            'day': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
    }