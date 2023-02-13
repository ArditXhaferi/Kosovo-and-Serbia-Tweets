from db import count_tweets_in_db, load_db, load_date_db
from sentiment import eval, polarity
from pie import make_pie_chart
from bar import make_bar_chart
from country_code import get_country_name
from testing_repository import first
# from cloud import create_cloud
from tweepy_repo import get_tweet_date
from line import line_chart, plot_tweets_sentiment
from helper import *
import json
import uuid
import time
from langdetect import detect
from lingua import Language, LanguageDetectorBuilder
from translate import translate_text_to_english
detector = LanguageDetectorBuilder.from_all_spoken_languages().build()

data = load_db()
dates = load_date_db()
labelsN = {}
labelsUF = {}
labelsU = {}
labelsP = {}
tweets_sentiment = {}
count = 0
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

for tweet in list(data.keys()):
    id = data[tweet]['id']
    if str(id) in dates:
        date = dates[str(id)][0:10]
        # language = data[tweet]['lang']
        text = data[tweet]['text']
        try:
            language = detector.detect_language_of(text)
            language = language._name_
            count+= 1
        except:
            language = "error"
        
        if language == "SERBIAN":
            print(f'{polarity(text)}: {text}')
        

        if language not in tweets_sentiment:
            tweets_sentiment[language] = {}
        if date not in tweets_sentiment[language]:
            tweets_sentiment[language][date] = 0
        translated_text = translate_text_to_english(text)
        vs = analyzer.polarity_scores(translated_text)
        print(vs['compound'], count)
        tweets_sentiment[language][date] += vs['compound']


        
print(json.dumps(tweets_sentiment))
# dates_formatted = map_remove_first_four_chars(list(tweets_sentiment.keys()))

# plot_tweets_sentiment(tweets_sentiment)
# line_chart(dates_formatted, tweets_sentiment.values(), "Sentiment from the dates 2022-12-12-2023-01-09", "Date", "Sentiment")

# for labels in labelsU:
#     if labelsU[labels] > 100:
#         labelsUF[labels] = labelsU[labels]
# make_pie_chart(labelsU.keys(), labelsU.values(), "Neutral")
# make_pie_chart(labelsP.keys(), labelsP.values(), "Postive")
# make_pie_chart(labelsN.keys(), labelsN.values(), "Negative")
# make_bar_chart(labelsU.keys(), labelsU.values(), "Neutral")
# make_bar_chart(labelsP.keys(), labelsP.values(), "Postive")
# make_bar_chart(labelsUF.keys(), labelsUF.values(), "Negative")
