from django.http import JsonResponse
from api.serializers.ingredients import IngredientSerializer
from market.database.ingredient import Ingredient
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


@api_view(['GET'])
def get_ingredients(request):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
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
    return Response(serializer.data)
