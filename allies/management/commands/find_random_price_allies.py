from django.core.management.base import BaseCommand, CommandError
from allies.importers import RandomAllyByPriceImporter
from django.conf import settings

class Command(BaseCommand):
    help = 'Scrapes allies from the heckfire API by price'
    """
    Usage: python manage.py find_random_price_allies
    """
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        staytoken = settings.STAY_ALIVE_TOKEN
        tokens = [settings.HECKFIRE_API_TOKEN, settings.TOKEN_106,
                settings.TOKEN_10,settings.TOKEN_128,settings.TOKEN_129,
                settings.TOKEN_99]
        for token in tokens:
            importer = RandomAllyByPriceImporter(token=token, staytoken=staytoken)
            importer.execute()