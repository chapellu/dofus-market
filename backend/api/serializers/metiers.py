from rest_framework import serializers

from market.database.metier import Metier


class MetierSerializer(serializers.Serializer):

    name = serializers.CharField()
