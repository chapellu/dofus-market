import time

from api.serializers.equipements import DofusObjectSerializer
from market.database.equipement import DofusObject
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_dofus_object(request):
    t1 = time.process_time()
    print("Enter GET")
    dofus_objects = DofusObject.objects.all().prefetch_related(
        "_effects", "_ingredients", "metier")[:10]
    t2 = time.process_time()
    print("GET Done", t2 - t1)
    t3 = time.process_time()
    print("Enter Serializer")
    serializer = DofusObjectSerializer(dofus_objects, many=True)
    data = serializer.data
    t4 = time.process_time()
    print("Serializer Done", t4 - t3)
    print("Total request time", t4 - t1)
    return Response(data)
