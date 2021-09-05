from django.core.management.base import BaseCommand, CommandError
from api import HeckfireApi, TokenException
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
class Command(BaseCommand):
    help = 'Volly an ally via supplied username'

    def add_arguments(self, parser):
        parser.add_argument('username',  type=str)

    def handle(self, *args, **options):
        """
        This class find an ally through the supplied username, and
        will cycle through each token purchasing the ally on each account.

        Usage: python manage.py volly_ally username "kevz"
        """
        staytoken = settings.STAY_ALIVE_TOKEN
        tokens = [settings.HECKFIRE_API_TOKEN,settings.TOKEN_10, settings.TOKEN_23,settings.TOKEN_128,settings.TOKEN_129]
        username = options['username']
        for token in tokens:
          api = HeckfireApi(token=token, staytoken=staytoken)
          ally = api.get_ally_by_name(username)
          try:
              user_id = ally['allies'][0]["user_id"]
              cost = ally['allies'][0]["cost"]
              try:
                  api.collect_loot()
                  api.buy_ally(user_id, cost)
                  api.stay_alive()
                  logger.info(f"Buying '{username}', ID: {user_id}, Cost: {cost}")
              except TokenException as e:
                  logger.info(f"Exception: {e}")
          except IndexError as e:
              logger.info(f"User does not exist")