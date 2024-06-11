from market.database.equipement import DofusObject
import json
import requests


class DofusBookScraper:
    def generateDB():
        url = "https://touch.dofusbook.net/items/touch/search/equipment"
        req = requests.get(url + '?page=1')
        first_page = json.loads(req.text)
        page_count = first_page["pages"]

        items = first_page["data"]
        for item in items:
            DofusObject.create_from_dofusbook_object(item)

        for i in range(2, page_count + 1):
            response = requests.get(
                url + f'?page={i}'
            )
            page = json.loads(response.text)
            for item in page["data"]:
                DofusObject.create_from_dofusbook_object(item)
