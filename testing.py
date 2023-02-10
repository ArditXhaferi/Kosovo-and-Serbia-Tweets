from db import count_tweets_in_db, load_db, load_date_db
from sentiment import eval, polarity
from pie import make_pie_chart
from bar import make_bar_chart
from country_code import get_country_name
from testing_repository import first
# from cloud import create_cloud
from tweepy_repo import get_tweet_date
import json
import uuid
import time

print(count_tweets_in_db())

data = load_db()
dates = load_date_db()
labelsN = {}
labelsUF = {}
labelsU = {}
labelsP = {}
tweets_sentiment = {'2022-12-12': 0, '2022-12-13': 0, '2022-12-14': 0, '2022-12-15': 0, '2022-12-16': 0, '2022-12-20': 0, '2022-12-21': 0, '2022-12-22': 0, '2022-12-23': 0, '2022-12-25': 0, '2022-12-26': 0, '2022-12-27': 0, '2022-12-28': 0, '2022-12-29': 0, '2022-12-30': 0, '2023-01-01': 0, '2022-12-31': 0, '2023-01-02': 0, '2023-01-03': 0, '2023-01-04': 0, '2023-01-05': 0, '2023-01-06': 0, '2023-01-07': 0, '2023-01-08': 0, '2023-01-09': 0}
count = 0
for tweet in list(data.keys()):
    id = data[tweet]['id']
    if str(id) in dates:
        date = dates[str(id)][0:10]
        text = data[tweet]['text']
        tweets_sentiment[date] += polarity(text)
        
print(tweets_sentiment, count)

# for labels in labelsU:
#     if labelsU[labels] > 100:
#         labelsUF[labels] = labelsU[labels]
# make_pie_chart(labelsU.keys(), labelsU.values(), "Neutral")
# make_pie_chart(labelsP.keys(), labelsP.values(), "Postive")
# make_pie_chart(labelsN.keys(), labelsN.values(), "Negative")
# make_bar_chart(labelsU.keys(), labelsU.values(), "Neutral")
# make_bar_chart(labelsP.keys(), labelsP.values(), "Postive")
# make_bar_chart(labelsUF.keys(), labelsUF.values(), "Negative")
