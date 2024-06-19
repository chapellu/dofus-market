import time

from api.serializers.equipements import EquipementDetailsSerializer, EquipementsSerializer
from market.database.equipement import DofusObject
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator


class Equipements:
    count: int
    results: []

    def __init__(self, count, results):
        self.count = count
        self.results = results


@api_view(['GET'])
def get_equipements(request):
    t1 = time.process_time()
    print(request.query_params)
    page_size = request.query_params.get("page_size", 10)
    page = request.query_params.get("page", 1)
    print("Enter GET")
    dofus_objects = DofusObject.objects.all().prefetch_related(
        "_effects", "_ingredients", "metier")
    p = Paginator(dofus_objects, page_size)
    t2 = time.process_time()
    print("GET Done", t2 - t1)
    t3 = time.process_time()
    print("Enter Serializer")
    serializer = EquipementsSerializer(Equipements(p.count, p.page(page)))
    data = serializer.data
    t4 = time.process_time()
    print("Serializer Done", t4 - t3)
    print("Total request time", t4 - t1)
    return Response(data)


@api_view(['GET'])
def get_equipements_details(request, name):
    dofus_objects = DofusObject.objects.get(name=name)
    serializer = EquipementDetailsSerializer(dofus_objects)
    data = serializer.data
    return Response(data)
