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