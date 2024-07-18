from django.db.models import QuerySet
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from api.serializers.metiers import MetierSerializer
from market.database.metier import Metier


@api_view(["GET"])
def get_metiers(request: Request) -> Response:
    query_set: QuerySet = Metier.objects.all()
    serializer: Serializer = MetierSerializer(query_set, many=True)
    return Response(serializer.data)
