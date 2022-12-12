import tweepy

# Authenticate with the Twitter API
consumer_key = "9OjCbiV6IOAi6fA8J9VG8ZiCV"
consumer_secret = "78dDG8aWSqKk6eINeR3eYbeffUuyn7dFfqk8k7tp3eAk61kIqf"
access_token = "1423354093012197377-6IgtZfrwwWbHWQOweETrR0iKkT8kaD"
access_token_secret = "oZhB2ghATxegd1nTu1NOuTuzvy8eNjYcmKU9CLl8xR3VX"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets containing a specific keyword or hashtag
tweets = tweepy.Cursor(api.user_timeline, q='#python').items(100)

# Iterate over the tweets
for tweet in tweets:
    # Print the text of the tweet
    print(tweet.text)

    # Print the mentions in the tweet
    print(tweet.mentions)