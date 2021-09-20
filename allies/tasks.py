from celery import Celery
from allies.importers import AllyByNameImporter, RandomAllyByPriceImporter
from django.conf import settings
from celery import shared_task
from allies.models import Ally
app = Celery('tasks', broker='redis://localhost')

@shared_task
def scrape_allies_by_name():
  staytoken = settings.STAY_ALIVE_TOKEN
  tokens = [settings.HECKFIRE_API_TOKEN, settings.TOKEN_106,
            settings.TOKEN_10,settings.TOKEN_128,settings.TOKEN_129,
            settings.TOKEN_99]
  for token in tokens:
    partial_allies = Ally.objects.all().order_by('-cost').values('username')
    seed_list = [a['username'] for a in partial_allies]
    seed_list = seed_list[:100]
    importer = AllyByNameImporter(token=token, staytoken=staytoken)
    importer.execute(seed_list, depth=5)

@shared_task
def scrape_allies_by_rand_price():
  staytoken = settings.STAY_ALIVE_TOKEN
  tokens = [settings.HECKFIRE_API_TOKEN, settings.TOKEN_106,
            settings.TOKEN_10,settings.TOKEN_128,settings.TOKEN_129,
            settings.TOKEN_99]
  for token in tokens:
    importer = RandomAllyByPriceImporter(token=token, staytoken=staytoken)
    importer.execute()