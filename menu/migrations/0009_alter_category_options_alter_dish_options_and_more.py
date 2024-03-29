# Generated by Django 5.0.1 on 2024-02-01 07:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0008_alter_dish_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("name",),
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterModelOptions(
            name="dish",
            options={"verbose_name": "Блюдо", "verbose_name_plural": "Блюда"},
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Название категории"),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(verbose_name="Это поле автоматически заполняется"),
        ),
        migrations.AlterField(
            model_name="dish",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dishes",
                to="menu.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="dish",
            name="description",
            field=models.TextField(max_length=255, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="dish",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="dish_images/",
                verbose_name="Изображение",
            ),
        ),
        migrations.AlterField(
            model_name="dish",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="dish",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Цена"
            ),
        ),
    ]
