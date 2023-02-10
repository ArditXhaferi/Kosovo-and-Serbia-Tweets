import requests

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
