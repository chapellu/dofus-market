from django.db import models

from market.database.equipement import DofusObject


class FabricationCosts(models.Model):
    equipement = models.ForeignKey(
        DofusObject, on_delete=models.DO_NOTHING, db_column="name", to_field="name"
    )
    fabrication_cost = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False  # Important: Django will not attempt to create/update/delete the table
        db_table = "FabricationCosts"

    def __str__(self):
        return f"{self.equipement} - {self.fabrication_cost}"