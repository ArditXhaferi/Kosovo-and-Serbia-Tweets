import matplotlib.pyplot as plt
import datetime

def line_chart(x_data, y_data, title, xlabel, ylabel):
    plt.plot(x_data, y_data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    

def plot_tweets_sentiment(tweets_sentiment):
    dates = sorted(tweets_sentiment.keys())
    for language in tweets_sentiment[dates[0]].keys():
        x = dates
        y = [tweets_sentiment[d].get(language, 0) for d in dates]
        if sum(y) == 0:
            continue
        plt.plot(x, y, label=language)
    plt.xlabel('Date')
    plt.ylabel('Sentiment Score')
    plt.legend()
    plt.show()