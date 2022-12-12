from textblob import TextBlob
from tweets import get

tweets = get()
print(tweets[0])

# create a TextBlob object from the sentence
sentence = "This is a great day!"
blob = TextBlob(sentence)

# determine the sentiment of the sentence
if blob.sentiment.polarity > 0:
    print("The sentiment of the sentence is positive.")
elif blob.sentiment.polarity == 0:
    print("The sentiment of the sentence is neutral.")
else:
    print("The sentiment of the sentence is negative.")