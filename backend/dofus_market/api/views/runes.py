from django.http import JsonResponse
from api.serializers.runes import RuneSerializer
from market.database.rune import Rune
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.db import connection

@api_view(["GET"])
def get_runes(request):
    runes = Rune.objects.all().order_by("name")
    serializer = RuneSerializer(runes, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_rune(request, name):
    try:
        rune = Rune.objects.get(name=name)
    except Rune.DoesNotExist:
        return JsonResponse({'message': 'This Rune does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    data = JSONParser().parse(request)
    rune.prix_ra = data["prix_ra"]
    rune.prix_pa = data["prix_pa"]
    rune.prix_ba = data["prix_ba"]
    rune.save()

    with connection.cursor() as cursor:
        cursor.execute("REFRESH MATERIALIZED VIEW EstimatedGains;")
        cursor.execute("REFRESH MATERIALIZED VIEW Rentability;")
        cursor.execute("REFRESH MATERIALIZED VIEW OrderedByRentability;")

    serializer = RuneSerializer(rune)
    return Response(serializer.data)
