from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .models import Language, Category

# Create your views here.


def cart_view(request):
    cart = Cart(request)
    
    return render(request, 'languages/cart_view.html', {
        'cart': cart }
        )

def add_to_cart(request, language_id):
    cart = Cart(request)
    cart.add(language_id)

    return redirect('cart_view')

def change_quantity(request, language_id):
    action = request.GET.get('action', '')
    
    if action:
        quantity = 1

        if action == 'decrease':
            quantity = -1

        cart = Cart(request)
        cart.add(language_id, quantity, True)

        return redirect('cart_view')
    
def remove_from_cart(request, language_id):
    cart = Cart(request)
    cart.remove(language_id)

    return redirect('cart_view')

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    languages = Category.languages.all()

    return render(request, 'languages/category_detail.html', {
        'category': category,
        'languages': languages
    })