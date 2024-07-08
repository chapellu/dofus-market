from django_socio_grpc import generics

from grpc_market.serializers.rune_serializer import RuneProtoSerializer
from market.database.rune import Rune


class RuneService(generics.AsyncModelService):
    queryset = Rune.objects.all()
    serializer_class = RuneProtoSerializer
