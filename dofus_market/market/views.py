from django.shortcuts import render

from django.http import HttpResponse
from .models import DofusObject, IngredientForCraft


def index(request):
    do = DofusObject.objects.get(pk=1)
    print(do.name)
    print(do.level)
    print(do.ingredients)
    print(do.effects)
    print(do.cout_fabrication())
    print(do.gain_estime())

    return HttpResponse("Hello, world. You're at the polls index.")
