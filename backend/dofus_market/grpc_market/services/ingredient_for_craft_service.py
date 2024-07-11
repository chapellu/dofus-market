from django_socio_grpc import generics

from grpc_market.serializers.ingredient_for_craft_serializer import IngredientForCraftProtoSerializer
from market.database.ingredient_for_craft import IngredientForCraft


class IngredientForCraftService(generics.AsyncModelService):
    queryset = IngredientForCraft.objects.all()
    serializer_class = IngredientForCraftProtoSerializer
