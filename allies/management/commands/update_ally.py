import random
from django.core.management.base import BaseCommand, CommandError
from allies.importers import UpdateAllyImporter

from django.conf import settings


class Command(BaseCommand):
    help = 'Find Ally and update'

    def add_arguments(self, parser):
        parser.add_argument('username',  type=str)

    def handle(self, *args, **options):
        """
        This class will search the database for already imported ally
        and then search the api to get an updated user.
        """
        staytoken = settings.STAY_ALIVE_TOKEN
        tokens = settings.TOKENS
        token = random.choice(tokens)
        name=options['username']
        importer = UpdateAllyImporter(token=token, staytoken=staytoken)
        importer.execute(name)