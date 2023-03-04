from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}


#context-processor ensures that cart is available globally
