# Generated by Django 5.0.1 on 2024-01-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Contact",
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="time",
        ),
        migrations.AddField(
            model_name="reservation",
            name="email",
            field=models.EmailField(blank=True, default="", max_length=254),
        ),
    ]
