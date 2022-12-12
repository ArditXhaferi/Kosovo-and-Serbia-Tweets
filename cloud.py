
import tweepy
import networkx as nx
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from langdetect import detect
import random

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

tweets = client.search_recent_tweets(query=query, tweet_fields=['text', 'lang', 'entities'], max_results=100)

# Create a WordCloud object
text = []

# The regex pattern to match URLs
url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

colors = ['red', 'blue']

wc = WordCloud(background_color='white', width=1080, height=1080, font_path='font.ttf')
# Use the regex pattern to find and delete the URL
for tweet in tweets.data:
    if('RT @' not in tweet.text):
        string = re.sub(url_pattern, '', tweet.text)
        text.append(string)

# Generate a word cloud from the tweets
wc.generate(' '.join(text))


# def word_to_color(word, font_size, position, orientation, random_state=None, **kwargs):

#     if "kosovo" and "serbia" in word.lower():
#         return "blue"
#     elif "kosova" and "serbia" in word.lower():
#         return "red"
#     elif "kosovo" and "srpska" in word.lower():
#         return "green"
#     else:
#         return "yellow"

def word_to_color(word, font_size, position, orientation, random_state=None, **kwargs):
    return colors[random.choice([0, 1])]

# Use the custom color function to color the words in the wordcloud
wc.recolor(color_func=word_to_color)

plt.imshow(wc)
plt.show()