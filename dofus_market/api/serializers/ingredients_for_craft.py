from rest_framework import serializers

from market.database.ingredient_for_craft import IngredientForCraft


class IngredientForCraftSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField('serialize_ingredient_for_craft')
    quantity = serializers.IntegerField()

    def serialize_ingredient_for_craft(
            self, ingredient_for_craft: IngredientForCraft):
        return ingredient_for_craft.ingredient.name
