from rest_framework import serializers


class MetierSerializer(serializers.Serializer):
    name = serializers.CharField()
