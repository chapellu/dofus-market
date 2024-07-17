from django_socio_grpc import proto_serializers

from market.database.recette import Recette
from grpc_market.grpc.grpc_market_pb2 import RecetteResponse, RecetteListResponse


class RecetteProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Recette
        fields = "__all__"
        proto_class = RecetteResponse
        proto_class_list = RecetteListResponse
