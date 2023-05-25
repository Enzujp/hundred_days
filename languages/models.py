from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File



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
    (DELETED, 'deleted'),
    )

    category = models.ForeignKey(Category, related_name="languages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="languages", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads/language_images", blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/language_images/thumbnails', blank=True, null=True)
    slug = models.SlugField(max_length=50)
    description_field = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)


    def __str__ (self):
        return self.title
    
def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        thumb_io = BytesIO()
        if img.mode in ("RGBA", "P"):
            img = img.convert('RGB')
        img.thumbnail(size)
    
        
        img.save(thumb_io, 'JPEG', quality=85)
        name = image.name.replace('uploads/languages_images/', '')
        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'





    
class LanguageOrder(models.Model):
    language = models.ForeignKey(Language, related_name="language_order", on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=50, null=False, default="")
    created_by = models.ForeignKey(User, related_name="details", on_delete=models.SET_NULL, null=True)
    country = models.CharField(max_length=225, blank=True)
    city = models.CharField(max_length=225, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)



class LanguageOrderItem(models.Model):
    language_order = models.ForeignKey(LanguageOrder, related_name="items", on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name="items", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

