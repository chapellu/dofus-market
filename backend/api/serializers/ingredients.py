from rest_framework import serializers

from market.database.ingredient import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class IngredientsSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    results = serializers.SerializerMethodField("serialize_equipements")

    def serialize_equipements(self, test):
        return IngredientSerializer(test.results, many=True).data
