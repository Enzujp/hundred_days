# Generated by Django 4.1.5 on 2023-05-12 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0022_blog_user_alter_blog_language_alter_blog_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='language',
        ),
    ]
