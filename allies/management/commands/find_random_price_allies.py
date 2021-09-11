from django.core.management.base import BaseCommand, CommandError
from allies.importers import RandomAllyByPriceImporter
from django.conf import settings

class Command(BaseCommand):
    help = 'Scrapes allies from the heckfire API by price and page number'
    """
    Usage: python manage.py find_random_price_allies token "1"
    """
    def add_arguments(self, parser):
        parser.add_argument('token',  type=int)

    def handle(self, *args, **options):
        staytoken = settings.STAY_ALIVE_TOKEN
        if options['token'] == 1:
            token = settings.HECKFIRE_API_TOKEN
        elif options['token'] == 106:
            token = settings.TOKEN_106
        elif options['token'] == 10:
            token = settings.TOKEN_10
        elif options['token'] == 128:
            token = settings.TOKEN_128
        elif options['token'] == 129:
            token = settings.TOKEN_129
        importer = RandomAllyByPriceImporter(token=token, staytoken=staytoken)
        importer.execute()