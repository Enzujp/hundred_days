from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name="cart"),
    path('add_to_cart/<int:language_id>', views.add_to_cart, name="add_to_cart"),
    path('change_quantity/<int:language_id>', views.change_quantity, name="change_quantity"),
    path('remove_from_cart/<int:language_id>', views.remove_from_cart, name="remove_from_cart"),
]