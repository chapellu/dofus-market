from django.db import models


class Ingredient(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    price = models.IntegerField(default=1000000000)

    def __str__(self) -> str:
        return self.name
