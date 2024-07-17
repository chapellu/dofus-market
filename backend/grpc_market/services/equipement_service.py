from django.db.models import Prefetch
from django_socio_grpc import generics
from django_socio_grpc.decorators import grpc_action
from google.protobuf.json_format import MessageToDict
from rest_framework.pagination import PageNumberPagination

import grpc_market.grpc.grpc_market_pb2 as pb2
from grpc_market.grpc.grpc_market_p2p import EquipementDetailsRequest
from grpc_market.serializers.equipement_serializer import (
    EquipementDetailsProtoSerializer,
    EquipementProtoSerializer,
)
from market.database.equipement import DofusObject
from market.database.materialized_views.orderered_by_rentability import (
    OrderedByRentability,
)


class EquipementService(generics.AsyncReadOnlyModelService):
    queryset = OrderedByRentability.objects.all()
    serializer_class = EquipementProtoSerializer
    pagination_class = PageNumberPagination

    @grpc_action(
        request=[{"name": "name", "type": "string"}],
        request_name="EquipementDetailsRequest",
        response=[
            {"name": "name", "type": "string"},
            {"name": "level", "type": "int32"},
            {"name": "cout_fabrication", "type": "float"},
            {"name": "gain_estime", "type": "float"},
            {"name": "rentabilite", "type": "float"},
            {"name": "nb_objet", "type": "int32"},
            {"name": "metier", "type": "string"},
            {
                "name": "effects",
                "type": "Caracteristique",
                "cardinality": "repeated",
            },
            {
                "name": "ingredients",
                "type": "Ingredient",
                "cardinality": "repeated",
            },
            {"name": "brisage", "type": "BrisageRune"},
        ],
        response_name="EquipementDetailsResponse",
    )
    async def Details(
        self, grpc_request: pb2.EquipementDetailsRequest, context
    ) -> pb2.EquipementDetailsResponse:
        request = EquipementDetailsRequest(
            **MessageToDict(grpc_request, preserving_proto_field_name=True)
        )
        equipement = await OrderedByRentability.objects.prefetch_related(
            Prefetch(
                "name",
                to_attr="dofus_object",
                queryset=DofusObject.objects.prefetch_related(
                    "_effects", "_ingredients"
                ),
            )
        ).aget(name=request.name)
        serializer = EquipementDetailsProtoSerializer(equipement)
        data = await serializer.amessage
        return data
