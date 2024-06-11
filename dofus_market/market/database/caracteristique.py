from django.db import models

from .rune import Rune
from .runes_data import runes_name
from ..runes import brisage_rune


class Caracteristique(models.Model):
    name = models.CharField(max_length=100)
    min = models.IntegerField()
    max = models.IntegerField()
    rune = models.ForeignKey(Rune, on_delete=models.CASCADE)
    level = models.IntegerField()
    number_of_ra = models.FloatField(default=0.0)
    number_of_pa = models.FloatField(default=0.0)
    number_of_ba = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f"{{'name': \'{self.name}\', 'min': {self.min}, 'max': {self.max}}}"

    def gain_estime(self, level):
        return self.number_of_ra * self.rune.prix_ra + self.number_of_pa * self.rune.prix_pa + self.number_of_ba * self.rune.prix_ba

    def brisage(self, level):
        return self.number_of_ba, self.number_of_pa, self.number_of_ba

    @classmethod
    def create_from_dofusbook(cls, dofusbook_caracteristique, level):
        if dofusbook_caracteristique["type"] == "O":
            return
        if dofusbook_caracteristique["name"] in [
                'pap', 'ptp', 'paf', 'pnf', 'pep', 'ptf', 'pfp', 'pnp', 'pef',
                'pff'
        ]:
            return
        ra, pa, ba = brisage_rune(
            level, dofusbook_caracteristique["min"],
            dofusbook_caracteristique["max"],
            runes_name[dofusbook_caracteristique["name"]])
        rune, _ = Rune.objects.get_or_create(
            name=runes_name[dofusbook_caracteristique["name"]])
        carac, _ = cls.objects.get_or_create(
            name=dofusbook_caracteristique["name"],
            min=dofusbook_caracteristique["min"],
            max=dofusbook_caracteristique["max"],
            rune=rune,
            level=level,
            number_of_ra=ra,
            number_of_pa=pa,
            number_of_ba=ba)
        return carac.pk
