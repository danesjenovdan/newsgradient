from datetime import datetime

from django.core.management import BaseCommand

from news.models import Tweet, Article, Event

import twint


def get_datetime_from_twint_datestring(datestring):
    return datetime.strptime(datestring, '%Y-%m-%d %H:%M:%S %Z')

def full_tweet_text(tweet):
  if not tweet.retweet:
    return tweet.tweet
  
  rt_prefix = tweet.tweet.split(': ')[0]
  return f'{rt_prefix}: {tweet.user_rt}'

def find_tweets(article):
    tweets = []

    twint_config = twint.Config()
    twint_config.Hide_output = True
    twint_config.Store_object = True
    twint_config.Store_object_tweets_list = tweets
    twint_config.Search = article.url

    # Run
    # twint.run.Profile(twint_config)
    twint.run.Search(twint_config)
    
    for tweet in tweets:
        db_tweet, created = Tweet.objects.get_or_create(twitter_id=tweet.id_str)

        db_tweet.user_handle = tweet.username
        db_tweet.timestamp = get_datetime_from_twint_datestring(tweet.datetime)
        db_tweet.text = full_tweet_text(tweet)

        db_tweet.retweet = bool(tweet.retweet)
        if db_tweet.retweet:
            db_tweet.retweet_timestamp = get_datetime_from_twint_datestring(tweet.retweet_date)
            db_tweet.retweet_id = tweet.retweet_id
            db_tweet.retweet_quote = bool(tweet.quote_url)
            if bool(tweet.quote_url):
                db_tweet.retweet_quote_url = tweet.quote_url
        
        db_tweet.quote = bool(tweet.quote_url)
        if db_tweet.quote:
            db_tweet.quote_url = tweet.quote_url
        
        db_tweet.favorite_count = int(tweet.likes_count)
        db_tweet.retweet_count = int(tweet.retweets_count)

        db_tweet.article = article
        db_tweet.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
        todays_events = Event.objects.filter(date=datetime.now().date())
        for event in todays_events:
            articles = Article.objects.filter(event=event)
            for article in articles:
                find_tweets(article)
