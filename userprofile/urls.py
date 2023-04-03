from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from. import views

urlpatterns = [
    path('signup/', views.signup, name="signup" ),
    path('signin/', auth_views.LoginView.as_view(template_name='userprofile/signin.html'), name="signin"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('my-languages/blog/', views.blog, name="blog"),
    path('my-languages/', views.my_languages, name="my_languages"),
    path('my-languages/add-language/', views.add_language, name="add-language"),
    path('my-languages/edit-language/<int:pk>/', views.edit_language, name="edit-language"),
    path('my-languages/delete-language/<int:pk>/', views.delete_language, name="delete-language"),
    
]