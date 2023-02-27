from django.shortcuts import render
from .cart import Cart
from languages.models import Language, User

# Create your views here.

def cart_view(request):
    cart = Cart(request)
    
    return render(request, 'languages/cart_view.html', {
        'cart': cart }
        )