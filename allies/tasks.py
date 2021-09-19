from celery import Celery
from allies.importers import AllyByNameImporter
from django.conf import settings
from celery import shared_task
from allies.models import Ally
app = Celery('tasks', broker='redis://localhost')

@shared_task
def scrape_allies_by_name(token):
  staytoken = settings.STAY_ALIVE_TOKEN
  if token == 1:
    token = settings.HECKFIRE_API_TOKEN
  elif token == 106:
    token = settings.TOKEN_106
  elif token == 10:
    token = settings.TOKEN_10
  elif token == 99:
    token = settings.TOKEN_99
  elif token == 128:
    token = settings.TOKEN_128
  elif token == 129:
    token = settings.TOKEN_129
  partial_allies = Ally.objects.all().order_by('-cost').values('username')
  seed_list = [a['username'] for a in partial_allies]
  seed_list = seed_list[:100]
  importer = AllyByNameImporter(token=token, staytoken=staytoken)
  importer.execute(seed_list, depth=5)