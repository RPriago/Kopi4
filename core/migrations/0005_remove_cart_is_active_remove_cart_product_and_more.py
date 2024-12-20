# Generated by Django 5.0.7 on 2024-11-14 07:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_cart_is_active"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="product",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="quantity",
        ),
        migrations.RemoveField(
            model_name="cartitem",
            name="is_active",
        ),
        migrations.AlterField(
            model_name="cart",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
