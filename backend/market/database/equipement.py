from typing import Any, Iterable

from django.db import models

from market.database.caracteristique import Caracteristique
from market.database.ingredient import Ingredient
from market.database.ingredient_for_craft import IngredientForCraft
from market.database.metier import Metier
from market.database.rune import Rune

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
    "tr": "Façonneur",
}

ABSOLUTLY_NOT_PROFITABLE = 10**12
HDV_TAXE = 1.03


class DofusObject(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    level = models.IntegerField()
    metier = models.ForeignKey(Metier, on_delete=models.CASCADE)
    _effects = models.ManyToManyField(Caracteristique)
    _ingredients = models.ManyToManyField(IngredientForCraft)

    def __str__(self) -> str:
        return self.name

    def cout_fabrication(self) -> int:
        return int(self.equipement_fabrication_cost)

    def gain_estime(self) -> int:
        return int(self.equipement_estimated_gain)

    def rentabilite(self) -> float:
        return self.rentability

    def brisage(self) -> list:
        res = []
        for caracteristique in self.effects:
            ra, pa, ba = caracteristique.brisage(self.level)
            rune = Rune.objects.get(name=caracteristique.rune.name)
            res.append(
                {
                    "rune": caracteristique.rune.name,
                    "quantity_ra": ra,
                    "prix_ra": rune.prix_ra,
                    "quantity_pa": pa,
                    "prix_pa": rune.prix_pa,
                    "quantity_ba": ba,
                    "prix_ba": rune.prix_ba,
                }
            )
        return res

    @classmethod
    def create_from_dofusbook_object(cls, dofusbook_object: Any) -> "DofusObject":
        print(dofusbook_object["id"])
        if dofusbook_object["category_name"] in [
            "tr",
            "do",
            "mt",
            "fa",
            "mo",
        ]:  # Ignore trophée, dofus, montilier, familier, monture
            return
        try:
            dofus_object = DofusObject.objects.get(name=dofusbook_object["name"])
        except DofusObject.DoesNotExist:
            metier, _ = Metier.objects.get_or_create(
                name=metier_name[dofusbook_object["category_name"]]
            )
            dofus_object = cls(
                name=dofusbook_object["name"],
                level=dofusbook_object["level"],
                metier=metier,
            )
            dofus_object.save()

            caracteristiques = [
                Caracteristique.create_from_dofusbook(
                    caracteristique, dofusbook_object["level"]
                )
                for caracteristique in dofusbook_object["effects"]
                if Caracteristique.create_from_dofusbook(
                    caracteristique, dofusbook_object["level"]
                )
                is not None
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
    def nombre_ingredients(self) -> int:
        return len(self.ingredients)

    @property
    def effects(self) -> Iterable[Caracteristique]:
        return self._effects.all()

    @property
    def ingredients(self) -> Iterable[Ingredient]:
        return IngredientForCraft.objects.all().filter(dofusobject=self.pk)
