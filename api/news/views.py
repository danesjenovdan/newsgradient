import typing
from datetime import datetime
from datetime import timedelta

from django.core.cache import cache
from django.db.models import Count
from django.db.models import F
from django.db.models import FloatField
from django.db.models import Q
from django.db.models.functions import Cast
from django.views.generic import TemplateView
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


class NewsletterView(TemplateView):
    template_name = "newsletter.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # header data
        context['date'] = '16. 7. 2021'
        context['title_image_url'] = 'https://newsgradient.org/_nuxt/img/logo-text.cbd59f5.svg' # TODO: use data url
        context['title'] = 'Newsgradient'
        context['subtitle'] = 'Obvestilnik'
        context['page_link_label'] = 'Newsgradient'
        context['page_link_url'] = 'https://newsgradient.org'

        # misc
        context['articles_slant_1'] = 'Najpopularniji clanak iz lijevo orientisanih medija'
        context['articles_slant_2'] = 'Najpopularniji clanak iz neutralnih medija'
        context['articles_slant_3'] = 'Najpopularniji clanak iz desno orientisanih medija'
        context['read_more'] = 'Pročitaj više'
        context['media_title'] = 'Koji su mediji pisali o dogadaju?'
        context['media_slant_1'] = 'lijevo orientisani mediji'
        context['media_slant_2'] = 'neutralni mediji'
        context['media_slant_3'] = 'desno orientisani mediji'
        context['social_media_share'] = 'Deli na društvenim mrežama'
        context['unsubscribe'] = 'Ako se želiš odjaviti od ovog newslettera klikni ovde.'

        # events
        context['events'] = [
            {
                'title': 'Sindikalna potrošačka korpa u FBiH u julu premašila dvije hiljade KM',
                'articles_slant_1': [
                    {
                        "content": "Biznis\n\nSavez samostalnih sindikata Mrvice za sirotinju, obilje za vlast i njene poltrone: Potrošačka korpa premašila 2.000 KM Prije 10m\n\nPokrivenost Sindikalne potrošačke korpe prosječnom platom je 47,42 posto\n\nSindikalna potrošačka korpa koju je Savez samostalnih sindikata Bosne i Hercegovine izračunao za juli ove godine iznosi 2.070,79 KM i za 27,45 KM je skuplja od potrošačke korpe za prethodni mjesec, javlja Anadolu Agency (AA).\n\nProsječna plata isplaćena u bosanskohercegovačkom entitetu Federacija BiH za maj iznosila je 982 KM (posljednji podatak Federalnog zavoda za statistiku) i za osam KM je niža od iznosa u prethodnom mjesecu.\n\nPokrivenost Sindikalne potrošačke korpe prosječnom platom je 47,42 posto.\n\nPrilikom izrade Sindikalne potrošačke korpe uzeta je u obzir prosječna plata isplaćena u Federaciji BiH te minimalni troškovi života četveročlane porodice koju čine dvije odrasle osobe i dvoje djece- jedno u srednjoškolskom, a drugo u uzrastu osnovca.\n\nPotrošačku korpu čine kategorije: prehrana (44,2 posto), stanovanje i komunalne usluge (15 posto), higijena i održavanje zdravlja (6,6 posto), obrazovanje i kultura (5,8 posto), odjeća i obuća (14,5 posto), prijevoz (6,7 posto) i održavanje domaćinstva (7,2 posto).\n\nU kategoriji prehrana korištene su cijene iz tri trgovačka centra za 86 artikala. Kada je riječ o higijeni i održavanju zdravlja, ubrojani su troškovi za dvanaest stavki, a za stanovanje i komunalne usluge troškovi za šest stavki.\n\nKomentari #potrošačka korpa Vezane vijesti Kako uopšte preživljavamo: Potrošačka korpa u junu iznosila više od 2.000 KM Sindikalna potrošačka korpa iznosi više od 2.000 KM Potrošačka korpa sada iznosi čak 2.083 KM, prosječna plata ne može je napuniti ni do pola",
                        "datetime": "2021-08-12T07:27:00+00:00",
                        "url": "https://www.fokus.ba/biznis/mrvice-za-sirotinju-obilje-za-vlast-i-njene-poltrone-potrosacka-korpa-premasila-2-000-km/2126229/",
                        "title": "Mrvice za sirotinju, obilje za vlast i njene poltrone: Potrošačka korpa premašila 2.000 KM",
                        "medium": {
                            "favicon": "None",
                            "title": "Fokus",
                            "uri": "fokus.ba",
                            "slant": "1"
                        },
                        "id": "6685116906",
                        "image": "https://www.fokus.ba/wp-content/uploads/2019/12/potrosacka-korpa-1.jpg",
                        "social_score": 0,
                    },
                ],
                'articles_slant_2': [],
                'articles_slant_3': [
                    {
                        "content": "Prilikom izrade sindikalne potrošačke korpe u obzir je uzeta prosječna plata isplaćena u Federaciji BiH, te minimalni troškovi života četveročlane porodice koju čine dvije odrasle osobe i dva djeteta, od kojih je jedno u srednjoškolskom, a drugo u uzrastu osnovca.\n\nPotrošačku korpu čine - prehrana (44,2 posto učešće u sindikalnoj potrošačkoj korpi), stanovanje i komunalne usluge (15 posto), higijena i održavanje zdravlja (6,6 posto), obrazovanje i kultura (5,8 posto), odjeća i obuća (14,5 posto), prijevoz (6,7 posto), te održavanje domaćinstva (7,2 posto).\n\nU kategoriji 'prehrana' korištene su cijene iz tri trgovačka centra za 86 artikala. Kada je riječ o higijeni i održavanju zdravlja ubrojani su troškovi za 12 stavki, a za stanovanje i komunalne usluge troškovi za šest stavki, saopćeno je iz Službe za informisanje SSSBiH.\n\n(FENA)",
                        "datetime": "2021-08-12T07:59:00+00:00",
                        "url": "http://www.source.ba/clanak/Ekonomija/575925/fb",
                        "title": "Source.ba:Sindikalna potrošačka korpa za BiH u julu 2.070,79 KM",
                        "medium": {
                            "favicon": "None",
                            "title": "Source",
                            "uri": "source.ba",
                            "slant": "3"
                        },
                        "id": "6685149445",
                        "image": "http://www.source.ba/local_files/pocetneSlike/0a8500cba03d49feac4595df35cb48be.jpg",
                        "social_score": 0
                    },
                ],
                'article_urls_slant_1': [
                    "https://www.fokus.ba/biznis/mrvice-za-sirotinju-obilje-za-vlast-i-njene-poltrone-potrosacka-korpa-premasila-2-000-km/2126229/",
                    "https://www.rtvusk.ba/vijest/za-sindikalnu-potrosacku-korpu-u-federaciji-bih-nisu-dovoljne-ni-dvije-prosjecne-plate/51322",
                    "https://www.klix.ba/biznis/privreda/za-sindikalnu-potrosacku-korpu-u-federaciji-bih-nisu-dovoljne-ni-dvije-prosjecne-plate/210812028",
                ],
                'article_urls_slant_2': [
                    "http://www.source.ba/clanak/Ekonomija/575925/fb"
                ],
                'article_urls_slant_3': [1,2,3,4,5,6,7,8,9,10],
            },
            {
                'title': 'Ko se pored Milorada Dodika može naći na udaru novog zakona o zabrani negiranja genocida',
                'articles_slant_1': [
                    {
                        "content": "Biznis\n\nSavez samostalnih sindikata Mrvice za sirotinju, obilje za vlast i njene poltrone: Potrošačka korpa premašila 2.000 KM Prije 10m\n\nPokrivenost Sindikalne potrošačke korpe prosječnom platom je 47,42 posto\n\nSindikalna potrošačka korpa koju je Savez samostalnih sindikata Bosne i Hercegovine izračunao za juli ove godine iznosi 2.070,79 KM i za 27,45 KM je skuplja od potrošačke korpe za prethodni mjesec, javlja Anadolu Agency (AA).\n\nProsječna plata isplaćena u bosanskohercegovačkom entitetu Federacija BiH za maj iznosila je 982 KM (posljednji podatak Federalnog zavoda za statistiku) i za osam KM je niža od iznosa u prethodnom mjesecu.\n\nPokrivenost Sindikalne potrošačke korpe prosječnom platom je 47,42 posto.\n\nPrilikom izrade Sindikalne potrošačke korpe uzeta je u obzir prosječna plata isplaćena u Federaciji BiH te minimalni troškovi života četveročlane porodice koju čine dvije odrasle osobe i dvoje djece- jedno u srednjoškolskom, a drugo u uzrastu osnovca.\n\nPotrošačku korpu čine kategorije: prehrana (44,2 posto), stanovanje i komunalne usluge (15 posto), higijena i održavanje zdravlja (6,6 posto), obrazovanje i kultura (5,8 posto), odjeća i obuća (14,5 posto), prijevoz (6,7 posto) i održavanje domaćinstva (7,2 posto).\n\nU kategoriji prehrana korištene su cijene iz tri trgovačka centra za 86 artikala. Kada je riječ o higijeni i održavanju zdravlja, ubrojani su troškovi za dvanaest stavki, a za stanovanje i komunalne usluge troškovi za šest stavki.\n\nKomentari #potrošačka korpa Vezane vijesti Kako uopšte preživljavamo: Potrošačka korpa u junu iznosila više od 2.000 KM Sindikalna potrošačka korpa iznosi više od 2.000 KM Potrošačka korpa sada iznosi čak 2.083 KM, prosječna plata ne može je napuniti ni do pola",
                        "datetime": "2021-08-12T07:27:00+00:00",
                        "url": "https://www.fokus.ba/biznis/mrvice-za-sirotinju-obilje-za-vlast-i-njene-poltrone-potrosacka-korpa-premasila-2-000-km/2126229/",
                        "title": "Mrvice za sirotinju, obilje za vlast i njene poltrone: Potrošačka korpa premašila 2.000 KM",
                        "medium": {
                            "favicon": "None",
                            "title": "Fokus",
                            "uri": "fokus.ba",
                            "slant": "1"
                        },
                        "id": "6685116906",
                        "image": "https://www.fokus.ba/wp-content/uploads/2019/12/potrosacka-korpa-1.jpg",
                        "social_score": 0,
                    },
                ],
                'articles_slant_2': [],
                'articles_slant_3': [
                    {
                        "content": "Prilikom izrade sindikalne potrošačke korpe u obzir je uzeta prosječna plata isplaćena u Federaciji BiH, te minimalni troškovi života četveročlane porodice koju čine dvije odrasle osobe i dva djeteta, od kojih je jedno u srednjoškolskom, a drugo u uzrastu osnovca.\n\nPotrošačku korpu čine - prehrana (44,2 posto učešće u sindikalnoj potrošačkoj korpi), stanovanje i komunalne usluge (15 posto), higijena i održavanje zdravlja (6,6 posto), obrazovanje i kultura (5,8 posto), odjeća i obuća (14,5 posto), prijevoz (6,7 posto), te održavanje domaćinstva (7,2 posto).\n\nU kategoriji 'prehrana' korištene su cijene iz tri trgovačka centra za 86 artikala. Kada je riječ o higijeni i održavanju zdravlja ubrojani su troškovi za 12 stavki, a za stanovanje i komunalne usluge troškovi za šest stavki, saopćeno je iz Službe za informisanje SSSBiH.\n\n(FENA)",
                        "datetime": "2021-08-12T07:59:00+00:00",
                        "url": "http://www.source.ba/clanak/Ekonomija/575925/fb",
                        "title": "Source.ba:Sindikalna potrošačka korpa za BiH u julu 2.070,79 KM",
                        "medium": {
                            "favicon": "None",
                            "title": "Source",
                            "uri": "source.ba",
                            "slant": "3"
                        },
                        "id": "6685149445",
                        "image": "http://www.source.ba/local_files/pocetneSlike/0a8500cba03d49feac4595df35cb48be.jpg",
                        "social_score": 0
                    },
                ],
            },
        ]

        return context


# html_content = render_to_string('reports/email.html', context=context).strip()
