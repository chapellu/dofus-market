import time

from api.serializers.equipements import (EquipementDetailsSerializer,
                                         EquipementsSerializer)
from django.core.paginator import Paginator
from django.db.models import QuerySet
from market.database.equipement import DofusObject
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.utils.serializer_helpers import ReturnDict


class Equipements:
    count: int
    results: []

    def __init__(self, count, results):
        self.count = count
        self.results = results


@api_view(['GET'])
def get_equipements(request: Request):
    page_size: int = request.query_params.get("page_size", 10)
    page: int = request.query_params.get("page", 1)
    query = """
        WITH EstimatedGains AS (
          SELECT
            e.name,
            SUM(c.number_of_ra * r.prix_ra + c.number_of_pa * r.prix_pa + c.number_of_ba * r.prix_ba) AS estimated_gain
          FROM market_dofusobject e
          JOIN market_dofusobject__effects ef ON e.name = ef.dofusobject_id
          JOIN market_caracteristique c ON c.id = ef.caracteristique_id
          JOIN market_rune r on r.name = c.rune_id
          WHERE
            CASE WHEN %(metier)s IS NULL THEN TRUE ELSE e.metier_id = %(metier)s END
          GROUP BY e.name
        )
        SELECT
          e.name,
          COALESCE(eg.estimated_gain, 0) AS equipement_estimated_gain
        FROM market_dofusobject e
        LEFT JOIN EstimatedGains eg ON e.name = eg.name
        WHERE 
            CASE WHEN %(metier)s IS NULL THEN TRUE ELSE e.metier_id = %(metier)s END
            AND %(equipment_name)s IS NULL OR e.name LIKE %(equipment_name)s
        ORDER BY equipement_estimated_gain DESC;
        """
    query_set = DofusObject.objects.raw(
        query, {
            "metier":
            request.query_params.get("metier", None),
            "equipment_name":
            f"%{request.query_params['search']}%"
            if "search" in request.query_params else None
        })
    paginator = Paginator(query_set, page_size)
    serializer: Serializer = EquipementsSerializer(
        Equipements(paginator.count, paginator.page(page)))
    data: ReturnDict = serializer.data
    return Response(data)


@api_view(['GET'])
def get_equipements_details(request: Request, name: str):
    query_set: QuerySet = DofusObject.objects.get(name=name)
    serializer: Serializer = EquipementDetailsSerializer(query_set)
    data: ReturnDict = serializer.data
    return Response(data)
