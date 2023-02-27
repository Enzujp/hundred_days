from .language_cart import LanguageCart

def cart(request):
    return {'cart': LanguageCart(request)}