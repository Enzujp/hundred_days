# Generated by Django 4.1.5 on 2023-05-25 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0037_language_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languageorder',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='languageorder',
            name='last_name',
        ),
        migrations.AddField(
            model_name='languageorder',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]