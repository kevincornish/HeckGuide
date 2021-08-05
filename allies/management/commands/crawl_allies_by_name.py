from django.core.management.base import BaseCommand, CommandError
from allies.importers import AllyByNameImporter
from allies.models import Ally

from django.conf import settings


class Command(BaseCommand):
    help = 'Find CurrentAlly owner records that have incomplete data'

    def add_arguments(self, parser):
        parser.add_argument('seed',  type=int)
        parser.add_argument('depth',  type=int)

    def handle(self, *args, **options):
        """
        This class imports allies currently in the database that are missing full results. The "owner" object
        that is returned does not returns a partial dataset, so this method looks for allies that have a null
        biome3 attack multiplier and fetches the full dataset for that ally.

        It will first fetch the ally, then the owner, then the owner's owner, etc until we're 'depth' layers deep. 

        Usage: python manage.py crawl_allies_by_name seed "10" depth "5"
        """
        partial_allies = Ally.objects.filter(biome3_attack_multiplier__isnull=True).values('username')
        seed_list = [a['username'] for a in partial_allies]
        seed_list = seed_list[:options['seed']]
        importer = AllyByNameImporter(token=settings.HECKFIRE_API_TOKEN)
        importer.execute(seed_list, depth=options['depth'])
