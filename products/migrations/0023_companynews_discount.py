# Generated by Django 4.1.3 on 2023-03-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_companynews_deleted_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='companynews',
            name='discount',
            field=models.IntegerField(blank=True, default=10),
        ),
    ]
