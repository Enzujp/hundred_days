from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from core.views import index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name="about"),
   
    path('', include("userprofile.urls")),
    path('', include('notepad.urls')),
    path('', include("languages.urls")),
    path('', include("core.urls")),
    
    
    
    path('', index, name="index"),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
