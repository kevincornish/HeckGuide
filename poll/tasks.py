from celery import Celery
from poll.importer import ChatImporter
from django.conf import settings
app = Celery('tasks', broker='redis://localhost')

@app.task
def poll_chat(token: int):
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
  importer = ChatImporter(token=token, staytoken=staytoken)
  importer.execute()