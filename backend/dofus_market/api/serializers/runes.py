from rest_framework import serializers

from market.database.rune import Rune


class RuneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rune
        fields = '__all__'
