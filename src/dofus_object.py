from src.runes import brisage_rune

runes_name = {
    "vi": "Vi",
    "ag": "Age",
    "pm": "Ga Pme",
    "rtp": "Ré Per Terre",
    "dt": "Do Terre",
    "fo": "Fo",
    "in": "Ine",
    "po": "Po",
    "so": "So"
}

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


class Rune:
    name: str
    _prix_ra: int = 0
    _prix_pa: int = 0
    _prix_ba: int = 0

    def __init__(self, rune_name) -> None:
        self.name = rune_name

    @property
    def prix_ra(self):
        return runes_price.get(f"Ra {self.name}", 0)

    @prix_ra.setter
    def prix_ra(self, value):
        self._prix_ra = value

    @property
    def prix_pa(self):
        return runes_price.get(f"Pa {self.name}", 0)

    @prix_pa.setter
    def prix_pa(self, value):
        self._prix_pa = value

    @property
    def prix_ba(self):
        return runes_price[self.name]

    @prix_ba.setter
    def prix_ba(self, value):
        self._prix_ba = value


class Caracteristique:
    name: str
    min: int
    max: int
    rune_name: str

    def __init__(self, dofusbook_caracteristique) -> None:
        self.name = dofusbook_caracteristique["name"]
        self.min = dofusbook_caracteristique["min"]
        self.max = dofusbook_caracteristique["max"]
        self.rune_name = runes_name[self.name]

    def __repr__(self) -> str:
        return f"{{'name': \'{self.name}\', 'min': {self.min}, 'max': {self.max}}}"

    def gain_estime(self, level):
        ra, pa, ba = brisage_rune(level, self.min, self.max, self.rune_name)
        return ra * Rune(self.rune_name).prix_ra + pa * Rune(
            self.rune_name).prix_pa + ba * Rune(self.rune_name).prix_ba


class Ingredient:
    name: str
    count: int
    _prix: int

    def __init__(self, dofusbook_ingredient) -> None:
        self.name = dofusbook_ingredient["name"]
        self.count = dofusbook_ingredient["count"]
        self.prix = 1000000000

    def __repr__(self) -> str:
        return f"{{'name': '{self.name}', 'count': {self.count}, 'prix': {self.prix}}}"

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, value):
        self._prix = value


class DofusObject:
    name: str
    level: int
    effects: list[Caracteristique]
    ingredients: list[Ingredient]

    def __init__(self, dofusbook_objet):
        self.name = dofusbook_objet["name"]
        self.level = dofusbook_objet["level"]
        self.effects = [
            Caracteristique(caracteristique)
            for caracteristique in dofusbook_objet["effects"]
        ]
        self.ingredients = [
            Ingredient(ingredient)
            for ingredient in dofusbook_objet["ingredients"]
        ]

    def cout_fabrication(self):
        return sum([
            ingredient.prix * ingredient.count
            for ingredient in self.ingredients
        ])

    def gain_estime(self):
        return sum([
            caracteristique.gain_estime(self.level)
            for caracteristique in self.effects
        ])

    def rentabilite(self):
        return (self.gain_estime() / self.cout_fabrication()) * 100

    @property
    def nombre_ingredients(self):
        return len(self.ingredients)
