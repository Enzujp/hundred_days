from .cart import LanguageCart

def cart(request):
    return {'cart': LanguageCart(request)}


#context-processor ensures that cart is available globally
