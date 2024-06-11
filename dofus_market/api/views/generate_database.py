from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib import admin
from api.scrapers.dofus_book_scraper import DofusBookScraper

@api_view(['POST'])
def generate_data_base_post(request):
    DofusBookScraper.generateDB()
    return Response("ok")
