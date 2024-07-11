from market.database.materialized_views.orderered_by_rentability import OrderedByRentability
from grpc_market.serializers.equipement_serializer import EquipementProtoSerializer
from django_socio_grpc import generics


class EquipementService(generics.AsyncReadOnlyModelService):
    queryset = OrderedByRentability.objects.all()
    serializer_class = EquipementProtoSerializer
