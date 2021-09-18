from django.core.management.base import BaseCommand, CommandError
from api import HeckfireApi, TokenException
from poll.models import RealmChat
from poll.importer import ChatImporter
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
class Command(BaseCommand):
    help = 'Scrape chat log of realm'

    def add_arguments(self, parser):
        parser.add_argument('token',  type=int)

    def handle(self, *args, **options):
        """
        This class polls the chat history for the realm of 
        given token.

        Usage: python manage.py poll_map 1
        """
        staytoken = settings.STAY_ALIVE_TOKEN
        if options['token'] == 1:
            token = settings.HECKFIRE_API_TOKEN
        elif options['token'] == 106:
            token = settings.TOKEN_106
        elif options['token'] == 10:
            token = settings.TOKEN_10
        elif options['token'] == 99:
            token = settings.TOKEN_99
        elif options['token'] == 128:
            token = settings.TOKEN_128
        elif options['token'] == 129:
            token = settings.TOKEN_129
        importer = ChatImporter(token=token, staytoken=staytoken)
        importer.execute()