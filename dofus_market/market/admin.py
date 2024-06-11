from django.contrib import admin

from .database.caracteristique import Caracteristique
from .database.equipement import DofusObject
from .database.ingredient import Ingredient
from .database.ingredient_for_craft import IngredientForCraft
from .database.metier import Metier
from .database.rune import Rune

admin.site.register(Caracteristique)
admin.site.register(Rune)
admin.site.register(DofusObject)
admin.site.register(Ingredient)
admin.site.register(IngredientForCraft)
admin.site.register(Metier)
