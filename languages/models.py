from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File

# Create your models here.


class Language(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50 )

    class Meta:
        verbose_name_plural = 'Languages'
    def __str__(self):
        return self.title