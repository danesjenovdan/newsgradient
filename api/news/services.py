from datetime import datetime

from django.db.models import Count
from django.db.models import Q
from rest_framework.exceptions import NotFound

from constants import Orientations
from news.models import Article
from news.models import Event
from news.models import Medium
from news.models import Tweet


def get_most_popular_events_with_articles(slant: int = Orientations.NEUTRAL):
    mediums = {medium.get('id'): medium for medium in Medium.objects.all().values()}

    promoted_events = Event.objects \
        .select_related('articles') \
        .annotate(all_articles_count=Count('articles')) \
        .values('uri', 'title', 'date', 'all_articles_count') \
        .filter(is_promoted=True) \
        .order_by('-all_articles_count')

    final_events = list(promoted_events)
    for event in final_events:
        articles = Article.objects.select_related('medium') \
                       .filter(event_id=event.get('uri'), medium__slant=slant) \
                       .order_by('-medium__reliability')
        articles_for_output = []
        for article in articles:
            article_for_output = {
                'uri': article.uri,
                'url': article.url,
                'title': article.title,
                'content': article.content,
                'image': article.image,
                'datetime': article.datetime,
                'medium_id': article.medium.id,
            }
            article_for_output['medium'] = mediums.get(article.medium.id)
            event['image'] = article.image if article.image else None
            article_for_output['social_score'] = article.tweets.count()
            articles_for_output.append(article_for_output)
        event['articles'] = articles_for_output[:3]
        event['articles_count'] = articles.count()
        event['social_score'] = Tweet.objects.filter(article__event=event.get('uri')).count()
        if len(articles):
            d = datetime.utcnow() - articles[0].datetime.replace(tzinfo=None)
            hours = int(d.total_seconds() // 3600)
            if hours <= 1:
                event['first_publish'] = f'Prije sat vremena'
            elif 1 < hours <= 2:
                event['first_publish'] = f'Prije dva sata'
            elif 2 < hours <= 3:
                event['first_publish'] = f'Prije tri sata'
            elif 3 < hours <= 5:
                event['first_publish'] = f'Prije pet sati'
            elif 5 < hours <= 24:
                event['first_publish'] = f'Danas'
            elif 24 < hours <= 48:
                event['first_publish'] = f'Jučer'
            elif 48 < hours <= 72:
                event['first_publish'] = f'Prije dva dana'
            elif 72 < hours <= 96:
                event['first_publish'] = f'Prije tri dana'
            elif 96 < hours <= 120:
                event['first_publish'] = f'Prije četiri dana'
            elif 120 < hours <= 144:
                event['first_publish'] = f'Prije pet dana'
            elif hours > 144:
                event['first_publish'] = f'Prije više od pet dana'

    return final_events

def get_most_popular_events_with_filtered_articles(
        positive_party_scores,
        negative_party_scores,
        locations
    ):
    if positive_party_scores or negative_party_scores or locations:
        if positive_party_scores or negative_party_scores:
            mediums_qs = Medium.objects.filter(
                Q(partymediumscore__score__lt=0,
                partymediumscore__party__in=negative_party_scores) |
                Q(partymediumscore__score__gt=0,
                partymediumscore__party__in=positive_party_scores)
            )
        else:
            mediums_qs = Medium.objects.all()
        # print(mediums_qs)
        # print(locations)
        if locations:
            mediums_qs = mediums_qs.filter(location__in=locations)
        # print(mediums_qs)
        mediums = {medium.get('id'): medium for medium in  mediums_qs.values()}
    else:
        mediums = {medium.get('id'): medium for medium in Medium.objects.all().values()}
    # print(mediums)

    promoted_events = Event.objects \
        .select_related('articles') \
        .annotate(all_articles_count=Count('articles')) \
        .values('uri', 'title', 'date', 'all_articles_count') \
        .filter(is_promoted=True) \
        .order_by('-all_articles_count')

    final_events = list(promoted_events)
    for event in final_events:
        articles = Article.objects.select_related('medium') \
                       .filter(event_id=event.get('uri'), medium_id__in=list(mediums.keys())) \
                       .order_by('-medium__reliability')
        articles_for_output = []
        for article in articles:
            article_for_output = {
                'uri': article.uri,
                'url': article.url,
                'title': article.title,
                'content': article.content,
                'image': article.image,
                'datetime': article.datetime,
                'medium_id': article.medium.id,
            }
            article_for_output['medium'] = mediums.get(article.medium.id)
            event['image'] = article.image if article.image else None
            article_for_output['social_score'] = article.tweets.count()
            articles_for_output.append(article_for_output)
        event['articles'] = articles_for_output[:3]
        event['articles_count'] = articles.count()
        event['social_score'] = Tweet.objects.filter(article__event=event.get('uri')).count()
        if len(articles):
            d = datetime.utcnow() - articles[0].datetime.replace(tzinfo=None)
            hours = int(d.total_seconds() // 3600)
            if hours <= 1:
                event['first_publish'] = f'Prije sat vremena'
            elif 1 < hours <= 2:
                event['first_publish'] = f'Prije dva sata'
            elif 2 < hours <= 3:
                event['first_publish'] = f'Prije tri sata'
            elif 3 < hours <= 5:
                event['first_publish'] = f'Prije pet sati'
            elif 5 < hours <= 24:
                event['first_publish'] = f'Danas'
            elif 24 < hours <= 48:
                event['first_publish'] = f'Jučer'
            elif 48 < hours <= 72:
                event['first_publish'] = f'Prije dva dana'
            elif 72 < hours <= 96:
                event['first_publish'] = f'Prije tri dana'
            elif 96 < hours <= 120:
                event['first_publish'] = f'Prije četiri dana'
            elif 120 < hours <= 144:
                event['first_publish'] = f'Prije pet dana'
            elif hours > 144:
                event['first_publish'] = f'Prije više od pet dana'

    return final_events

def get_event_articles(event_uri):
    try:
        event = Event.objects.values('title', 'description', 'og_image_article').get(uri=event_uri)
    except Event.DoesNotExist:
        raise NotFound
    mediums = {medium.get('id'): medium for medium in Medium.objects.all().values()}
    articles = Article.objects.select_related('medium').filter(event_id=event_uri).annotate(social_score=Count('tweets')).values()
    for article in articles:
        article['medium'] = mediums.get(article.get('medium_id'))

    og_image = None
    if event.get('og_image_article'):
        og_image_article = Article.objects.values('image').get(uri=event.get('og_image_article'))
        og_image = og_image_article.get('image')

    data = {
        'title': event.get('title'),
        'description': event.get('description'),
        'og_image': og_image,
        'articles': list(articles)
    }
    return data

def get_event_filtered_articles(
        event_uri,
        positive_party_scores,
        negative_party_scores,
        locations
    ):
    try:
        event = Event.objects.values('title', 'description', 'og_image_article').get(uri=event_uri)
    except Event.DoesNotExist:
        raise NotFound

    if positive_party_scores or negative_party_scores or locations:
        if positive_party_scores or negative_party_scores:
            mediums_qs = Medium.objects.filter(
                Q(partymediumscore__score__lt=0,
                partymediumscore__party__in=negative_party_scores) |
                Q(partymediumscore__score__gt=0,
                partymediumscore__party__in=positive_party_scores)
            )
        else:
            mediums_qs = Medium.objects.all()
        # print(mediums_qs)
        # print(locations)
        if locations:
            mediums_qs = mediums_qs.filter(location__in=locations)
        # print(mediums_qs)
        mediums = {medium.get('id'): medium for medium in  mediums_qs.values()}
    else:
        mediums = {medium.get('id'): medium for medium in Medium.objects.all().values()}
    # print(mediums)

    articles = Article.objects.select_related('medium').filter(event_id=event_uri, medium_id__in=list(mediums.keys())).annotate(social_score=Count('tweets')).values()
    for article in articles:
        article['medium'] = mediums.get(article.get('medium_id'))

    og_image = None
    if event.get('og_image_article'):
        og_image_article = Article.objects.values('image').get(uri=event.get('og_image_article'))
        og_image = og_image_article.get('image')

    data = {
        'title': event.get('title'),
        'description': event.get('description'),
        'og_image': og_image,
        'articles': list(articles)
    }
    return data


def get_event(event_uri):
    try:
        return Event.objects.defer('updated_at', 'is_promoted', 'sentiment', 'wgt') \
            .values() \
            .get(uri=event_uri)
    except Event.DoesNotExist:
        raise NotFound


def determine_slant_from_bias(bias: float) -> Orientations:
    if bias < -3:
        return Orientations.LEFT
    if bias > 3:
        return Orientations.RIGHT
    return Orientations.NEUTRAL
