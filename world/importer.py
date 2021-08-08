import logging
import time
from typing import Dict, List

from api import HeckfireApi, TokenException
from .models import WorldSegments

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
                data['name'] = self.process_component(data['name'])
                logger.info(f"Found Component: {data['name']}")
            except (TypeError, AttributeError) as e:
                logger.info(f"NoneType Error Exception: {e}")
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

    def execute(self):
      logger.info(f"Crawling world")
      stay_alive = self.api.stay_alive()
      logger.info(f"Keeping token alive: {stay_alive['timestamp']}")
      self.crawl_world()

    def crawl_world(self):
        try:
            data = self.api.fetch_world()
            logger.info(f"Fetching world {data}")
        except TokenException as e:
            logger.info(f"Token exception found, sleeping for 60 seconds before retry. Exception: {e}")
            time.sleep(60)
        segments = self.format_segments(data)
        self.update_or_create_segments(segments)

        logger.info(f"Created {self.created_count} records")
        logger.info(f"Updated {self.updated_count} records")