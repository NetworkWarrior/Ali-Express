# Generated by Django 4.1.3 on 2023-02-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(default='default_profile_pic.jpg', upload_to=''),
        ),
    ]