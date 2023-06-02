from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.mynotes, name="mynotes"),
    # path('<slug:slug>/', views.blog_contents, name="blog_contents"),
    path('<slug:slug>/', views.note_contents, name="blog-contents"),
    path('new-note/', views.new_note, name="new-note"),
    path('notes/edit-note/<slug:slug>/', views.edit_blog, name="edit-note"),
    path('blogs/delete_note/<slug:slug>/', views.delete_blog, name="delete-note"),
]