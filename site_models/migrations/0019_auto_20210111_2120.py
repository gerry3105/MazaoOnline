# Generated by Django 3.0.9 on 2021-01-11 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_models', '0018_currentproductstore_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentproductstore',
            name='product',
        ),
        migrations.AddField(
            model_name='currentproductstore',
            name='ordered_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='site_models.OrderProduct'),
        ),
    ]