from django.core.management.base import BaseCommand, CommandError
from allies.importers import AllyByPriceImporter

from django.conf import settings

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('price',  type=int)
        parser.add_argument('page_count',  type=int)

    def handle(self, *args, **options):
        importer = AllyByPriceImporter(token=settings.HECKFIRE_API_TOKEN, staytoken=settings.STAY_ALIVE_TOKEN)
        importer.execute(options['price'], options['page_count'])
