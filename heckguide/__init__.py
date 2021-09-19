import environ
env = environ.Env()
environ.Env.read_env()
DEBUG = env.bool("DJANGO_DEBUG", False)
if not DEBUG:
  from .celery import app as celery_app
  __all__ = ('celery_app',)