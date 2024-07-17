from django_socio_grpc import proto_serializers

from grpc_market.grpc.grpc_market_pb2 import RuneListResponse, RuneResponse
from market.database.rune import Rune


class RuneProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Rune
        fields = "__all__"
        proto_class = RuneResponse
        proto_class_list = RuneListResponse
