from django.core.management.base import BaseCommand, CommandError
from api import HeckfireApi, TokenException
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
class Command(BaseCommand):
    help = 'Purchase an ally via supplied username'

    def add_arguments(self, parser):
        parser.add_argument('username',  type=str)
        parser.add_argument('token',  type=int)

    def handle(self, *args, **options):
        """
        This class first takes the username supplied and will search the api for the user details,
        once returned it will take the user_id and cost and attempt to purchase the ally with the 
        given token.

        Usage: python manage.py buy_ally_by_name username "kevz" token "23"
        """
        staytoken = settings.STAY_ALIVE_TOKEN
        if options['token'] == 1:
            token = settings.HECKFIRE_API_TOKEN
        elif options['token'] == 106:
            token = settings.TOKEN_106
        elif options['token'] == 10:
            token = settings.TOKEN_10
        elif options['token'] == 92:
            token = settings.TOKEN_92
        elif options['token'] == 99:
            token = settings.TOKEN_99
        elif options['token'] == 128:
            token = settings.TOKEN_128
        elif options['token'] == 129:
            token = settings.TOKEN_129
        elif options['token'] == 121:
            token = settings.TOKEN_121
        elif options['token'] == 130:
            token = settings.TOKEN_130
        username = options['username']
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