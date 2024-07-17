from django_socio_grpc import proto_serializers

from market.database.ingredient_for_craft import IngredientForCraft
from grpc_market.grpc.grpc_market_pb2 import IngredientForCraftResponse, IngredientForCraftListResponse


class IngredientForCraftProtoSerializer(proto_serializers.ModelProtoSerializer
                                        ):

    class Meta:
        model = IngredientForCraft
        fields = '__all__'
        proto_class = IngredientForCraftResponse
        proto_class_list = IngredientForCraftListResponse
