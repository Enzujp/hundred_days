# Generated by Django 4.1.5 on 2023-03-04 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0010_language_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='quantity',
        ),
    ]
