# Generated by Django 4.1.5 on 2023-01-25 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0003_rename_image_language_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
