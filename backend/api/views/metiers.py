from api.serializers.metiers import MetierSerializer
from django.db.models import QuerySet
from market.database.metier import Metier
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.utils.serializer_helpers import ReturnDict


@api_view(['GET'])
def get_metiers(request: Request):
    query_set: QuerySet = Metier.objects.all()
    serializer: Serializer = MetierSerializer(query_set, many=True)
    return Response(serializer.data)
