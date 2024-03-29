# Generated by Django 4.1.5 on 2023-03-23 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('languages', '0012_remove_languageorder_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languageorderitem',
            name='price',
        ),
        migrations.AlterField(
            model_name='language',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='languages.category'),
        ),
        migrations.AlterField(
            model_name='language',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to=settings.AUTH_USER_MODEL),
        ),
    ]
