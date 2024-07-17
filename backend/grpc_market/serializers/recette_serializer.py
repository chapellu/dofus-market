from django_socio_grpc import proto_serializers

from grpc_market.grpc.grpc_market_pb2 import RecetteListResponse, RecetteResponse
from market.database.recette import Recette


class RecetteProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Recette
        fields = "__all__"
        proto_class = RecetteResponse
        proto_class_list = RecetteListResponse
