import random
from celery import Celery
from poll.importer import ChatImporter, RealmListImporter
from django.conf import settings
from celery import shared_task
app = Celery('tasks', broker='redis://localhost')

@shared_task
def poll_chat():
  staytoken = settings.STAY_ALIVE_TOKEN
  tokens = settings.TOKENS
  for token in tokens:
    importer = ChatImporter(token=token, staytoken=staytoken)
    importer.execute()

@shared_task
def poll_realm_list():
  staytoken = settings.STAY_ALIVE_TOKEN
  tokens = settings.TOKENS
  token = random.choice(tokens)
  importer = RealmListImporter(token=token, staytoken=staytoken)
  importer.execute()