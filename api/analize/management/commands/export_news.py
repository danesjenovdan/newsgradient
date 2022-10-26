from analize.models import Media, News, Party

from django.core.management.base import BaseCommand
from django.db.models import Q
from datetime import datetime

import os
import csv


class Command(BaseCommand):
    help = 'Export news'

    @staticmethod
    def filter_article(article):
        # filter severina
        if 'Severina' in article.content:
            return False
        if 'GSS' in article.content:
            return False
        if 'KCUS' in article.content:
            return False
        return True

    def handle(self, *args, **options):
        media = Media.objects.all()
        # media = Media.objects.filter(name="klix")
        parties = Party.objects.all()
        all_articles = []

        for medium in media:
            print(medium)
            for party in parties:
                search_strings = party.get_search_terms()
                q_news_objects = Q()
                for search_string in search_strings:
                    pattern = ''
                    if len(search_string.strip().split(' ')) > 1:
                        # print('#######')
                        # print(search_string)
                        for ss in search_string.strip().split(' '):
                            pattern += f'{ss}% '
                    else:
                        pattern = search_string
                    q_news_objects.add(
                        Q(content__contains=pattern.strip()),
                        Q.OR
                    )
                    # print(pattern.strip())
                    # if search_string.isupper():
                    #     # exact word matching for allcaps words (acronyms)
                    #     # contains
                    #     search_q_object = Q(content__contains=search_string)
                    # else:
                    #     # query each word from parser name
                    #     # icontains
                    #     # TODO - če je ime in priimek, iščemo samo priimek
                    #     # TODO - isto se dogaja s strankami, mora biti celo ime, ne samo ena beseda
                    #     search_q_object = Q()
                    #     sub_strings = search_string.split(' ')[1:]
                    #     for sub_string in sub_strings:
                    #         search_q_object.add(
                    #             Q(content__contains=sub_string),
                    #             Q.AND
                    #         )

                    # q_news_objects.add(
                    #     search_q_object,
                    #     Q.OR
                    # )
                
                # q_news_objects.add(
                #     Q(published_at__date=datetime.strptime('2022-09-10', '%Y-%m-%d')),
                #     Q.AND
                # )
                articles = medium.news.filter(
                    q_news_objects
                )
                if articles:
                    filtered_articles = list(filter(self.filter_article, articles))
                    self.write_file(filtered_articles, medium.name, f'{party.name}_{medium.name}.csv')
                    all_articles += filtered_articles

        print(len(all_articles))

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
