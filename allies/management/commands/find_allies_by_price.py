import random
from django.core.management.base import BaseCommand, CommandError
from allies.importers import AllyByPriceImporter

from django.conf import settings

class Command(BaseCommand):
    help = 'Scrapes allies from the heckfire API by price and page number'
    """
    Usage: python manage.py find_allies_by_price price "1000" page count "5"
    """
    def add_arguments(self, parser):
        parser.add_argument('price',  type=int)
        parser.add_argument('page_count',  type=int)

    def handle(self, *args, **options):
        staytoken = settings.STAY_ALIVE_TOKEN
        tokens = settings.TOKENS
        token = random.choice(tokens)
        importer = AllyByPriceImporter(token=token, staytoken=staytoken)
        importer.execute(options['price'], options['page_count'])
