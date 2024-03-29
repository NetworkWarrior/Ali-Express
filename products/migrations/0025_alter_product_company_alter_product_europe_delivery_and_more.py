# Generated by Django 4.1.3 on 2023-03-08 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_product_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.company'),
        ),
        migrations.AlterField(
            model_name='product',
            name='europe_delivery',
            field=models.IntegerField(blank=True, default=7),
        ),
        migrations.AlterField(
            model_name='product',
            name='europe_out_delivery',
            field=models.IntegerField(blank=True, default=12),
        ),
        migrations.AlterField(
            model_name='product',
            name='sold_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
