from django.contrib import admin

from .models import Category, Language, LanguageOrder, LanguageOrderItem
# Register your models here.

admin.site.register(Category)

admin.site.register(Language)

admin.site.register(LanguageOrder)

admin.site.register(LanguageOrderItem)