from django.contrib import admin

from .models import Rune, Caracteristique, DofusObject, Ingredient, IngredientForCraft, Metier

admin.site.register(Caracteristique)
admin.site.register(Rune)
admin.site.register(DofusObject)
admin.site.register(Ingredient)
admin.site.register(IngredientForCraft)
admin.site.register(Metier)
