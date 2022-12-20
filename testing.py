from db import count_tweets_in_db, load_db, generate_tweet_text_array
from sentiment import eval
from pie import make_pie_chart
from bar import make_bar_chart
from country_code import get_country_name
from testing_repository import first
from cloud import create_cloud


# print(count_tweets_in_db())

data = load_db()
labelsN = {}
labelsUF = {}
labelsU = {}
labelsP = {}

# first(data)

# create_cloud(generate_tweet_text_array())

# for tweet in data.keys():
#     if data[tweet]['lang'] not in labelsU:
#         labelsU[get_country_name(data[tweet]['lang'])] = 0
#     if data[tweet]['lang'] not in labelsP:
#         labelsP[data[tweet]['lang']] = 0
#     if data[tweet]['lang'] not in labelsN:
#         labelsN[data[tweet]['lang']] = 0
#     result = eval(data[tweet]['text'])
#     if result == "Neutral":
#         labelsU[get_country_name(data[tweet]['lang'])] += 1
#     elif result == "Positive":
#         labelsP[data[tweet]['lang']] += 1
#     elif result == "Negative":
#         labelsN[data[tweet]['lang']] += 1

# for labels in labelsU:
#     if labelsU[labels] > 100:
#         labelsUF[labels] = labelsU[labels]
# make_pie_chart(labelsU.keys(), labelsU.values(), "Neutral")
# make_pie_chart(labelsP.keys(), labelsP.values(), "Postive")
# make_pie_chart(labelsN.keys(), labelsN.values(), "Negative")
# make_bar_chart(labelsU.keys(), labelsU.values(), "Neutral")
# make_bar_chart(labelsP.keys(), labelsP.values(), "Postive")
# make_bar_chart(labelsUF.keys(), labelsUF.values(), "Negative")
