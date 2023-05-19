from django.urls import path

from . import views

urlpatterns = [
    path('blogs/', views.blogposts, name="blogs"),
    # path('<slug:slug>/', views.blog_contents, name="blog_contents"),
    path('blogs/<int:id>', views.blog_contents, name="blog_contents"),
    path('blogs/new_blog/', views.new_blog, name="new_blog"),
    path('blogs/<int:id>/edit-blog/', views.edit_blog, name="edit_blog"),
    path('blogs/<int:id>/delete_blog/', views.delete_blog, name="delete_blog"),
]