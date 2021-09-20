from django.core.cache import cache
from django.core.management import BaseCommand, call_command
from eventregistry import *

import constants
from news.models import Article
from news.models import Event
from news.models import Medium

import datetime
import os
import traceback


def get_medium_uris():
    mediums = Medium.objects.all()
    return [medium.uri for medium in mediums]
    # return {medium.uri: medium.id for medium in mediums}


class Command(BaseCommand):
    def handle(self, *args, **options):
        if cache.get(constants.NEW_ARTICLES_FETCH_KEY) == constants.CommandStatus.RUNNING.value:
            self.stderr.write('Command already running!')
            return
        try:
            cache.set(constants.NEW_ARTICLES_FETCH_KEY, constants.CommandStatus.RUNNING.value)
            self.handle_impl()
            #call_command('update_event_uris')
            call_command('clear_cache')
        except Exception as e:
            self.stderr.write(f'Exception: {e}')
            traceback.print_exc()
        cache.set(constants.NEW_ARTICLES_FETCH_KEY, constants.CommandStatus.IDLE.value)

    def handle_impl(self):
        key = os.getenv('ER_API_KEY')
        er = EventRegistry(apiKey=key)
        self.stdout.write('-' * 80)

        medium_uris = get_medium_uris()
        self.stdout.write(f'Medium URIs: {medium_uris}')
        self.stdout.write('-' * 80)

        q = QueryArticlesIter(
            sourceUri=QueryItems.OR(medium_uris),
            lang=QueryItems.OR(['hrv', 'srp']),
            dateStart=datetime.datetime.now() - datetime.timedelta(days=1),
            isDuplicateFilter='skipDuplicates',
        )

        results = q.execQuery(
            er,
            sortBy="date"
            # maxItems=10,
        )

        newEventsCount = 0
        newArticlesCount = 0

        for article in results:
            articleUrl = article.get('url', '')
            if 'index.hr/oglasi' in articleUrl:
                continue

            articleUri = article.get('uri', '')
            if Article.objects.filter(uri=articleUri).exists():
                continue

            mediumUri = article.get('source', {}).get('uri')
            medium = Medium.objects.filter(uri=mediumUri).first()
            if not medium:
                continue

            eventUri = article.get('eventUri', '')
            articleTitle = article.get('title', '')
            articleImage = article.get('image', '')
            articleBody = article.get('body', '')
            articleDateTime = article.get('dateTime', None)

            if eventUri and not Event.objects.filter(uri=eventUri).exists() and articleDateTime and articleTitle:
                Event.objects.create(
                    uri=eventUri,
                    title=articleTitle,
                    date=articleDateTime.split('T')[0]
                )
                newEventsCount += 1
            else:
                print('Skip adding event', articleTitle, articleDateTime)

            Article.objects.create(
                uri=articleUri,
                title=articleTitle,
                content=articleBody,
                url=articleUrl,
                datetime=articleDateTime,
                image=articleImage,
                event_id=eventUri,
                medium=medium,
            )
            self.stdout.write(f'NEW ARTICLE: {articleUri} - {articleTitle}')
            newArticlesCount += 1

            self.stdout.write('-' * 80)

        self.stdout.write('-' * 80)
        self.stdout.write(f'+ new events:   {newEventsCount}')
        self.stdout.write(f'+ new articles: {newArticlesCount}')
        self.stdout.write('-' * 80)
        self.stdout.write('+ DONE')
        self.stdout.write('-' * 80)
