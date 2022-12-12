# import tweepy



# # Search for tweets containing the specified keywords
# tweets = api.search_all_tweets(query)

# # Print the text of each tweet
# for tweet in tweets:
#     print(tweet.text)

import tweepy
import networkx as nx
import matplotlib.pyplot as plt

# Replace these with your own API credentials
consumer_key = "9OjCbiV6IOAi6fA8J9VG8ZiCV"
consumer_secret = "78dDG8aWSqKk6eINeR3eYbeffUuyn7dFfqk8k7tp3eAk61kIqf"
access_token = "1423354093012197377-6IgtZfrwwWbHWQOweETrR0iKkT8kaD"
access_token_secret = "oZhB2ghATxegd1nTu1NOuTuzvy8eNjYcmKU9CLl8xR3VX"

# Authenticate to the Twitter API using your credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Connect to the Twitter API using the authenticate
api = tweepy.API(auth)

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAIszhAEAAAAAcHco%2BbjF1TSCybAo4DoF4z%2F5P%2FU%3DrlZtwKdZVySFCJFkc9hNdgZwKxwRic4UymW0Lgznb1H04KVERK')

# Replace with your own search query
query = """
    Kosovo Serbia OR
    Kosovo Srpska OR
    Kosova Serbia OR
    Kosovo Srpska -is:retweet
"""
graph = nx.Graph()

tweets = client.search_recent_tweets(query=query, tweet_fields=['text', 'lang', 'entities'], max_results=10)

langs = ["en", "sq", "rs"]

for tweet in tweets.data:
    
    graph.add_node(tweet, label=tweet.lang)
    
def getTweetLocation(tweet):
    if "kosovo" and "serbia" in tweet.lower():
        return "en"
    elif "kosova" and "serbia" in tweet.lower():
        return "sq"
    elif "kosovo" and "srpska" in tweet.lower():
        return "rs"
    else:
        return "undefined: " + tweet

for tweet in tweets.data:
    if('RT @' not in tweet.text):
        # text = tweet.text[0:5]
        # print(getTweetLocation(tweet.text))
        graph.add_edge(tweet, tweet.lang)



nx.draw(graph, with_labels="true")
nx.draw_networkx_labels(graph, pos=nx.spring_layout(graph))
plt.show()