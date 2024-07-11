from django_socio_grpc import generics

from grpc_market.serializers.ingredient_serializer import IngredientProtoSerializer
from market.database.ingredient import Ingredient


class IngredientService(generics.AsyncModelService):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientProtoSerializer
