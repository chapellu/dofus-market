from typing import Iterable
from django.db import models
from .runes import brisage_rune

runes_price = {
    "Age": 12,
    "Cha": 9,
    "de chasse": 394,
    "Fo": 12,
    "Ine": 22,
    "Ini": 159,
    "Prospe": 1977,
    "Ré Air": 193,
    "Ré Eau": 19,
    "Ré Feu": 19,
    "Ré Neutre": 79,
    "Ré Per air": 166,
    "Ré Per Eau": 157,
    "Ré Per Feu": 932,
    "Ré Per Neutre": 498,
    "Ré Per Terre": 898,
    "Ré Terre": 390,
    "Sa": 16,
    "Vi": 45,
    "Cri": 99,
    "Do": 452,
    "Do Air": 374,
    "Do Cri": 792,
    "Do Eau": 189,
    "Do Feu": 203,
    "Do Neutre": 284,
    "Do Pou": 252,
    "Do Terre": 157,
    "Rui": 49,
    "Invo": 7556,
    "Pa Age": 88,
    "Pa Cha": 76,
    "Pa Do Air": 7575,
    "Pa Do Cri": 3631,
    "Pa Do Eau": 5749,
    "Pa Do Feu": 4967,
    "Pa Do Neutre": 896,
    "Pa Do Pou": 3902,
    "Pa Do Terre": 2723,
    "Pa Fo": 108,
    "Pa Fui": 184,
    "Pa Ine": 121,
    "Pa Ini": 2160,
    "Pa Prospe": 8889,
    "Pa Ré Cri": 15956,
    "Pa Ré Pa": 26939,
    "Pa Ré Pme": 12077,
    "Pa Ré Pou": 4563,
    "Pa Ret Pa": 2267,
    "Pa Ret Pme": 833,
    "Pa Sa": 180,
    "Pa Tac": 1116,
    "Pa Vi": 777,
    "Po": 9911,
    "Pod": 28,
    "Pui": 96,
    "Ré Cri": 1404,
    "Ré Pa": 14894,
    "Ré Pme": 2304,
    "Ré Pou": 1962,
    "Ret Pa": 842,
    "Ret Pme": 202,
    "So": 188,
    "Tac": 144,
    "Pa Pod": 224,
    "Pa Pui": 1007,
    "Ra Age": 669,
    "Ra Cha": 625,
    "Ra Fo": 958,
    "Ra Ine": 1104,
    "Ra Ini": 8810,
    "Ra Pod": 1190,
    "Ra Pui": 7415,
    "Ra Sa": 823,
    "Ra Vi": 8552,
    "Pa Ré Air": 240,
    "Pa Ré Eau": 185,
    "Pa Ré Feu": 142,
    "Pa Ré Neutre": 1742,
    "Pa Ré Terre": 3200,
    "Ga Pa": 106910,
    "Ga Pme": 104554,
    "Pa So": 400
}

# class Caracteristique(models.Model):
#     name = models.CharField(max_length=200)
#     jet_min = models.IntegerField()
#     jet_max = models.IntegerField()

#     def __str__(self):
#         return self.name

# class Objet(models.Model):
#     id = models.IntegerField(primary_key=True)
#     level = models.IntegerField()
#     caracteristiques = models.ForeignKey(Caracteristique,
#                                          on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.id)


class Rune(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    prix_ra = models.IntegerField(default=0)
    prix_pa = models.IntegerField(default=0)
    prix_ba = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    # def __init__(self, rune_name) -> None:
    #     self.name = rune_name

    # @property
    # def prix_ra(self):
    #     return runes_price.get(f"Ra {self.name}", 0)

    # @prix_ra.setter
    # def prix_ra(self, value):
    #     self._prix_ra = value

    # @property
    # def prix_pa(self):
    #     return runes_price.get(f"Pa {self.name}", 0)

    # @prix_pa.setter
    # def prix_pa(self, value):
    #     self._prix_pa = value

    # @property
    # def prix_ba(self):
    #     return runes_price[self.name]

    # @prix_ba.setter
    # def prix_ba(self, value):
    #     self._prix_ba = value


runes_name = {
    "fo": "Fo",
    "in": "Ine",
    "ch": "Cha",
    "ag": "Age",
    "vi": "Vi",
    "sa": "Sa",
    "ii": "Ini",
    "rt": "Ré Terre",
    "rf": "Ré Feu",
    "ra": "Ré Air",
    "re": "Ré Eau",
    "rn": "Ré Neutre",
    "rtp": "Ré Per Terre",
    "rfp": "Ré Per Feu",
    "rnp": "Ré Per Neutre",
    "rep": "Ré Per Eau",
    "rap": "Ré Per Air",
    "rp": "Ré Pou",
    "rc": "Ré Cri",
    "epa": "Ré Pa",
    "epm": "Ré Pme",
    "pp": "Prospe",
    "fu": "Fui",
    "po": "Po",
    "so": "So",
    "df": "Do",
    "dtf": "Do Terre",
    "dnf": "Do Neutre",
    "dff": "Do Feu",
    "daf": "Do Air",
    "def": "Do Eau",
    "dp": "Do Pou",
    "pa": "Ga Pa",
    "cc": "Cri",
    "pu": "Pui",
    "ic": "Invo",
    "pm": "Ga Pme",
    "ta": "Tac",
    "rpa": "Ret Pa",
    "rpm": "Ret Pme",
    "dc": "Do Cri",
    "dmg": "Do",
    "pd": "Pod",
}

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


class Caracteristique(models.Model):
    name = models.CharField(max_length=100)
    min = models.IntegerField()
    max = models.IntegerField()
    rune = models.ForeignKey(Rune, on_delete=models.CASCADE)

    # def __init__(self, dofusbook_caracteristique) -> None:
    #     self.name = dofusbook_caracteristique["name"]
    #     self.min = dofusbook_caracteristique["min"]
    #     self.max = dofusbook_caracteristique["max"]
    #     self.rune = Rune(runes_name[self.name])

    def __str__(self) -> str:
        return f"{{'name': \'{self.name}\', 'min': {self.min}, 'max': {self.max}}}"

    def gain_estime(self, level):
        ra, pa, ba = self.brisage(level)
        return ra * self.rune.prix_ra + pa * self.rune.prix_pa + ba * self.rune.prix_ba

    def brisage(self, level):
        return brisage_rune(level, self.min, self.max, self.rune.name)

    @classmethod
    def create_from_dofusbook(cls, dofusbook_caracteristique):
        if dofusbook_caracteristique["type"] == "O":
            return
        if dofusbook_caracteristique["name"] in [
                'pap', 'ptp', 'paf', 'pnf', 'pep', 'ptf', 'pfp', 'pnp', 'pef',
                'pff'
        ]:
            return
        rune, _ = Rune.objects.get_or_create(
            name=runes_name[dofusbook_caracteristique["name"]])
        carac, _ = cls.objects.get_or_create(
            name=dofusbook_caracteristique["name"],
            min=dofusbook_caracteristique["min"],
            max=dofusbook_caracteristique["max"],
            rune=rune)
        return carac.pk


class Ingredient(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    # count = models.IntegerField()
    _prix = models.IntegerField(default=1000000000)

    # def __init__(self, dofusbook_ingredient) -> None:
    #     self.name = dofusbook_ingredient["name"]
    #     self.count = dofusbook_ingredient["count"]

    def __str__(self) -> str:
        return self.name

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, value):
        self._prix = value


class IngredientForCraft(models.Model):
    # dofus_object = models.ForeignKey(DofusObject, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return f"{{name: \"{self.ingredient}\", quantity: {self.quantity}}}"

    @classmethod
    def create_from_dofusbook(cls, dofusbook_ingredient):
        ig, _ = Ingredient.objects.get_or_create(
            name=dofusbook_ingredient["name"])
        ingredient, _ = cls.objects.get_or_create(
            ingredient=ig, quantity=dofusbook_ingredient["count"])
        return ingredient.pk


class Metier(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self) -> str:
        return self.name


class DofusObject(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    level = models.IntegerField()
    metier = models.ForeignKey(Metier, on_delete=models.CASCADE)
    _effects = models.ManyToManyField(Caracteristique)
    _ingredients = models.ManyToManyField(IngredientForCraft)

    # def __init__(self, dofusbook_objet):
    #     self.name = dofusbook_objet["name"]
    #     self.level = dofusbook_objet["level"]
    #     self.effects = [
    #         Caracteristique(caracteristique)
    #         for caracteristique in dofusbook_objet["effects"]
    #     ]
    #     self.ingredients = [
    #         Ingredient(ingredient)
    #         for ingredient in dofusbook_objet["ingredients"]
    #     ]

    def __str__(self) -> str:
        return self.name

    def cout_fabrication(self) -> int:
        return int(
            sum([
                ingredient.ingredient.prix * ingredient.quantity
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
                Caracteristique.create_from_dofusbook(caracteristique)
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
