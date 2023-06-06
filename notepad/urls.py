from django.urls import path
from . import views

urlpatterns = [
    path('my-notes/<slug:slug>/', views.detail, name="note-detail"),
 
    path('my-notes/', views.my_notes, name="my-notes"),
    path('new-notes/', views.new_notes, name="new-notes"),
    path('my-notes/edit-note/<slug:slug>/', views.edit_note, name="edit-note"),
    path('my-notes/delete-note/<slug:slug>/', views.delete_notes, name="delete-note"),
    
]