# Generated by Django 4.1.5 on 2023-03-04 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0008_languageorder_languageorderitem_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='languageorderitem',
            old_name='product',
            new_name='language',
        ),
    ]
