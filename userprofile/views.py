from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth import login
from languages.forms import SignUpForm,LanguageForm
from languages.models import Language, LanguageOrderItem
from django.contrib.auth.decorators import login_required



@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')


@login_required
def my_languages(request):
    language = request.user.languages.exclude(status=Language.DELETED)
    language_orders = LanguageOrderItem.objects.filter(language__user=request.user)
    return render(request, 'userprofile/my_languages', {
        'language': language,
        'order_items': language_orders
    })

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
            language = form.save(commit=False)
            language.user = request.user
            language.slug = slugify('title')
            language.save()

            messages.success(request, "The product was added!")

            return redirect('my_store')
    else:
        form = LanguageForm()
    form = LanguageForm()
    return render (request, 'userprofile/language_form.html', {
        'form': form,
        'title': 'Add Language'
    })


def edit_language(request, pk):
    language = Language.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = LanguageForm(request.POST, request.FILES, instance=language)

        if form.is_valid:
            form.save()
            messages.success(request, 'Your changes have been made successfully!')
            return redirect('my_languages')

# above view would be used by user to add language

def delete_language(request, pk):
    language = Language.objects.filter(user=request.user).get(pk=pk)
    language.status = language.DELETED
    language.save()
    messages.success(request, 'This language has been successfully deleted!')
    return redirect('my_languages')

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
