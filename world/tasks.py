from celery import Celery
from world.importer import WorldImporter
from django.conf import settings
from celery import shared_task
app = Celery('tasks', broker='redis://localhost')

@shared_task
def scrape_world():
  staytoken = settings.STAY_ALIVE_TOKEN
  tokens = settings.TOKENS
  for token in tokens:
    importer = WorldImporter(token=token, staytoken=staytoken)
    importer.execute(lowerbound=1868, upperbound=6328)