# Generated by Django 4.1.3 on 2023-03-08 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_localproduct_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='localproduct',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
    ]
