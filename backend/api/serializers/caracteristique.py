from typing import Any

from rest_framework import serializers
from rest_framework.serializers import ReturnDict, ReturnList

from api.serializers.runes import RuneSerializer
from market.database.rune import Rune


class CaracteristiqueSerializer(serializers.Serializer):
    name = serializers.CharField()
    min = serializers.IntegerField()
    max = serializers.IntegerField()
    rune = serializers.SerializerMethodField("serialize_rune")

    def serialize_rune(self, rune: Rune) -> ReturnList | Any | ReturnDict:
        return RuneSerializer(rune.rune).data
