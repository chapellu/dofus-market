import time
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
    t1 = time.process_time()
    print("Enter GET")
    dofus_objects = DofusObject.objects.all().prefetch_related(
        "_effects", "_ingredients", "metier")
    t2 = time.process_time()
    print("GET Done", t2 - t1)
    t3 = time.process_time()
    print("Enter Serializer")
    serializer = DofusObjectSerializer(dofus_objects, many=True)
    data = serializer.data
    t4 = time.process_time()
    print("Serializer Done", t4 - t3)
    print("Total request time", t4 - t1)
    return Response(data)


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
    ingredient.price = data["price"]
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


@api_view(["GET"])
def getRunes(request):
    runes = Rune.objects.all()
    serializer = RuneSerializer(runes, many=True)
    return Response(serializer.data)
