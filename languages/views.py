from django.shortcuts import render
from .cart import LanguageCart
from languages.models import Language, User

# Create your views here.

def cart_view(request):
    cart = LanguageCart(request)
    
    return render(request, 'languages/cart_view.html', {
        'cart': cart
    })