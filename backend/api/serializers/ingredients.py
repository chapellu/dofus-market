from typing import Any

from rest_framework import serializers
from rest_framework.serializers import ReturnDict, ReturnList

from api.views.ingredients import Ingredients
from market.database.ingredient import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class IngredientsSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    results = serializers.SerializerMethodField("serialize_equipements")

    def serialize_equipements(
        self, equipments: Ingredients
    ) -> ReturnList | Any | ReturnDict:
        return IngredientSerializer(equipments.results, many=True).data
