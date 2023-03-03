from django.urls import path
from . import views

urlpatterns = [
    path('login_index/', views.login_index, name="login_index")
]