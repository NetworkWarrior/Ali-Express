# Generated by Django 4.1.3 on 2023-03-08 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_productpicture_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localproduct',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productpicture',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]