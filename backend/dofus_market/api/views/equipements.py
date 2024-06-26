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
    t1: float = time.process_time()
    page_size: int = request.query_params.get("page_size", 10)
    page: int = request.query_params.get("page", 1)
    print("Enter GET")
    query_set: QuerySet = DofusObject.objects.all().prefetch_related(
        "_effects", "_ingredients", "metier").order_by("name")
    if "search" in request.query_params:
        query_set = query_set.filter(
            name__icontains=request.query_params["search"])
    if "metier" in request.query_params:
        query_set = query_set.filter(
            metier__name__icontains=request.query_params["metier"])
    paginator = Paginator(query_set, page_size)
    t2 = time.process_time()
    print("GET Done", t2 - t1)
    t3 = time.process_time()
    print("Enter Serializer")
    serializer: Serializer = EquipementsSerializer(
        Equipements(paginator.count, paginator.page(page)))
    data: ReturnDict = serializer.data
    t4 = time.process_time()
    print("Serializer Done", t4 - t3)
    print("Total request time", t4 - t1)
    return Response(data)


@api_view(['GET'])
def get_equipements_details(request: Request, name: str):
    query_set: QuerySet = DofusObject.objects.get(name=name)
    serializer: Serializer = EquipementDetailsSerializer(query_set)
    data: ReturnDict = serializer.data
    return Response(data)
