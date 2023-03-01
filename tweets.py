import tweepy
import os
from dotenv import load_dotenv


def get_tweets():
    load_dotenv()
    client = tweepy.Client(bearer_token=os.getenv("API"))

    query = """
        Kosovo Serbia OR
        Kosovo Srpska OR
        Kosova Serbia OR
        North of Kosovo OR
        north of Kosovo OR
        North of Kosova OR
        north of Kosova OR
        Kosovo Srpska -is:retweet
    """

    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'entities', 'lang', 'possibly_sensitive', 'public_metrics'], max_results=100)

    return tweets.data

def get_tweets_by_date(since_date, until_date):
    load_dotenv()
    client = tweepy.Client(bearer_token=os.getenv("API"),  consumer_key=None, consumer_secret=None, access_token=None, access_token_secret=None)
    print(client)
    query = """
        Kosovo Serbia OR
        Kosovo Srpska OR
        Kosova Serbia OR
        North of Kosovo OR
        north of Kosovo OR
        North of Kosova OR
        north of Kosova OR
        Kosovo Srpska -is:retweet
    """

    tweets = client.search_all_tweets(query=query, start_time=since_date, end_time=until_date, max_results=500)

    return tweets.data