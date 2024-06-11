from rest_framework.response import Response
from rest_framework.decorators import api_view

from market.database.equipement import DofusObject
import json
import requests


@api_view(['POST'])
def import_dofusbook_equipement(request):
    req = requests.get(
        'https://touch.dofusbook.net/items/touch/search/equipment?page=1')
    first_page = json.loads(req.text)
    page_count = first_page["pages"]

    items = first_page["data"]
    for item in items:
        DofusObject.create_from_dofusbook_object(item)

    for i in range(2, page_count + 1):
        response = requests.get(
            f'https://touch.dofusbook.net/items/touch/search/equipment?page={i}'
        )
        page = json.loads(response.text)
        for item in page["data"]:
            DofusObject.create_from_dofusbook_object(item)

    return Response("ok")
