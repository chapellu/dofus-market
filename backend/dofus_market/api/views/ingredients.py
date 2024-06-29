from django.http import JsonResponse
from api.serializers.ingredients import IngredientsSerializer, IngredientSerializer
from market.database.ingredient import Ingredient
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework.request import Request
from django.db import connection

class Ingredients:
    count: int
    results: []

    def __init__(self, count, results):
        self.count = count
        self.results = results


@api_view(['GET'])
def get_ingredients(request: Request):
    page_size: int = request.query_params.get("page_size", 10)
    page: int = request.query_params.get("page", 1)
    query_set = Ingredient.objects.all().order_by("name")
    if "search" in request.query_params:
        query_set = query_set.filter(
            name__icontains=request.query_params["search"])
    paginator = Paginator(query_set, page_size)
    serializer = IngredientsSerializer(
        Ingredients(paginator.count, paginator.page(page)))
    return Response(serializer.data)


@api_view(['PUT'])
def update_ingredient(request, name):
    try:
        ingredient = Ingredient.objects.get(name=name)
    except Ingredient.DoesNotExist:
        return JsonResponse({'message': 'This ingredient does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    data = JSONParser().parse(request)
    ingredient.price = data["price"]
    ingredient.save()
    serializer = IngredientSerializer(ingredient)

    with connection.cursor() as cursor:
        cursor.execute("REFRESH MATERIALIZED VIEW FabricationCosts;")
        cursor.execute("REFRESH MATERIALIZED VIEW Rentability;")
        cursor.execute("REFRESH MATERIALIZED VIEW OrderedByRentability;")


    return Response(serializer.data)
