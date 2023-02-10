import json
from tweet import Tweet
import re
import os
from dotenv import load_dotenv

load_dotenv()


def load_db():
    try:
        #todo add this in .env
        with open(os.getenv('DB_PATH'), 'r') as f:
            data = json.loads(f.read())

        return data
    except:
        return {}
    
def load_date_db():
    try:
        #todo add this in .env
        with open(os.getenv('DATE_DB_PATH'), 'r') as f:
            data = json.loads(f.read())

        return data
    except:
        return {}

def create_or_update_db(request):
    db = load_db()
    for data in request:
        db[data.id] = getattr(Tweet(**data), 'get')()
    
    with open(os.getenv('DB_PATH'), 'w') as f:
        f.write(json.dumps(db))

def count_tweets_in_db():
    return len(load_db())

def generate_tweet_text_array():
    text_array = []

    data = load_db()
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    for tweet in data.keys():
        text = re.sub(url_pattern, '', data[tweet]['text'])

        for word in text.split():
            if len(word) > 3:
                text_array.append(word)

    print(len(text_array))
    return text_array