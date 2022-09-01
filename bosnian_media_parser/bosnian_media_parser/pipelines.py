# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging

logger = logging.getLogger('logger')


class BosnianMediumParserPipeline:
    def process_item(self, item, spider):
        if not self.is_valid_object(item):
            logging.error('Invalid item')
            return
        return item

    def is_valid_object(self, item):
        keys = [
            'title',
            'content',
            'array',
            'medium_id',
            'url',
            'date',
            'html',
        ]

        item_keys = list(item.keys())
        item_keys.sort()
        keys.sort()

        return item_keys == keys
