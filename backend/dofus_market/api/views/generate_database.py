import asyncio
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib import admin
from api.scrapers.dofus_book_scraper import DofusBookScraper
from api.scrapers.official_website_scraper import OfficialWebsiteScraper
import datetime


@api_view(['POST'])
def generate_data_base_post(request):
    DofusBookScraper.populateDB()
    return Response("ok")


@api_view(['POST'])
def generate_data_base(request):
    DofusBookScraper.populateDB()
    data = OfficialWebsiteScraper()
    now = datetime.datetime.now()  #datetime(2024, 6, 14, 22, 15, 31, 0)
    asyncio.run(data.load(now))
    data.populate_professions_db()
    data.populate_recipes_db()
    return Response("ok")
