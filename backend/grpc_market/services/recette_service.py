from django_socio_grpc import generics

from grpc_market.serializers.recette_serializer import RecetteProtoSerializer
from market.database.recette import Recette


class RecetteService(generics.AsyncModelService):
    queryset = Recette.objects.all()
    serializer_class = RecetteProtoSerializer
