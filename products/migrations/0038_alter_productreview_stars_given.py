# Generated by Django 4.1.3 on 2023-03-24 21:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_alter_companynews_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='stars_given',
            field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
