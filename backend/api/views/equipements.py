from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.utils.serializer_helpers import ReturnDict

from api.serializers.equipements import (
    EquipementDetailsSerializer,
    EquipementsSerializer,
)
from market.database.equipement import DofusObject


class Equipements:
    count: int
    results: []

    def __init__(self, count, results):
        self.count = count
        self.results = results


@api_view(["GET"])
def get_equipements(request: Request) -> Response:
    page_size: int = request.query_params.get("page_size", 10)
    page: int = request.query_params.get("page", 1)
    query = """
      SELECT
        e.name,
        e.metier_id,
        e.equipement_estimated_gain,
        e.equipement_fabrication_cost,
        e.rentability
      FROM OrderedByRentability e
        WHERE
          e.rentability IS NOT NULL
          AND CASE WHEN %(metier)s IS NULL THEN TRUE ELSE e.metier_id = %(metier)s END
          AND CASE WHEN %(equipment_name)s IS NULL THEN TRUE ELSE LOWER(e.name) LIKE LOWER(%(equipment_name)s) END;
        """

    query_set = DofusObject.objects.raw(
        query,
        {
            "metier": request.query_params.get("metier", None),
            "equipment_name": f"%{request.query_params['search']}%"
            if "search" in request.query_params
            else None,
        },
    )
    paginator = Paginator(query_set, page_size)
    serializer: Serializer = EquipementsSerializer(
        Equipements(paginator.count, paginator.page(page))
    )
    data: ReturnDict = serializer.data
    return Response(data)


@api_view(["GET"])
def get_equipements_details(request: Request, name: str) -> Response:
    query = """
      SELECT
        e.name,
        e.equipement_estimated_gain,
        e.equipement_fabrication_cost,
        e.rentability
      FROM Rentability e
        WHERE e.name = %s
    """

    query_set = DofusObject.objects.raw(query, [name])[0]
    serializer: Serializer = EquipementDetailsSerializer(query_set)
    data: ReturnDict = serializer.data
    return Response(data)
