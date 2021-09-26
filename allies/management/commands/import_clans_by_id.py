import random
from django.core.management.base import BaseCommand, CommandError
from allies.importers import ClanImporter
from allies.models import Ally

from django.conf import settings

class Command(BaseCommand):
    help = 'Scrapes allies from the heckfire API by price and page number'
    """
    Usage: python manage.py find_allies_by_price price "1000" page count "5"
    """
    def add_arguments(self, parser):
        parser.add_argument('seed',  type=int)

    def handle(self, *args, **options):
        clan_list = Ally.objects.all().exclude(group_id__isnull=True).order_by('-last_modified').values('group_id')
        seed_list = [a['group_id'] for a in clan_list]
        seed_list = seed_list[:options['seed']]
        staytoken = settings.STAY_ALIVE_TOKEN
        tokens = settings.TOKENS
        token = random.choice(tokens)
        for clan in seed_list:
          importer = ClanImporter(token=token, staytoken=staytoken)
          importer.execute(clan)