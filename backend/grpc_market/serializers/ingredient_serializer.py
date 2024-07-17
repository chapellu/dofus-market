from django_socio_grpc import proto_serializers

from grpc_market.grpc.grpc_market_pb2 import IngredientListResponse, IngredientResponse
from market.database.ingredient import Ingredient


class IngredientProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"
        proto_class = IngredientResponse
        proto_class_list = IngredientListResponse
