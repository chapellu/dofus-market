from django_socio_grpc import proto_serializers

from market.database.metier import Metier
from grpc_market.grpc.grpc_market_pb2 import MetierResponse, MetierListResponse


class MetierProtoSerializer(proto_serializers.ModelProtoSerializer):

    class Meta:
        model = Metier
        fields = '__all__'
        proto_class = MetierResponse
        proto_class_list = MetierListResponse
