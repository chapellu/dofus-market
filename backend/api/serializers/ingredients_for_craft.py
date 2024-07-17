from rest_framework import serializers

from market.database.ingredient_for_craft import IngredientForCraft
from market.database.recette import Recette


class IngredientForCraftSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField("serialize_ingredient_for_craft")
    quantity = serializers.IntegerField()
    price = serializers.SerializerMethodField("serialize_ingredient_price_for_craft")
    ingredients = serializers.SerializerMethodField("serialize_ingredients")
    nb_objet = serializers.SerializerMethodField("serialize_nb_objet")
    cout_fabrication = serializers.SerializerMethodField("serialize_cout_fabrication")

    rentabilite = serializers.SerializerMethodField("serialize_rentabilite")

    def serialize_ingredient_for_craft(self, ingredient_for_craft: IngredientForCraft):
        return ingredient_for_craft.ingredient.name

    def serialize_ingredient_price_for_craft(
        self, ingredient_for_craft: IngredientForCraft
    ):
        return ingredient_for_craft.ingredient.price

    def serialize_ingredients(self, ingredient_for_craft: IngredientForCraft):
        try:
            recette = Recette.objects.get(pk=ingredient_for_craft.ingredient.pk)
        except Recette.DoesNotExist:
            return []
        return IngredientForCraftSerializer(recette.ingredients, many=True).data

    def serialize_nb_objet(self, ingredient_for_craft: IngredientForCraft):
        try:
            recette = Recette.objects.get(pk=ingredient_for_craft.ingredient.pk)
        except Recette.DoesNotExist:
            return 0
        return len(recette.ingredients.all())

    def serialize_cout_fabrication(self, ingredient_for_craft: IngredientForCraft):
        try:
            recette = Recette.objects.get(pk=ingredient_for_craft.ingredient.pk)
        except Recette.DoesNotExist:
            return 0
        return int(
            sum(
                [
                    ingredient.ingredient.price * ingredient.quantity
                    for ingredient in recette.ingredients.all()
                ]
            )
        )

    def serialize_rentabilite(self, ingredient_for_craft: IngredientForCraft):
        # rentabilite = recette / cout * 100
        cout_fabrication = self.serialize_cout_fabrication(ingredient_for_craft)
        if cout_fabrication == 0:
            return 0
        else:
            return (
                (ingredient_for_craft.ingredient.price - cout_fabrication)
                / ingredient_for_craft.ingredient.price
                * 100
            )
