# Generated by Django 4.1.2 on 2022-11-19 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='category',
        ),
    ]
