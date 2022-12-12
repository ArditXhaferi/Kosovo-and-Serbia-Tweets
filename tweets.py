import tweepy

def get_tweets():
    client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAIszhAEAAAAAcHco%2BbjF1TSCybAo4DoF4z%2F5P%2FU%3DrlZtwKdZVySFCJFkc9hNdgZwKxwRic4UymW0Lgznb1H04KVERK')

    query = """
        Kosovo Serbia OR
        Kosovo Srpska OR
        Kosova Serbia OR
        Kosovo Srpska -is:retweet
    """

    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'entities', 'lang', 'possibly_sensitive', 'public_metrics'], max_results=10)

    return tweets.data