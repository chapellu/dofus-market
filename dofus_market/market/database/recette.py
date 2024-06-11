from django.db import models

from .ingredient import Ingredient
from .metier import Metier
from .ingredient_for_craft import IngredientForCraft


class Recette(models.Model):
    ingredient = models.OneToOneField(primary_key=True,
                                      to=Ingredient,
                                      on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    ingredients = models.ManyToManyField(IngredientForCraft)
    metier = models.ForeignKey(Metier, on_delete=models.CASCADE)
