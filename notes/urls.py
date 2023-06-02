from django.urls import path

from . import views

urlpatterns = [
    path('blogs/', views.blogposts, name="blogs"),
    # path('<slug:slug>/', views.blog_contents, name="blog_contents"),
    path('<int:id>/', views.blog_contents, name="blog_contents"),
    path('new_blog/', views.new_blog, name="new_blog"),
    path('blogs/edit-blog/<int:id>/', views.edit_blog, name="edit_blog"),
    path('blogs/delete_blog/<int:id>/', views.delete_blog, name="delete_blog"),
]