# Generated by Django 4.1.3 on 2023-02-12 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='picture',
            new_name='main_picture',
        ),
    ]
