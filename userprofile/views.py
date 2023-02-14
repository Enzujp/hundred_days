from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from languages.forms import SignUpForm
from languages.models import User
from django.contrib.auth.decorators import login_required


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


@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')