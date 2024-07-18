from django.db import models

from market.database.ingredient import Ingredient


class IngredientForCraft(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = (
            "ingredient",
            "quantity",
        )  # Ensuring uniqueness for the combination of ingredient and quantity

    def __str__(self) -> str:
        return f'{{name: "{self.ingredient}", quantity: {self.quantity}}}'

    @classmethod
    def create_from_dofusbook(cls, dofusbook_ingredient) -> int:
        ig, _ = Ingredient.objects.get_or_create(name=dofusbook_ingredient["name"])
        ingredient, _ = cls.objects.get_or_create(
            ingredient=ig, quantity=dofusbook_ingredient["count"]
        )
        return ingredient.pk
