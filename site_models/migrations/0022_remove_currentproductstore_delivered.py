# Generated by Django 3.0.9 on 2021-01-11 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_models', '0021_order_delivered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentproductstore',
            name='delivered',
        ),
    ]
