from django.contrib import admin

from .models import Category, Language, LanguageOrder, LanguageOrderItem, Blog
# Register your models here.

admin.site.register(Category)

admin.site.register(Language)

admin.site.register(LanguageOrder)

admin.site.register(LanguageOrderItem)

admin.site.register(Blog)