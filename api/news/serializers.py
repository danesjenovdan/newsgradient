import random
from collections import Counter

from rest_framework import serializers

from news import models


class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medium
        fields = ['title', 'slant', 'favicon', 'is_embeddable']


class EventSerializer(serializers.ModelSerializer):
    # count = serializers.SerializerMethodField()
    # computed_time = serializers.SerializerMethodField()

    # counter = serializers.SerializerMethodField()
    # wgt = serializers.SerializerMethodField()
    # first_article = serializers.SerializerMethodField()
    # most = serializers.SerializerMethodField()
    social_score = serializers.SerializerMethodField()
    class Meta:
        model = models.Event
        fields = [
            'uri',
            'title',
            'summary',
            'date',
            'social_score',
            # 'computed_time',
            # 'count',
            # 'is_visible',
            # 'counter',
            # 'first_article',
            # 'most',
            # 'wgt',
        ]

    def get_count(self, obj):
        return obj.articles.exclude(medium__slant=None).count()

    def get_computed_time(self, obj):
        return obj.articles.earliest("datetime").datetime

    def get_counter(self, obj):
        all_articles = obj.articles.exclude(medium__slant=None)
        slants = all_articles.values_list('medium__slant', flat=True)
        all_count = all_articles.count()
        data = dict(Counter(slants))
        data.update({'total': all_count})
        return data

    def get_most(self, obj):
        all_articles = obj.articles.exclude(medium__slant=None)
        positive = all_articles.latest("sentiment")
        negative = all_articles.earliest("sentiment")
        return {'positive': ArticleSerializer(positive).data, 'negative': ArticleSerializer(negative).data}

    def get_first_article(self, obj):
        return obj.articles.exclude(medium__slant=None).earliest('datetime').datetime

    def get_wgt(self, obj):
        return {'this_count': obj.this_count, 'all_count': obj.all_count, 'score': obj.this_count / obj.all_count}

    def get_social_score(self, obj):
        return models.Tweet.objects.filter(article__event=obj).count()


class ArticleSerializer(serializers.ModelSerializer):
    medium = MediumSerializer()
    sentiment_bucket = serializers.SerializerMethodField()
    social_score = serializers.SerializerMethodField()

    def calculate_bucket(self, value):
        return round(round((value + 1) * 5) / 2)

    class Meta:
        model = models.Article
        fields = [
            'id',
            'uri',
            'title',
            'content',
            'image',
            'sentiment',
            'sentimentRNN',
            'sentiment_bucket',
            'medium',
            'datetime',
            'url',
            'og_title',
            'og_description',
            'og_image',
            'social_score',
        ]

    def get_sentiment_bucket(self, obj):
        return self.calculate_bucket(obj.sentiment)

    def get_social_score(self, obj):
        return obj.tweets.count()
