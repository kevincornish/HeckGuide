import random
from django.core.management.base import BaseCommand, CommandError
from poll.importer import RealmListImporter
from django.conf import settings
class Command(BaseCommand):
    help = 'Scrape chat log of realm'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        """
        This class polls the chat history for the realm of 
        given token.

        Usage: python manage.py poll_map 1
        """
        staytoken = settings.STAY_ALIVE_TOKEN
        tokens = settings.TOKENS
        token = random.choice(tokens)
        importer = RealmListImporter(token=token, staytoken=staytoken)
        importer.execute()