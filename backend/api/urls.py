from django.urls import path

from api.views.caracteristiques import get_caracteristique
from api.views.equipements import get_equipements, get_equipements_details
from api.views.generate_database import generate_data_base, generate_data_base_post
from api.views.ingredients import get_ingredients, update_ingredient
from api.views.metiers import get_metiers
from api.views.runes import get_runes, update_rune

urlpatterns = [
    path("importDofusbookEquipement", generate_data_base_post),
    path("importData", generate_data_base),
    path("equipements", get_equipements),
    path("equipements/<str:name>", get_equipements_details),
    path("caracteristiques", get_caracteristique),
    path("ingredients", get_ingredients),
    path("ingredients/<str:name>", update_ingredient),
    path("runes", get_runes),
    path("runes/<str:name>", update_rune),
    path("metiers", get_metiers),
]
