from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title


class Language(models.Model):
    ACTIVE = 'active'
    DELETED = 'deleted'
    PAUSED = 'paused'

    STATUS_CHOICES = (
    (ACTIVE, 'active'),
    (PAUSED, 'paused'),
    (DELETED, 'deleted')
    )

    category = models.ForeignKey(Category, related_name="languages", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, related_name="languages", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads/language_images", blank=True, null=True)
    slug = models.SlugField(max_length=50)
    description_field = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)


    def __str__ (self):
        return self.title

    
class Language_detail(models.Model):
    title = models.CharField(max_length=225)
    created_by = models.ForeignKey(User, related_name="details", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    language = models.ForeignKey(Language, related_name="details", on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
