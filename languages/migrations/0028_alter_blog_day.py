# Generated by Django 4.1.5 on 2023-05-15 16:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0027_delete_blogcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='day',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
