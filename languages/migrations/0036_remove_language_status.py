# Generated by Django 4.1.5 on 2023-05-24 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0035_delete_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='status',
        ),
    ]
