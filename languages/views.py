from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .models import Language, Category, LanguageOrderItem
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import LanguageOrderForm


# something in the cart configuration requires a fix, and I'm working on it

def add_to_cart(request, language_id):
    cart = Cart(request)
    cart.add(language_id)

    return redirect('cart')


def change_quantity(request, language_id):
    action = request.GET.get('action', '')

    if action:
        quantity = 1

        if action == 'decrease':
            quantity = -1

        cart = Cart(request)
        cart.add(language_id, quantity, True)

    return redirect('cart')

def remove_from_cart(request, language_id):
    cart = Cart(request)
    cart.remove(language_id)

    return redirect('cart')


def cart_view(request):
    cart = Cart(request)
    
    return render(request, 'languages/cart_view.html', {
        'cart': cart 
        })


def search(request):
    query = request.GET.get('query', '')
    languages = Language.objects.filter(status=Language.ACTIVE).filter(Q(title__icontains=query) | Q(description_field__icontains=query))
    return render(request, 'languages/search.html', {
        'languages': languages,
        'query': query
    })

@login_required
def language_cart_checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = LanguageOrderForm(request.POST)

        if form.is_valid():
            for item in cart:
                language = item['language']
                # total_price += product.price * int(item['quantity'])

            order = form.save(commit=False)
            order.created_by = request.user
            order.save()

            for item in cart:
                language = item['language']
                quantity = int(item['quantity'])
                item = LanguageOrderItem.objects.create(order=order, language=language, quantity=quantity)
            
            cart.clear()

            return redirect('my')
    else:
        form = LanguageOrderForm()
    return render(request, 'languages/checkout.html', {
        'cart': cart,
        'form': form
    })



def language_detail(request, category_slug, slug):
    language = get_object_or_404(Language, slug=slug, status=Language.ACTIVE)

    return render(request, 'languages/language_detail.html', {
        'language': language
    })



# def category_detail(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     languages = Category.languages.all()

#     return render(request, 'languages/category_detail.html', {
#         'category': category,
#         'languages': languages
#     })