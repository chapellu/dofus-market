from django_socio_grpc import generics

from grpc_market.serializers.metier_serializer import MetierProtoSerializer
from market.database.metier import Metier


class MetierService(generics.AsyncModelService):
    queryset = Metier.objects.all()
    serializer_class = MetierProtoSerializer
