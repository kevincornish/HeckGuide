from django.core.management.base import BaseCommand, CommandError
from world.importer import WorldImporter

from django.conf import settings


class Command(BaseCommand):
    help = 'Crawl through the world'

    def handle(self, *args, **options):
        """
        Usage: python manage.py crawl_world
        """
        importer = WorldImporter(token=settings.HECKFIRE_API_TOKEN, staytoken=settings.STAY_ALIVE_TOKEN)
        importer.execute(lowerbound=1868, upperbound=6317)