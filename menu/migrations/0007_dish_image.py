# Generated by Django 5.0.1 on 2024-01-29 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0006_alter_category_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="dish",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="goods_images"),
        ),
    ]