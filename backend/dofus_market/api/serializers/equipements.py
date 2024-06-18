import time
from rest_framework import serializers

from market.database.equipement import DofusObject

from .caracteristique import CaracteristiqueSerializer
from .ingredients_for_craft import IngredientForCraftSerializer


class EquipementSerializer(serializers.Serializer):
    name = serializers.CharField()
    level = serializers.IntegerField()

    cout_fabrication = serializers.SerializerMethodField(
        'serialize_cout_fabrication')
    gain_estime = serializers.SerializerMethodField('serialize_gain_estime')
    rentabilite = serializers.SerializerMethodField('serialize_rentabilite')
    # brisage = serializers.SerializerMethodField('serialize_brisage')
    nb_objet = serializers.SerializerMethodField('serialize_nb_objet')
    metier = serializers.CharField()

    def serialize_cout_fabrication(self, dofus_object: DofusObject):
        return dofus_object.cout_fabrication()

    def serialize_gain_estime(self, dofus_object: DofusObject):
        return dofus_object.gain_estime()

    def serialize_rentabilite(self, dofus_object: DofusObject):
        return int(dofus_object.rentabilite())

    def serialize_brisage(self, dofus_object: DofusObject):
        return dofus_object.brisage()

    def serialize_nb_objet(self, dofus_object: DofusObject):
        return dofus_object.nombre_ingredients


class EquipementDetailsSerializer(EquipementSerializer):
    effects = serializers.SerializerMethodField('serialize_effects')
    ingredients = serializers.SerializerMethodField('serialize_ingredients')

    def serialize_effects(self, dofus_object: DofusObject):
        return CaracteristiqueSerializer(dofus_object.effects, many=True).data

    def serialize_ingredients(self, dofus_object: DofusObject):
        return IngredientForCraftSerializer(dofus_object.ingredients,
                                            many=True).data
