# Generated by Django 5.0.1 on 2024-01-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0007_dish_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="dish_images/"),
        ),
    ]
