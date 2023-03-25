from django.conf import settings

from .models import Language


# Cart.py holds a class with nested functions that would allow users control over how many languages
# they wish to learn, letting them add, update or remove from a self curated library.

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['language'] = Language.objects.get(pk=p)

        for item in self.cart.values():
            item['total_items'] = int(item['language'])
            yield(item)

    def len(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, language_id, quantity=1, update_quantity=False):
        language_id = str(language_id)

        if language_id not in self.cart:
            self.cart[language_id] = {'quantity': int(quantity), 'id': language_id}

        if update_quantity:
            self.cart[language_id]['quantity'] += int(quantity)

            if self.cart[language_id]['quantity'] == 0:
                self.remove(language_id)    

        self.save()


    def remove(self, language_id):
        if language_id in self.cart:
            del self.cart[(language_id)]

            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True