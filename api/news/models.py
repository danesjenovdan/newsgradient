from django.db import models

# Create your models here.
from constants import Orientations
from constants import Reliability


class Medium(models.Model):
    ORIENTATIONS = (
        (Orientations.LEFT.value, 'Left'),
        (Orientations.NEUTRAL.value, 'Neutral'),
        (Orientations.RIGHT.value, 'Right'),
    )
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

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def article_count(self):
        return self.articles.count()


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
