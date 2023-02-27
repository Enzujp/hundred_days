from django.shortcuts import render
from .language_cart import LanguageCart
from languages.models import Language, User

# Create your views here.

def cart_view(request):
    cart = LanguageCart(request)
    
    return render(request, 'languages/language_cart_view.html', {
        'cart': cart
    })