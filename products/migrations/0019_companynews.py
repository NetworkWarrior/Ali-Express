# Generated by Django 4.1.3 on 2023-03-04 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_rename_picture_company_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('description', models.TextField()),
                ('video', models.FileField(upload_to='videos/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]