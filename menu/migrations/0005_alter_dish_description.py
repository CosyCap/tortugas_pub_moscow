# Generated by Django 5.0.1 on 2024-01-29 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0004_alter_dish_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="description",
            field=models.TextField(max_length=255),
        ),
    ]
