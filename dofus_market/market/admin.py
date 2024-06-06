from django.contrib import admin

from .models import Rune, Caracteristique, DofusObject, Ingredient, IngredientForCraft

admin.site.register(Caracteristique)
admin.site.register(Rune)
admin.site.register(DofusObject)
admin.site.register(Ingredient)
admin.site.register(IngredientForCraft)
