from django.urls import path
from . import views

urlpatterns = [
    path('my-notes/', views.my_notes, name="my-notes"),
    path('new-notes/', views.new_notes, name="new-notes"),
    
    path('<slug:slug>/', views.detail, name="note-detail"),
    path('my-posts/<slug:slug>/', views.edit_notes, name="edit-note"),
    path('my-posts/<slug:slug>/', views.delete_notes, name="delete-note"),
    
]