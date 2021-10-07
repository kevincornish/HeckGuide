import logging
import time
from typing import Dict, List

from api import HeckfireApi, TokenException
from .models import RealmChat, RealmList, ClanChat
from discord_webhook import DiscordWebhook
from home.models import Webhooks
# Get an instance of a logger
logger = logging.getLogger(__name__)

class ChatImporter:
    def __init__(self, token: str, staytoken: str):
        self.api = HeckfireApi(token=token, staytoken=staytoken)
        self.model_fields = [f.name for f in RealmChat._meta.get_fields()]
        self.created_count = 0
        self.updated_count = 0
        self.webhooks = Webhooks.objects.all().filter(item="Chatlog")

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
        try:
            data = self.api.poll_chat()
        except TokenException as e:
            logger.info(f"Token exception found, sleeping for 60 seconds before retry. Exception: {e}")
            time.sleep(60)
            data = self.api.poll_chat()
        try:
            segments = self.format_segments(data)
            self.update_or_create_segments(segments)
        except IndexError as e:
            logger.info(f"Index Error Exception: {e}")


class ClanChatImporter:
    def __init__(self, token: str, staytoken: str, realm: int):
        self.api = HeckfireApi(token=token, staytoken=staytoken)
        self.model_fields = [f.name for f in ClanChat._meta.get_fields()]
        self.created_count = 0
        self.updated_count = 0
        self.realm = realm
        self.webhooks = Webhooks.objects.all().filter(item="ClanChatlog")

    def format_segments(self, segments) -> List[Dict]:
        results = []
        for segment in segments:
            try:
                data = {key: value for key, value in segment.items() if key in self.model_fields}
                data['realm'] = self.realm
                data['mail_id']= data.pop('id')
                data['mail_id'] = self.process_component(data['mail_id'])
            except (TypeError, AttributeError) as e:
                pass
            results.append(data)
        return results

    def process_component(self, component_data: Dict) -> ClanChat:
        data = {key: value for key, value in component_data.items() if key in self.model_fields}
        return self.update_or_create_segment(data)

    def update_or_create_segments(self, data: List[Dict]) -> None:
        for row in data:
            self.update_or_create_segment(row)

    def update_or_create_segment(self, data: Dict) -> ClanChat:
        segment_data = data.copy()
        mail_id = segment_data.pop('mail_id')
        obj, created = ClanChat.objects.update_or_create(mail_id=mail_id, defaults=segment_data)
        self.record_count(created, data)
        return obj

    def record_count(self, created, data):
        if created:
            for webhook in self.webhooks.iterator():
                hookurl = webhook.hookurl
                realm = webhook.realm
                if data['realm'] == realm:
                    webhook = DiscordWebhook(url=(f'{hookurl}'), content=(f"{data['username']} {data['message']}"))
                    webhook.execute()
                    logger.info(f"Chat Log: {data['username']}, {data['message']}")
            self.created_count += 1
        else:
            self.updated_count += 1

    def execute(self):
        logger.info(f"Polling clan chat")
        self.crawl_chat()

    def crawl_chat(self):
        try:
            data = self.api.poll_clan_chat()
        except TokenException as e:
            logger.info(f"Token exception found, sleeping for 60 seconds before retry. Exception: {e}")
            time.sleep(60)
            data = self.api.poll_clan_chat()
        try:
            segments = self.format_segments(data)
            self.update_or_create_segments(segments)
        except IndexError as e:
            logger.info(f"Index Error Exception: {e}")

class RealmListImporter:
    def __init__(self, token: str, staytoken: str):
        self.api = HeckfireApi(token=token, staytoken=staytoken)
        self.model_fields = [f.name for f in RealmList._meta.get_fields()]
        self.created_count = 0
        self.updated_count = 0

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

    def process_component(self, component_data: Dict) -> RealmList:
        data = {key: value for key, value in component_data.items() if key in self.model_fields}
        return self.update_or_create_segment(data)

    def update_or_create_segments(self, data: List[Dict]) -> None:
        for row in data:
            self.update_or_create_segment(row)

    def update_or_create_segment(self, data: Dict) -> RealmList:
        segment_data = data.copy()
        id = segment_data.pop('id')
        obj, created = RealmList.objects.update_or_create(id=id, defaults=segment_data)
        self.record_count(created, data)
        return obj

    def record_count(self, created, data):
        if created:
            self.created_count += 1
        else:
            self.updated_count += 1

    def execute(self):
        logger.info(f"Polling Realm List")
        self.crawl_realm_list()

    def crawl_realm_list(self):
        try:
            data = self.api.poll_realm_list()
        except TokenException as e:
            logger.info(f"Token exception found, sleeping for 60 seconds before retry. Exception: {e}")
            time.sleep(60)
            data = self.api.poll_realm_list()
        try:
            segments = self.format_segments(data)
            self.update_or_create_segments(segments)
        except IndexError as e:
            logger.info(f"Index Error Exception: {e}")