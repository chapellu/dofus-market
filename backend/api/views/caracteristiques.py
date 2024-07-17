from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.serializers.caracteristique import CaracteristiqueSerializer
from market.database.caracteristique import Caracteristique


@api_view(["GET"])
def get_caracteristique(request):
    dofus_objects = Caracteristique.objects.all()
    serializer = CaracteristiqueSerializer(dofus_objects, many=True)
    return Response(serializer.data)
