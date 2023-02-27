from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from languages.forms import SignUpForm
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

def add_language(request):
    pass

# use add_product function from ecommerce app to tailor this too.


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
