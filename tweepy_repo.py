import requests
import tweepy

bearer_token = "AAAAAAAAAAAAAAAAAAAAAIszhAEAAAAAEXDVc2f353JZh%2BLRt3B51dIdwQU%3D28hAvE7ejRA4StzVLrhUAtSHcbJwDATdS7Cfas2UgqXMJijBiM"
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "User-Agent": "My Twitter Scraper",
}

def get_tweet_date(tweet_id):
    url = f"https://api.twitter.com/2/tweets/{tweet_id}?tweet.fields=created_at"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        tweet = response.json()
        if "data" in tweet:
            return tweet['data']["created_at"]
        else:
            return "Error";
    else:
        print(f"Error getting tweet with id {tweet_id}: {response.text}")
        return None

def getTweepyAPI():
    consumer_key = "9OjCbiV6IOAi6fA8J9VG8ZiCV"
    consumer_secret = "78dDG8aWSqKk6eINeR3eYbeffUuyn7dFfqk8k7tp3eAk61kIqf"
    access_token = "1423354093012197377-6IgtZfrwwWbHWQOweETrR0iKkT8kaD"
    access_token_secret = "oZhB2ghATxegd1nTu1NOuTuzvy8eNjYcmKU9CLl8xR3VX"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    return tweepy.API(auth)