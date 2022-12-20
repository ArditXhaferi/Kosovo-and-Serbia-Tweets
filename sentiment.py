from textblob import TextBlob

def eval(sentence):
    blob = TextBlob(sentence)

    # determine the sentiment of the sentence
    if blob.sentiment.polarity > 0:
        return "Positive"
    elif blob.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"
