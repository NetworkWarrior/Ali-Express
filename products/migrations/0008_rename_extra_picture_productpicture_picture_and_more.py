# Generated by Django 4.1.3 on 2023-02-12 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_productpictures_productpicture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productpicture',
            old_name='extra_picture',
            new_name='picture',
        ),
        migrations.RemoveField(
            model_name='product',
            name='main_picture',
        ),
    ]