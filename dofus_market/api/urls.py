from django.urls import path
from .views.equipements import get_dofus_object
from .views.caracteristiques import get_caracteristique
from .views.runes import get_runes, update_rune
from .views.ingredients import get_ingredients, update_ingredient
from .views.import_dofusbook_data import import_dofusbook_equipement

urlpatterns = [
    path('importDofusbookEquipement', import_dofusbook_equipement),
    path('equipements', get_dofus_object),
    path('caracteristiques', get_caracteristique),
    path('ingredients', get_ingredients),
    path('ingredients/<str:name>', update_ingredient),
    path('runes', get_runes),
    path('runes/<str:name>', update_rune),
]
