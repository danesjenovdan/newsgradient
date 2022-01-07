import typing
import requests
import json
from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.core.cache import cache
from django.db.models import Count
from django.db.models import F
from django.db.models import FloatField
from django.db.models import Q
from django.db.models.functions import Cast
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from common.views import SuperAPIView
from constants import CacheKeys
from constants import TimeRange
from constants import Orientations
from news import models
from news import serializers
from news.schemas import EventArticlesSchema
from news.schemas import EventSchema
from news.schemas import TopEventQPSchema
from news.services import get_event
from news.services import get_event_articles
from news.services import get_most_popular_events_with_articles


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    #filter_fields = ('is_visible',)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = (AllowAny,)
        else:
            self.permission_classes = (IsAuthenticated,)
        return super(EventViewSet, self).get_permissions()

    def get_queryset(self):
        time_range = self.request.GET.get('range', 'all')
        slant = self.request.GET.get('slant', 'all')

        # get all events and annotate field count of articles per event
        events = models.Event.objects.all().annotate(
            all_count=Cast(
                Count(
                    'articles',
                    filter=Q(articles__medium__slant__isnull=False),
                    distinct=True
                ),
                FloatField()
            )
        )

        if time_range == TimeRange.TODAY:
            events = events.filter(date=datetime.today())
        if time_range == TimeRange.YESTERDAY:
            events = events.filter(date=datetime.today() - timedelta(days=1))
        if time_range == TimeRange.LAST_WEEK:
            events = events.filter(date__gte=datetime.today() - timedelta(days=7))
        if time_range == TimeRange.LAST_MONTH:
            events = events.filter(date__gte=datetime.today() - timedelta(days=30))
        else:
            events = events.all()

        if slant == 'all':
            return events.exclude(articles__isnull=True).annotate(
                this_count=Cast(
                    Count(
                        'articles'
                    ),
                    FloatField()
                )
            ).order_by('-all_count')
        else:
            events = events.filter(articles__medium__slant=slant)
            # annotate field count of articles of this slant per event and returns orderd queryset
            return events.annotate(
                this_count=Cast(
                    Count(
                        'articles',
                        filter=Q(articles__medium__slant=slant),
                        distinct=True
                    ),
                    FloatField()
                )
            ).annotate(ordering=F('this_count') / F('all_count')).order_by('-ordering')


class ArticleView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, event_id):
        cache_key = f'{CacheKeys.EVENT_ARTICLES}::{event_id}'
        cached_value = cache.get(cache_key)
        if not cached_value:
            service_response: typing.List[typing.Dict] = get_event_articles(event_id)
            schema = EventArticlesSchema()
            data = schema.dump(service_response)
            cache.set(cache_key, data)
            return Response(data)
        return Response(cached_value)


class TopEventsView(SuperAPIView):
    permission_classes = (AllowAny,)
    qp_schema = TopEventQPSchema

    def get(self, request):
        # time_range = self.cleaned_qp.get('timerange')
        slant = self.cleaned_qp.get('slant')
        if slant is None:
            slant = Orientations.NEUTRAL.value

        cache_key = f'{CacheKeys.TOP_EVENTS}::{slant}'
        cached_value = cache.get(cache_key)
        if not cached_value:
            events: typing.List[typing.Dict] = get_most_popular_events_with_articles(slant)
            schema = EventSchema(many=True)
            data = schema.dump(events)
            cache.set(cache_key, data)
            return Response(data)
        return Response(cached_value)

        # events: typing.List[typing.Dict] = get_most_popular_events_with_articles(slant)
        # schema = EventSchema(many=True)
        # data = schema.dump(events)
        # return Response(data)


class EventDetailView(APIView):
    permission_classes = (AllowAny,)
    qp_schema = TopEventQPSchema

    def get(self, request, event_id):
        event: typing.Dict = get_event(event_id)
        schema = EventSchema()
        data = schema.dump(event)
        return Response(data)


class NewsletterApiView(APIView):
    permission_classes = (AllowAny,)

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

    def get(self, request):
        events = models.Event.objects \
            .select_related('articles') \
            .annotate(all_articles_count=Count('articles')) \
            .values('uri', 'title', 'all_articles_count', 'date') \
            .filter(is_promoted=True) \
            .order_by('-all_articles_count')

        def articles_for_event_slant(event, slant):
            return models.Article.objects \
                .select_related('medium') \
                .annotate(social_score=Count('tweets')) \
                .values('url', 'image', 'title', 'medium__title', 'social_score') \
                .filter(event_id=event.get('uri'), medium__slant=slant) \
                .order_by('-medium__reliability')

        # events
        eventsData = [{
            'title': event.get('title', ''),
            'date': self.get_locale_date(event.get('date', datetime.today())),
            'uri': event.get('uri', ''),
            'articles_slant_1': [article for article in articles_for_event_slant(event, 1)[:1]],
            'articles_slant_3': [article for article in articles_for_event_slant(event, 3)[:1]],
            'all_articles_slant_1': [article for article in articles_for_event_slant(event, 1)],
            'all_articles_slant_2': [article for article in articles_for_event_slant(event, 2)],
            'all_articles_slant_3': [article for article in articles_for_event_slant(event, 3)],
        } for event in events]

        return Response(eventsData)


class NewsletterView(TemplateView):
    template_name = "newsletter.html"

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # header data
        context['date'] = datetime.today().strftime('%-d. %-m. %Y')

        context['title'] = 'Newsgradient'
        context['subtitle'] = 'Pregled sedmice'
        context['page_link_label'] = 'Newsgradient'
        context['page_link_url'] = 'https://newsgradient.org'

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

        events = models.Event.objects \
            .select_related('articles') \
            .annotate(all_articles_count=Count('articles')) \
            .values('uri', 'title', 'all_articles_count', 'date') \
            .filter(is_promoted=True) \
            .order_by('-all_articles_count')

        def articles_for_event_slant(event, slant):
            return models.Article.objects \
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

        # html_content = render_to_string('newsletter.html', context=context).strip()

        # send_mail = True
        # if send_mail and settings.MAUTIC_SECRET:
        #     response = requests.post(
        #         'https://podpri.djnd.si/api/create-and-send-custom-email/',
        #         headers={'Authorization': settings.MAUTIC_SECRET},
        #         json={
        #             'title': f'{context["title"]} {context["subtitle"]} {context["date"]}',
        #             'description': f'{context["title"]} {context["subtitle"]} {context["date"]}',
        #             'content': html_content,
        #             'segments': [19]
        #         },
        #     )
        #     print(response.text)

        # print(html_content)

        return context
