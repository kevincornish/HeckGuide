from django.core.management.base import BaseCommand, CommandError
from api import HeckfireApi, TokenException
from django.conf import settings
from allies.models import Ally
import logging
logger = logging.getLogger(__name__)
class Command(BaseCommand):
    help = 'Strip a users allies via supplied username and token'

    def add_arguments(self, parser):
        parser.add_argument('username',  type=str)
        parser.add_argument('token',  type=int)

    def handle(self, *args, **options):
        """
        This class finds all allies owned by given username in heckguide db,
        then attempts to purchase all found allies.
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
        username = options['username']
        user_list = Ally.objects.filter(owner__username__iexact=username).values("user_id", "cost", "username")
        api = HeckfireApi(token=token, staytoken=staytoken)
        try:
          for user in user_list:
            username = user['username']
            cost = user['cost']
            user_id = user['user_id']
            try:
                logger.info(f"Buying {username}, Cost: {cost}")
                api.collect_loot()
                api.buy_ally(user_id, cost)
                api.stay_alive()
            except TokenException as e:
                logger.info(f"Exception: {e}")
        except IndexError as e:
            logger.info(f"User does not exist")