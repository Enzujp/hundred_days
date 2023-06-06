from django.shortcuts import render, redirect

from django.http import HttpResponse

from languages.models import Language

# Create your views here.


def index(request):
    languages = Language.objects.filter(status=Language.ACTIVE)[0:]
    return render(request, 'core/index.html', {
            'languages' : languages
        })

  

def about(request):
    return render(request, 'core/about.html')


