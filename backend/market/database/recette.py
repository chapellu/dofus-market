from django.db import models

from market.database.ingredient import Ingredient
from market.database.ingredient_for_craft import IngredientForCraft
from market.database.metier import Metier


class Recette(models.Model):
    ingredient = models.OneToOneField(
        primary_key=True, to=Ingredient, on_delete=models.CASCADE
    )
    level = models.IntegerField(default=0)
    ingredients = models.ManyToManyField(IngredientForCraft)
    metier = models.ForeignKey(Metier, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return str(self.ingredient)
