from typing import Iterable
from django.db import models

from .caracteristique import Caracteristique
from .ingredient_for_craft import IngredientForCraft
from .ingredient import Ingredient
from .metier import Metier

metier_name = {
    "bo": "Cordonnier",
    "ce": "Cordonnier",
    "sa": "Cordonnier",
    "pe": "Forgeur de Pelles",
    "an": "Bijoutier",
    "am": "Bijoutier",
    "ep": "Forgeur d'Epées",
    "da": "Forgeur de Dagues",
    "ha": "Forgeur de Haches",
    "ar": "Sculteur d'Arcs",
    "ba": "Sculteur de Baguettes",
    "bm": "Sculteur de Baton",
    "ch": "Coiffeur",
    "ca": "Cape",
    "br": "Façonneur",
    "tr": "Façonneur"
}


class DofusObject(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    level = models.IntegerField()
    metier = models.ForeignKey(Metier, on_delete=models.CASCADE)
    _effects = models.ManyToManyField(Caracteristique)
    _ingredients = models.ManyToManyField(IngredientForCraft)

    def __str__(self) -> str:
        return self.name

    def cout_fabrication(self) -> int:
        return int(
            sum([
                ingredient.ingredient.price * ingredient.quantity
                for ingredient in self.ingredients
            ]))

    def gain_estime(self) -> int:
        return int(
            sum([
                caracteristique.gain_estime(self.level)
                for caracteristique in self.effects
            ]))

    def rentabilite(self) -> float:
        try:
            return ((self.gain_estime() - self.cout_fabrication()) /
                    self.cout_fabrication()) * 100
        except ZeroDivisionError:
            return -1000.0

    def brisage(self):
        res = []
        for caracteristique in self.effects:
            res.append(
                (caracteristique.name, *caracteristique.brisage(self.level)))
        return res

    @classmethod
    def create_from_dofusbook_object(cls, dofusbook_object):
        print(dofusbook_object["id"])
        if dofusbook_object["category_name"] in [
                "tr", "do", "mt", "fa", "mo"
        ]:  #Ignore trophée, dofus, montilier, familier, monture
            return
        try:
            dofus_object = DofusObject.objects.get(
                name=dofusbook_object["name"])
        except DofusObject.DoesNotExist:
            metier, _ = Metier.objects.get_or_create(
                name=metier_name[dofusbook_object["category_name"]])
            dofus_object = cls(name=dofusbook_object["name"],
                               level=dofusbook_object["level"],
                               metier=metier)
            dofus_object.save()

            caracteristiques = [
                Caracteristique.create_from_dofusbook(
                    caracteristique, dofusbook_object["level"])
                for caracteristique in dofusbook_object["effects"]
            ]

            dofus_object._effects.add(*caracteristiques)

            ingredients = [
                IngredientForCraft.create_from_dofusbook(ingredient)
                for ingredient in dofusbook_object["ingredients"]
            ]

            dofus_object._ingredients.add(*ingredients)

            dofus_object.save()

        return dofus_object

    @property
    def nombre_ingredients(self):
        return len(self.ingredients)

    @property
    def effects(self) -> Iterable[Caracteristique]:
        return self._effects.all()

    @property
    def ingredients(self) -> Iterable[Ingredient]:
        return IngredientForCraft.objects.all().filter(dofusobject=self.pk)
