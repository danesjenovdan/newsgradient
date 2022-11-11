from analize.models import Media

from django.core.management.base import BaseCommand
from urllib.parse import urlparse
from datetime import datetime

import json


class Command(BaseCommand):
    help = 'Load media URLs from local json file.'

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

        print(Media.objects.all())
        for medium in data:
          m = Media.objects.get(id=medium["id"])
          try:
            m = Media.objects.get(id=medium["id"])
            m.link = medium["domain"]
            m.save()
          except:
            print("Not found: ", medium)
            m = Media(name=medium["name"], link=medium["domain"])
            m.save()

