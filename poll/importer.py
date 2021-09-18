import logging
import time
from typing import Dict, List

from api import HeckfireApi, TokenException
from .models import RealmChat
from discord_webhook import DiscordWebhook
from django.conf import settings
from home.models import Webhooks
# Get an instance of a logger
logger = logging.getLogger(__name__)

class ChatImporter:
    def __init__(self, token: str, staytoken: str):
        self.api = HeckfireApi(token=token, staytoken=staytoken)
        self.model_fields = [f.name for f in RealmChat._meta.get_fields()]
        self.created_count = 0
        self.updated_count = 0
        self.webhooks = Webhooks.objects.all()

    def format_segments(self, segments) -> List[Dict]:
        results = []
        for segment in segments:
            try:
                data = {key: value for key, value in segment.items() if key in self.model_fields}
                data['id'] = self.process_component(data['id'])
            except (TypeError, AttributeError) as e:
                pass
            results.append(data)
        return results

    def process_component(self, component_data: Dict) -> RealmChat:
        data = {key: value for key, value in component_data.items() if key in self.model_fields}
        return self.update_or_create_segment(data)

    def update_or_create_segments(self, data: List[Dict]) -> None:
        for row in data:
            self.update_or_create_segment(row)

    def update_or_create_segment(self, data: Dict) -> RealmChat:
        segment_data = data.copy()
        id = segment_data.pop('id')
        obj, created = RealmChat.objects.update_or_create(id=id, defaults=segment_data)
        self.record_count(created, data)
        return obj

    def record_count(self, created, data):
        if created:
            for webhook in self.webhooks.iterator():
                hookurl = webhook.hookurl
                realm = webhook.realm
                if data['region'] == realm:
                    webhook = DiscordWebhook(url=(f'{hookurl}'), content=(f"{data['username']} {data['message']}"))
                    webhook.execute()
                    logger.info(f"Chat Log: {data['username']}, {data['message']}")
            self.created_count += 1
        else:
            self.updated_count += 1

    def execute(self):
        logger.info(f"Polling chat")
        self.crawl_chat()

    def crawl_chat(self):
        while True:
            try:
                data = self.api.poll_chat()
            except TokenException as e:
                logger.info(f"Token exception found, sleeping for 60 seconds before retry. Exception: {e}")
                time.sleep(60)
                data = self.api.poll_chat()
            try:
                segments = self.format_segments(data)
                self.update_or_create_segments(segments)
                time.sleep(20)
            except IndexError as e:
                logger.info(f"Index Error Exception: {e}")