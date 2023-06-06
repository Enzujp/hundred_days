from django.urls import path
from . import views

urlpatterns = [
    path('my-notes/', views.my_notes, name="my-notes"),
    path('<slug:slug>/', views.detail, name="note-detail"),
    path('new-notes/', views.new_notes, name="new-notes"),
    path('my-notes/edit-note/<slug:slug>/', views.edit_note, name="edit-note"),
    path('delete-note/<slug:slug>/', views.delete_note, name="delete-note"),
    
]