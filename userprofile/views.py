from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth import login
from languages.forms import SignUpForm,LanguageForm
from languages.models import User
from django.contrib.auth.decorators import login_required



@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')


@login_required
def my_languages(request):
    pass

# use my_store function from ecommerce app to tailor this function

@login_required
def my_languages_detail(request):
    pass

# might not be necessary but check against my_store_details to be sure


@login_required

@login_required
def add_language(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify('title')
            product.save()

            messages.success(request, "The product was added!")

            return redirect('my_store')
    else:
        form = LanguageForm()
    form = LanguageForm()
    return render (request, 'userprofile/language_form.html', {
        'form': form,
        'title': 'Add Language'
    })


# above view would be used by user to add language


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            messages.success(request, "Registration was successful!")

            return redirect('index')

    else:
        form = SignUpForm

    return render(request, 'userprofile/signup.html', {
        'form': form
    }
    )
