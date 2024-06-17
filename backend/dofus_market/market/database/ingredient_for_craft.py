from django.db import models

from .ingredient import Ingredient


class IngredientForCraft(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return f"{{name: \"{self.ingredient}\", quantity: {self.quantity}}}"

    @classmethod
    def create_from_dofusbook(cls, dofusbook_ingredient):
        ig, _ = Ingredient.objects.get_or_create(
            name=dofusbook_ingredient["name"])
        ingredient, _ = cls.objects.get_or_create(
            ingredient=ig, quantity=dofusbook_ingredient["count"])
        return ingredient.pk
