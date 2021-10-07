from django.core.management.base import BaseCommand
from world.importer import WorldImporter

from django.conf import settings


class Command(BaseCommand):
    help = 'Crawl through the world using selected token'

    def add_arguments(self, parser):
        parser.add_argument('token',  type=int)

    def handle(self, *args, **options):
        """
        Usage: python manage.py crawl_world token "2"
        """
        staytoken = settings.STAY_ALIVE_TOKEN
        if options['token'] == 1:
            token = settings.HECKFIRE_API_TOKEN
        elif options['token'] == 128:
            token = settings.TOKEN_128
        elif options['token'] == 106:
            token = settings.TOKEN_106
        elif options['token'] == 10:
            token = settings.TOKEN_10
        elif options['token'] == 92:
            token = settings.TOKEN_92
        elif options['token'] == 99:
            token = settings.TOKEN_99
        elif options['token'] == 129:
            token = settings.TOKEN_129
        elif options['token'] == 121:
            token = settings.TOKEN_121
        elif options['token'] == 130:
            token = settings.TOKEN_130
        importer = WorldImporter(token=token, staytoken=staytoken)
        importer.execute(lowerbound=1868, upperbound=6328)