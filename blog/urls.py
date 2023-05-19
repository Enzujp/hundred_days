from django.urls import path

from . import views

urlpatterns = [
    path('blog', views.blogpost, name="blog")
]