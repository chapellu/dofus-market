from django.db import models

from market.database.equipement import DofusObject


class Rentability(models.Model):
    equipement = models.ForeignKey(
        DofusObject, on_delete=models.DO_NOTHING, db_column="name", to_field="name"
    )
    equipement_estimated_gain = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    equipement_fabrication_cost = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    rentability = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False  # Important: Django will not attempt to create/update/delete the table
        db_table = "Rentability"

    def __str__(self) -> str:
        return f"{self.name} - Rentability: {self.rentability}%"
