# Generated by Django 4.1.3 on 2023-02-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_extra_picture_productpicture_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='europe_delivery',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='product',
            name='europe_out_delivery',
            field=models.IntegerField(default=12),
        ),
    ]
