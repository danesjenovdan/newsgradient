from analize.models import Media, News

from django.core.management.base import BaseCommand
from urllib.parse import urlparse
from datetime import datetime

import json


class Command(BaseCommand):
    help = 'Load news'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            nargs=1,
            help='File path',
        )

    def handle(self, *args, **options):
        file_path = options['file'][0]
        f = open (file_path, "r")
        data = json.loads(f.read())

        media = Media.objects.get(id=data[0]['medium_id'])
        for news in data:
            News(
                title=news['title'],
                content=news['content'],
                link=news['url'],
                html=news['html'],
                media=media,
                published_at=news['date'],
                parsed_at=datetime.now(),
                last_parsed_at=datetime.now(),
            ).save()

