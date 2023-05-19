from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Blog(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'
    DELETED = 'deleted'

    STATUS_CHOICES = (
        (ACTIVE, 'active'),
        (DRAFT, 'draft'),
        (DELETED, 'deleted')
    )


    author = models.ForeignKey(User, related_name="blog_posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=80, )
    content = models.CharField(max_length=900)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    day = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)
    slug = models.SlugField(max_length=50, default="", null=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title