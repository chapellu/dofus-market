# Generated by Django 5.0.6 on 2024-06-14 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0002_recette"),
    ]

    operations = [
        migrations.AddField(
            model_name="recette",
            name="metier",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="market.metier",
            ),
        ),
    ]
