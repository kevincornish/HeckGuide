import logging
import time
from typing import Dict, List

from api import HeckfireApi, TokenException
from .models import WorldSegments
from discord_webhook import DiscordWebhook
from django.conf import settings
from home.models import Webhooks
# Get an instance of a logger
logger = logging.getLogger(__name__)

class WorldImporter:
    def __init__(self, token: str, staytoken: str):
        self.api = HeckfireApi(token=token, staytoken=staytoken)
        self.model_fields = [f.name for f in WorldSegments._meta.get_fields()]
        self.created_count = 0
        self.updated_count = 0

    def format_segments(self, segments) -> List[Dict]:
        results = []
        for segment in segments:
            try:
                data = {key: value for key, value in segment.items() if key in self.model_fields}
                if data['owner_username']:
                    logger.info(f"Found player: {data['owner_username']} Clan: {data['owner_group_name']}")
                webhooks = Webhooks.objects.all()
                for webhook in webhooks.iterator():
                    item = webhook.item
                    hookurl = webhook.hookurl
                    realm = webhook.realm
                    if data['name'] in item:
                        if data['world_id'] == realm:
                            webhook = DiscordWebhook(url=(f'{hookurl}'), content=(f"{data['name']} X: {data['x']} Y: {data['y']}"))
                            webhook.execute()
                data['name'] = self.process_component(data['name'])
            except (TypeError, AttributeError) as e:
                pass
            results.append(data)
        return results

    def process_component(self, component_data: Dict) -> WorldSegments:
        data = {key: value for key, value in component_data.items() if key in self.model_fields}
        return self.update_or_create_segment(data)

    def update_or_create_segments(self, data: List[Dict]) -> None:
        for row in data:
            self.update_or_create_segment(row)

    def update_or_create_segment(self, data: Dict) -> WorldSegments:
        segment_data = data.copy()
        object_id = segment_data.pop('object_id')
        obj, created = WorldSegments.objects.update_or_create(object_id=object_id, defaults=segment_data)
        self.record_count(created)
        return obj

    def record_count(self, created):
        if created:
            self.created_count += 1
        else:
            self.updated_count += 1

    def execute(self, lowerbound: int, upperbound: int):
        logger.info(f"Crawling world")
        stay_alive = self.api.stay_alive()
        logger.info(f"Keeping token alive: {stay_alive['timestamp']}")
        self.crawl_world(lowerbound, upperbound)

    def crawl_world(self, lowerbound: int, upperbound: int):
        while lowerbound < upperbound:
            try:
                data = self.api.fetch_world(lowerbound)
                logger.info(f"Crawling bound: Lower Bound {[i for i in range(lowerbound, lowerbound + 20)]} Upper Bound {upperbound}")
            except TokenException as e:
                logger.info(f"Token exception found, sleeping for 60 seconds before retry. Exception: {e}")
                time.sleep(60)
                data = self.api.fetch_world(lowerbound)
            try:
                segments = self.format_segments(data)
                self.update_or_create_segments(segments)
                lowerbound += 20
                logger.info(f"Created {self.created_count} records")
                logger.info(f"Updated {self.updated_count} records")
                stay_alive = self.api.stay_alive()
                logger.info(f"Keeping token alive: {stay_alive['timestamp']}")
                self.api.collect_loot()
                logger.info(f"Collecting Loot")
                if lowerbound > 6327:
                    lowerbound = 1868
            except IndexError as e:
                logger.info(f"Index Error Exception: {e}")