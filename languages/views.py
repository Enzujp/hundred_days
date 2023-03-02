from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .models import Language, Category
from django.db.models import Q

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

def search(request):
    query = request.GET.get('query', '')
    languages = Language.objects.filter(status=Language.ACTIVE).filter(Q(title__icontains=query) | Q(description_field__icontains=query))
    return render(request, 'languages/search.html', {
        'languages': languages,
        'query': query
    })


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

def language_detail(request, category_slug, slug):
    language = get_object_or_404(Language, slug=slug, status=Language.ACTIVE)

    return render(request, 'languages/language_detail.html', {
        'language': language
    })