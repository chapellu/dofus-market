# Generated by Django 5.0.6 on 2024-06-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0003_recette_metier"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="price",
            field=models.BigIntegerField(default=1000000000),
        ),
    ]