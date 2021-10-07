import random
from celery import Celery
from poll.importer import ChatImporter, RealmListImporter, ClanChatImporter
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
def poll_clan_chat(realm):
  staytoken = settings.STAY_ALIVE_TOKEN
  if realm == 23:
      token = settings.HECKFIRE_API_TOKEN
  elif realm == 106:
      token = settings.TOKEN_106
  elif realm == 10:
      token = settings.TOKEN_10
  elif realm == 92:
      token = settings.TOKEN_92
  elif realm == 99:
      token = settings.TOKEN_99
  elif realm == 128:
      token = settings.TOKEN_128
  elif realm == 129:
      token = settings.TOKEN_129
  elif realm == 121:
      token = settings.TOKEN_121
  elif realm == 130:
      token = settings.TOKEN_130
  importer = ClanChatImporter(token=token, staytoken=staytoken, realm=realm)
  importer.execute()

@shared_task
def poll_realm_list():
  staytoken = settings.STAY_ALIVE_TOKEN
  tokens = settings.TOKENS
  token = random.choice(tokens)
  importer = RealmListImporter(token=token, staytoken=staytoken)
  importer.execute()