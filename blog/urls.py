from django.urls import path

from . import views

urlpatterns = [
    path('blogs/', views.blogposts, name="blogs"),
    # path('<slug:slug>/', views.blog_contents, name="blog_contents"),
    path('blogs/<int:id>', views.blog_contents, name="blog_contents"),
]