from rest_framework import serializers

from market.models import DofusObject, Caracteristique, Ingredient, Rune


class DofusObjectSerializer(serializers.Serializer):
    name = serializers.CharField()
    level = serializers.IntegerField()
    effects = serializers.SerializerMethodField('serialize_effects')
    ingredients = serializers.SerializerMethodField('serialize_ingredients')
    cout_fabrication = serializers.SerializerMethodField(
        'serialize_cout_fabrication')
    gain_estime = serializers.SerializerMethodField('serialize_gain_estime')
    rentabilite = serializers.SerializerMethodField('serialize_rentabilite')
    brisage = serializers.SerializerMethodField('serialize_brisage')
    nb_objet = serializers.SerializerMethodField('serialize_nb_objet')
    metier = serializers.CharField()

    def serialize_effects(self, dofus_object):
        return CaracteristiqueSerializer(dofus_object.effects, many=True).data

    def serialize_ingredients(self, dofus_object):
        return IngredientForCraftSerializer(dofus_object.ingredients,
                                            many=True).data

    def serialize_cout_fabrication(self, dofus_object):
        return dofus_object.cout_fabrication()

    def serialize_gain_estime(self, dofus_object):
        return dofus_object.gain_estime()

    def serialize_rentabilite(self, dofus_object):
        return int(dofus_object.rentabilite())

    def serialize_brisage(self, dofus_object):
        return dofus_object.brisage()

    def serialize_nb_objet(self, dofus_object):
        return dofus_object.nombre_ingredients


class IngredientForCraftSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField('serialize_ingredient_for_craft')
    quantity = serializers.IntegerField()

    def serialize_ingredient_for_craft(self, ingredient_for_craft):
        return ingredient_for_craft.ingredient.name


class RuneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rune
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'


class CaracteristiqueSerializer(serializers.Serializer):

    name = serializers.CharField()
    min = serializers.IntegerField()
    max = serializers.IntegerField()
    rune = serializers.SerializerMethodField('serialize_rune')

    def serialize_rune(self, foo):
        return RuneSerializer(foo.rune).data
