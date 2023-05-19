from django.urls import path

from . import views

urlpatterns = [
    path('blogs/', views.blogposts, name="blogs"),
    path('<slug:slug>/', views.blog_contents, name="details"),
    # path('blogs/contents/<int:id>/', views.contents, name="contents"),
]