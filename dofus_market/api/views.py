from rest_framework.response import Response
from rest_framework.decorators import api_view
from market.models import DofusObject, Caracteristique, Rune
from .serializers import DofusObjectSerializer, CaracteristiqueSerializer, RuneSerializer


@api_view(['GET'])
def getDofusObject(request):
    dofus_objects = DofusObject.objects.all()
    serializer = DofusObjectSerializer(dofus_objects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRune(request):
    dofus_objects = Rune.objects.all()
    serializer = RuneSerializer(dofus_objects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCaracteristique(request):
    dofus_objects = Caracteristique.objects.all()
    serializer = CaracteristiqueSerializer(dofus_objects, many=True)
    return Response(serializer.data)
