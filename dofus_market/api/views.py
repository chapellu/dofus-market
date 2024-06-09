from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from market.models import DofusObject, Caracteristique, Ingredient, Rune
from .serializers import DofusObjectSerializer, CaracteristiqueSerializer, IngredientSerializer, RuneSerializer
import json
import requests
import asyncio
import aiohttp
import itertools


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


@api_view(['GET'])
def getIngredients(request):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def updateIngredient(request, name):
    try:
        ingredient = Ingredient.objects.get(name=name)
    except Ingredient.DoesNotExist:
        return JsonResponse({'message': 'This ingredient does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    data = JSONParser().parse(request)
    ingredient.prix = data["prix"]
    ingredient.save()
    serializer = IngredientSerializer(ingredient)
    return Response(serializer.data)


@api_view(['POST'])
def createDofusbookObject(request):
    req = requests.get(
        'https://touch.dofusbook.net/items/touch/search/equipment?page=1')
    first_page = json.loads(req.text)
    page_count = first_page["pages"]

    items = first_page["data"]
    for item in items:
        DofusObject.create_from_dofusbook_object(item)

    for i in range(2, page_count + 1):
        response = requests.get(
            f'https://touch.dofusbook.net/items/touch/search/equipment?page={i}'
        )
        page = json.loads(response.text)
        for item in page["data"]:
            DofusObject.create_from_dofusbook_object(item)

    return Response("ok")
