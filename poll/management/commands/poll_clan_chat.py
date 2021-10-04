from django.core.management.base import BaseCommand, CommandError
from poll.importer import ClanChatImporter
from django.conf import settings
class Command(BaseCommand):
    help = 'Scrape clan chat log of realm'

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
        importer = ClanChatImporter(token=token, staytoken=staytoken, realm=options['token'])
        importer.execute()