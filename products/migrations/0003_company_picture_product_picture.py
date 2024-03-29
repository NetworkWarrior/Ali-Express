# Generated by Django 4.1.3 on 2023-02-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_review_alter_product_category_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='picture',
            field=models.ImageField(default='default_company_pic.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='default_product_picture.jpg', upload_to=''),
        ),
    ]
