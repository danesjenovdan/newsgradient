from django.db import models
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _

# Create your models here.
from constants import CacheKeys, Orientations
from constants import Reliability


class Medium(models.Model):
    ORIENTATIONS = (
        (Orientations.LEFT.value, 'Left'),
        (Orientations.NEUTRAL.value, 'Neutral'),
        (Orientations.RIGHT.value, 'Right'),
    )
    class Locations(models.TextChoices):
        FBIH = 'FBIH', _('FBIH')
        HBZ = 'HBŽ', _('HBŽ')
        SZ = 'SŽ', _('SŽ')
        ZZH = 'ŽZH', _('ŽZH')
        ZDZ = 'ZDŽ', _('ZDŽ')
        USZ = 'USŽ', _('USŽ')
        HNZ = 'HNŽ', _('HNŽ')
        ZSB = 'ŽSB', _('ŽSB')
        BPZ = 'BPŽ', _('BPŽ')
        TZ = 'TŽ', _('TŽ')
        RS = 'RS', _('RS')
        BRCKO = 'Brčko', _('Brčko')

    title = models.CharField(max_length=128)
    uri = models.CharField(max_length=128, db_index=True)
    favicon = models.URLField(
        max_length=512,
        null=True,
        blank=True
    )
    slant = models.PositiveSmallIntegerField(
        choices=ORIENTATIONS,
        null=True,
        blank=True
    )
    is_embeddable = models.BooleanField(default=True)
    reliability = models.PositiveSmallIntegerField()
    partyscore = models.ManyToManyField('Party', related_name='medias', through='PartyMediumScore', verbose_name=_('Party score'))
    location = models.CharField(
        max_length=5,
        choices=Locations.choices,
        default=Locations.FBIH,
        verbose_name=_('Media\'s location')
    )

    def __str__(self):
        return self.title

    @property
    def reliability_group(self):
        if self.reliability >= 33:
            return Reliability.FACT_REPORTING
        elif 17 <= self.reliability < 33:
            return Reliability.OPINION_PERSUASION
        else:
            return Reliability.PROPAGANDA


class Event(models.Model):
    #class Meta:
    #    ordering = ['-article_count']

    uri = models.TextField(primary_key=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)
    title = models.TextField(default='')
    date = models.DateField(db_index=True)
    images = models.TextField(default='', blank=True)
    is_promoted = models.BooleanField(default=False, db_index=True)
    description = models.TextField(null=True, blank=True)
    og_image_article = models.ForeignKey(
        'Article',
        related_name='+',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def article_count(self):
        return self.articles.count()

    def save(self, *args, **kwargs):
        if self.pk:
            cache_key = f'{CacheKeys.EVENT_ARTICLES}::{self.pk}'
            cache.delete(cache_key)

        super().save(*args, **kwargs)


class Article(models.Model):
    uri = models.TextField(primary_key=True)
    title = models.TextField( default='')
    content = models.TextField(default='')
    url = models.URLField(max_length=512)
    datetime = models.DateTimeField()
    image = models.CharField(max_length=512, null=True, blank=True)
    medium = models.ForeignKey('Medium', related_name='articles', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', related_name='articles', on_delete=models.CASCADE, null=True, blank=True)

    sentiment = models.FloatField(null=True, blank=True)
    sentimentRNN = models.FloatField(null=True, blank=True)

    og_title = models.CharField(
        max_length=512,
        null=True,
        blank=True
    )
    og_image = models.CharField(
        max_length=512,
        null=True,
        blank=True
    )
    og_description = models.CharField(
        max_length=512,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


class Tweet(models.Model):
    updated_at = models.DateTimeField(db_index=True, auto_now=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, blank=True, null=True, related_name='tweets')
    twitter_id = models.TextField(null=False, unique=True)
    timestamp = models.DateTimeField(null=True)
    text = models.TextField(null=False)

    retweet = models.BooleanField(default=False)
    retweet_timestamp = models.DateTimeField(null=True)
    retweet_id = models.TextField(null=True)
    retweet_quote = models.BooleanField(default=False)
    retweet_quote_url = models.URLField(null=True)

    quote = models.BooleanField(default=False)
    quote_url = models.URLField(null=True)

    favorite_count = models.IntegerField(null=True)
    retweet_count = models.IntegerField(null=True)

    user_handle = models.TextField(null=False)

class Newsletter(models.Model):
    date = models.DateField()
    events = models.ManyToManyField(
        'Event',
        blank=True,
        help_text='Events to include in the newsletter',
    )
    sent = models.BooleanField(
        blank=False,
        null=False,
        default=False,
    )

    def __str__(self):
        return self.date.strftime('%-d. %-m. %Y')

class Party(models.Model):
    name = models.TextField(verbose_name=_('Name'))
    parser_names = models.TextField(verbose_name=_('Parser names separated with |'))
    mediumscore = models.ManyToManyField('Medium', related_name='parties', through='PartyMediumScore', verbose_name=_('Medium score'))

    def __str__(self):
        return self.name


class PartyMediumScore(models.Model):
    party = models.ForeignKey('Party', on_delete=models.CASCADE, related_name='partymediumscore', verbose_name=_('Party'))
    medium = models.ForeignKey('Medium', on_delete=models.CASCADE, related_name='partymediumscore', verbose_name=_('Medium'))
    score = models.DecimalField(max_digits=10, decimal_places=7,null=True, blank=True, verbose_name=_('Score'))
    neutral_score = models.DecimalField(max_digits=10, decimal_places=7,null=True, blank=True, verbose_name=_('Neutral score'))
