from django.core.cache import cache
from django.core.management import BaseCommand, call_command
from django.db.models import Count
from django.template.loader import render_to_string
from django.conf import settings

from eventregistry import *

import constants
from news.models import Article, Event, Medium, Newsletter

from datetime import datetime, timedelta

class Command(BaseCommand):
    @staticmethod
    def get_locale_date(date):
        days_map = {
            'Monday': 'ponedeljak',
            'Tuesday': 'utorak',
            'Wednesday': 'srijeda',
            'Thursday': 'četvrtak',
            'Friday': 'petak',
            'Saturday': 'subota',
            'Sunday': 'nedjelja'
        }

        day = days_map.get(date.strftime('%A'), 'ERROR')

        return f'{day}, {date.strftime("%d. %m.")}'

    def handle(self, *args, **options):
        newsletter = Newsletter.objects.filter(
            sent=False
        ).order_by(
            '-date'
        ).first()
        if not newsletter:
            print('YOU NEED TO SET UP A NEWSLETTER MOFO!')
        if not newsletter.events.count():
            print('YOU NEED EVENTS MOFO!')
            return

        # initialize context
        context = {}

        # header data
        context['date'] = newsletter.date.strftime('%-d. %-m. %Y')

        context['title'] = 'Newsgradient'
        context['subtitle'] = 'Pregled sedmice'
        context['page_link_label'] = 'Newsgradient'
        context['page_link_url'] = 'https://newsgradient-pwa.lb.djnd.si'

        # misc
        context['articles_slant_1'] = 'Najpopularniji clanak iz lijevo orientisanih medija'
        context['articles_slant_2'] = 'Najpopularniji clanak iz neutralnih medija'
        context['articles_slant_3'] = 'Najpopularniji clanak iz desno orientisanih medija'
        context['read_more'] = 'Pročitaj više'
        context['media_title'] = 'Pogledaj kako su mediji izvještavali o događaju.'
        context['media_slant_1'] = 'lijevo orientisani mediji'
        context['media_slant_2'] = 'neutralni mediji'
        context['media_slant_3'] = 'desno orientisani mediji'
        context['social_media_share'] = 'Deli na društvenim mrežama'
        context['unsubscribe'] = 'Ako se želiš odjaviti od ovog newslettera klikni ovde.'
        context['download_app'] = 'Preuzmi Android aplikaciju Newsgradient.'

        events = newsletter.events.select_related(
            'articles'
        ).annotate(
            all_articles_count=Count('articles')
        ).values(
            'uri',
            'title',
            'all_articles_count',
            'date'
        ).order_by(
            '-all_articles_count'
        )

        def articles_for_event_slant(event, slant):
            return Article.objects \
                .select_related('medium') \
                .annotate(social_score=Count('tweets')) \
                .values('url', 'image', 'title', 'medium__title', 'social_score') \
                .filter(event_id=event.get('uri'), medium__slant=slant) \
                .order_by('-medium__reliability')

        # events
        context['events'] = [{
            'title': event.get('title', ''),
            'date': self.get_locale_date(event.get('date', datetime.today())),
            'uri': event.get('uri', ''),
            'articles_slant_1': [article for article in articles_for_event_slant(event, 1)[:1]],
            'articles_slant_3': [article for article in articles_for_event_slant(event, 3)[:1]],
            'all_articles_slant_1': [article for article in articles_for_event_slant(event, 1)],
            'all_articles_slant_2': [article for article in articles_for_event_slant(event, 2)],
            'all_articles_slant_3': [article for article in articles_for_event_slant(event, 3)],
        } for event in events]

        html_content = render_to_string('newsletter.html', context=context).strip()

        if settings.MAUTIC_SECRET:
            response = requests.post(
                'https://podpri.lb.djnd.si/api/create-and-send-custom-email/',
                headers={'Authorization': settings.MAUTIC_SECRET},
                json={
                    'title': f'{context["title"]} {context["subtitle"]} {context["date"]}',
                    'description': f'{context["title"]} {context["subtitle"]} {context["date"]}',
                    'content': html_content,
                    'segments': [20],
                    'fromName': 'Newsgradient'
                },
            )
            print('Newsletter submitted, API response follows:')
            print(response.text)

            newsletter.sent = True
            newsletter.save()

            new_newsletter = Newsletter(
                date=newsletter.date + timedelta(days=7)
            )
            new_newsletter.save()
        else:
            print('Missing MAUTIC_SECRET.')
