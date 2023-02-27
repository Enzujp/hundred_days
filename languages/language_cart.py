from django.conf import settings

from .models import Language

class LanguageCart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.LANGUAGE_CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.LANGUAGE_CART_SESSION_ID] = {}
        
        self.cart = cart


    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['language'] = Language.objects.get(pk=p)

        for item in self.cart.values():
            yield item

    def len(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        self.session[settings.LANGUAGE_CART_SESSION_ID] = self.cart