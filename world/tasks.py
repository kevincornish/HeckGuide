from celery import Celery
from world.importer import WorldImporter
from django.conf import settings
app = Celery('tasks', broker='redis://localhost')

@app.task
def scrape_world(token):
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
  importer = WorldImporter(token=token, staytoken=staytoken)
  importer.execute(lowerbound=1868, upperbound=6328)