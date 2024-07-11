from django_socio_grpc import proto_serializers
from rest_framework import serializers
from market.database.materialized_views.orderered_by_rentability import OrderedByRentability

from grpc_market.grpc.grpc_market_pb2 import EquipementResponse, EquipementListResponse


class EquipementProtoSerializer(proto_serializers.ModelProtoSerializer):
    cout_fabrication = serializers.DecimalField(
        max_digits=12, decimal_places=2, source="equipement_fabrication_cost")
    gain_estime = serializers.DecimalField(max_digits=12,
                                           decimal_places=2,
                                           source="equipement_estimated_gain")
    rentabilite = serializers.IntegerField(source="rentability")
    nb_object = serializers.IntegerField(source="number_of_ingredients")

    class Meta:
        model = OrderedByRentability
        fields = ("name", "level", "cout_fabrication", "gain_estime",
                  "rentabilite", "nb_object", "metier")
        proto_class = EquipementResponse
        proto_class_list = EquipementListResponse
