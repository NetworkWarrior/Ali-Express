# Generated by Django 4.1.3 on 2023-03-09 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0032_alter_localproduct_email_alter_productpicture_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpicture',
            name='local_product',
        ),
        migrations.RemoveField(
            model_name='productpicture',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='local',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.company'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.DeleteModel(
            name='LocalProduct',
        ),
    ]
