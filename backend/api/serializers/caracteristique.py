from rest_framework import serializers

from .runes import RuneSerializer


class CaracteristiqueSerializer(serializers.Serializer):
    name = serializers.CharField()
    min = serializers.IntegerField()
    max = serializers.IntegerField()
    rune = serializers.SerializerMethodField("serialize_rune")

    def serialize_rune(self, foo):
        return RuneSerializer(foo.rune).data
