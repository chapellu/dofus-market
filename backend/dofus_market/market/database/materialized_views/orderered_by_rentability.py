from django.db import models

from market.database.equipement import DofusObject
from market.database.metier import Metier


class OrderedByRentability(models.Model):
    name = models.ForeignKey(DofusObject,
                             on_delete=models.DO_NOTHING,
                             db_column='name',
                             to_field='name',
                             primary_key=True)
    metier = models.ForeignKey(Metier,
                               on_delete=models.DO_NOTHING,
                               db_column='metier_id')
    level = models.IntegerField()
    number_of_ingredients = models.IntegerField()
    equipement_estimated_gain = models.DecimalField(max_digits=12,
                                                    decimal_places=2)
    equipement_fabrication_cost = models.DecimalField(max_digits=12,
                                                      decimal_places=2)
    rentability = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False  # This model will not be managed by Django
        db_table = 'orderedbyrentability'  # Ensure this matches the actual materialized view name in the database

    def __str__(self):
        return f"{self.equipement} (Metier: {self.metier}) - Rentability: {self.rentability}%"
