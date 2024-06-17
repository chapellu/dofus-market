from django.db import models


class Rune(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    prix_ra = models.IntegerField(default=0)
    prix_pa = models.IntegerField(default=0)
    prix_ba = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
