from analize.models import Media, News, Party

from django.core.management.base import BaseCommand
from django.db.models import Q
from datetime import datetime

import os
import csv


class Command(BaseCommand):
    help = 'Export news'

    def handle(self, *args, **options):
        search_strings = options['search_strings']
        media = Media.objects.all()
        parties = Party.objects.all()

        for medium in media:
            print(medium)
            for party in parties:
                search_strings = party.get_search_terms()
                q_news_objects = Q()
                for search_string in search_strings:
                    q_news_objects.add(
                        Q(content__contains=search_string),
                        Q.OR
                    )
                articles = medium.news.filter(q_news_objects)
                if articles:
                    self.write_file(articles, medium.name, f'{party.name}_{medium.name}_sample.csv')

    def write_file(self, articles, folder, file_name):
        os.makedirs(f'exports', exist_ok=True)
        os.makedirs(f'exports/{folder}', exist_ok=True)
        file_path = f'exports/{folder}/{file_name}'
        with open(file_path, 'w', newline='') as outfile:
            csvwriter = csv.writer(outfile, delimiter=',',
                quotechar='"', quoting=csv.QUOTE_MINIMAL)

            csvwriter.writerow(['id', 'medij', 'naslov', 'link', 'datum', 'naslovnica'])
            for article in articles:
                csvwriter.writerow([
                    str(article.id),
                    article.media.name,
                    article.title,
                    article.link,
                    article.parsed_at.strftime('%Y-%m-%d'),
                    str(True),
                ])

