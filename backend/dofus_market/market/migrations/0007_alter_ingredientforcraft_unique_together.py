# Generated by Django 5.0.6 on 2024-07-11 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20240711_0957'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ingredientforcraft',
            unique_together={('ingredient', 'quantity')},
        ),
    ]
