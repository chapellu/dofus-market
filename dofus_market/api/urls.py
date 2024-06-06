from django.urls import path
from . import views

urlpatterns = [
    path('', views.getDofusObject),
    path('caracteristiques', views.getCaracteristique),
    path('rune', views.getRune)
]
