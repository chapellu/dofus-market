from django.urls import path
from . import views

urlpatterns = [
    path('', views.getDofusObject),
    path('caracteristiques', views.getCaracteristique),
    path('rune', views.getRune),
    path('createDofusbookObject', views.createDofusbookObject),
    path('ingredients', views.getIngredients),
    path('ingredients/<str:name>', views.updateIngredient),
    path('runes', views.getRunes),
]
