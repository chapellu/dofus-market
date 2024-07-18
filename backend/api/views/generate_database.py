import asyncio
import datetime

from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from api.scrapers.dofus_book_scraper import DofusBookScraper
from api.scrapers.official_website_scraper import OfficialWebsiteScraper


@api_view(["POST"])
def generate_data_base_post(request: Request) -> Response:
    DofusBookScraper.populateDB()
    return Response("ok")


@api_view(["POST"])
def generate_data_base(request: Request) -> Response:
    DofusBookScraper.populateDB()
    data = OfficialWebsiteScraper()
    now = datetime.datetime.now()  # datetime(2024, 6, 14, 22, 15, 31, 0)
    asyncio.run(data.load(now))
    data.populate_professions_db()
    data.populate_recipes_db()

    with connection.cursor() as cursor:
        cursor.execute("REFRESH MATERIALIZED VIEW EstimatedGains;")
        cursor.execute("REFRESH MATERIALIZED VIEW FabricationCosts;")
        cursor.execute("REFRESH MATERIALIZED VIEW Rentability;")
        cursor.execute("REFRESH MATERIALIZED VIEW OrderedByRentability;")

    return Response("ok")
