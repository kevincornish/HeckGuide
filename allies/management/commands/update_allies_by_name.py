from django.core.management.base import BaseCommand, CommandError
from allies.importers import AllyByNameImporter
from allies.models import Ally

from django.conf import settings


class Command(BaseCommand):
    help = 'Find Ally records and update them'

    def add_arguments(self, parser):
        parser.add_argument('seed',  type=int)
        parser.add_argument('depth',  type=int)

    def handle(self, *args, **options):
        """
        This class will search the database for already imported ally names
        and then search the api to get an updated user.
        """
        staytoken = settings.STAY_ALIVE_TOKEN
        tokens = settings.TOKENS
        for token in tokens:
            partial_allies = Ally.objects.all().values('username')
            seed_list = [a['username'] for a in partial_allies]
            seed_list = seed_list[:options['seed']]
            importer = AllyByNameImporter(token=token, staytoken=staytoken)
            importer.execute(seed_list, depth=options['depth'])