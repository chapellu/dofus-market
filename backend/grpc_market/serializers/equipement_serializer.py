from typing import Any

from django_socio_grpc import proto_serializers
from rest_framework import serializers
from rest_framework.serializers import ReturnDict, ReturnList

from grpc_market.grpc.grpc_market_pb2 import (
    EquipementDetailsResponse,
    EquipementListResponse,
    EquipementResponse,
)
from grpc_market.serializers.rune_serializer import RuneProtoSerializer
from market.database.caracteristique import Caracteristique
from market.database.ingredient_for_craft import IngredientForCraft
from market.database.materialized_views.orderered_by_rentability import (
    OrderedByRentability,
)
from market.database.recette import Recette


class EquipementProtoSerializer(proto_serializers.ModelProtoSerializer):
    cout_fabrication = serializers.FloatField(source="equipement_fabrication_cost")
    gain_estime = serializers.FloatField(source="equipement_estimated_gain")
    rentabilite = serializers.IntegerField(source="rentability")
    nb_objet = serializers.IntegerField(source="number_of_ingredients")

    class Meta:
        model = OrderedByRentability
        fields = (
            "name",
            "level",
            "cout_fabrication",
            "gain_estime",
            "rentabilite",
            "nb_objet",
            "metier",
        )
        proto_class = EquipementResponse
        proto_class_list = EquipementListResponse


class EquipementDetailsProtoSerializer(EquipementProtoSerializer):
    effects = serializers.SerializerMethodField("serialize_effects")
    ingredients = serializers.SerializerMethodField("serialize_ingredients")
    brisage = serializers.SerializerMethodField("serialize_brisage")

    class Meta:
        model = OrderedByRentability
        fields = (
            "name",
            "level",
            "cout_fabrication",
            "gain_estime",
            "rentabilite",
            "nb_objet",
            "metier",
            "effects",
            "ingredients",
            "brisage",
        )
        proto_class = EquipementDetailsResponse

    def serialize_effects(
        self, ordered_by_rentability: OrderedByRentability
    ) -> ReturnList | Any | ReturnDict:
        return CaracteristiqueProtoSerializer(
            ordered_by_rentability.name._effects, many=True
        ).data

    def serialize_ingredients(
        self, ordered_by_rentability: OrderedByRentability
    ) -> ReturnList | Any | ReturnDict:
        return IngredientforCraftProtoSerializer(
            ordered_by_rentability.name._ingredients, many=True
        ).data

    def serialize_brisage(self, ordered_by_rentability: OrderedByRentability) -> list:
        return ordered_by_rentability.name.brisage()


class CaracteristiqueProtoSerializer(proto_serializers.ProtoSerializer):
    name = serializers.CharField()
    min = serializers.IntegerField()
    max = serializers.IntegerField()
    rune = serializers.SerializerMethodField("serialize_rune")

    def serialize_rune(
        self, caracteristique: Caracteristique
    ) -> ReturnList | Any | ReturnDict:
        return RuneProtoSerializer(caracteristique.rune).data


class IngredientforCraftProtoSerializer(proto_serializers.ProtoSerializer):
    name = serializers.SerializerMethodField("serialize_ingredient_for_craft")
    quantity = serializers.IntegerField()
    price = serializers.SerializerMethodField("serialize_ingredient_price_for_craft")
    ingredients = serializers.SerializerMethodField("serialize_ingredients")
    nb_objet = serializers.SerializerMethodField("serialize_nb_objet")
    cout_fabrication = serializers.SerializerMethodField("serialize_cout_fabrication")
    rentabilite = serializers.SerializerMethodField("serialize_rentabilite")

    def serialize_ingredient_for_craft(
        self, ingredient_for_craft: IngredientForCraft
    ) -> str:
        return ingredient_for_craft.ingredient.name

    def serialize_ingredient_price_for_craft(
        self, ingredient_for_craft: IngredientForCraft
    ) -> int:
        return ingredient_for_craft.ingredient.price

    def serialize_ingredients(
        self, ingredient_for_craft: IngredientForCraft
    ) -> ReturnList | Any | ReturnDict:
        try:
            recette = Recette.objects.get(pk=ingredient_for_craft.ingredient.pk)
        except Recette.DoesNotExist:
            return []
        return IngredientforCraftProtoSerializer(recette.ingredients, many=True).data

    def serialize_nb_objet(self, ingredient_for_craft: IngredientForCraft) -> int:
        try:
            recette = Recette.objects.get(pk=ingredient_for_craft.ingredient.pk)
        except Recette.DoesNotExist:
            return 0
        return len(recette.ingredients.all())

    def serialize_cout_fabrication(
        self, ingredient_for_craft: IngredientForCraft
    ) -> int:
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

    def serialize_rentabilite(self, ingredient_for_craft: IngredientForCraft) -> float:
        cout_fabrication = self.serialize_cout_fabrication(ingredient_for_craft)
        if cout_fabrication == 0:
            return 0.0
        else:
            return (
                (ingredient_for_craft.ingredient.price - cout_fabrication)
                / ingredient_for_craft.ingredient.price
                * 100
            )
