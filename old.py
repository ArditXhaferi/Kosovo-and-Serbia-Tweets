import snscrape.modules.twitter as sntwitter
import pandas as pd
import json
import time

# Set search query parameters
keyword = "Kosovo"
start_date = pd.to_datetime("2022-06-02")
end_date = pd.to_datetime("2023-01-01")

# Set up tweet criteria and execute search for each day
while start_date < end_date:
    # Define start and end date for current search
    current_start = start_date.strftime("%Y-%m-%d")
    current_end = (start_date + pd.DateOffset(days=1)).strftime("%Y-%m-%d")
    
    # Set up search query and execute search
    query = f"{keyword} since:{current_start} until:{current_end}"
    max_tweets = 100
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= max_tweets:
            break
        tweets.append([tweet.date.strftime('%Y-%m-%d %H:%M:%S'), tweet.content])

    # Store tweets in a pandas dataframe
    data = pd.DataFrame(tweets, columns=['date', 'text'])

    # Save results to a JSON file
    filename = f"data/{current_start}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data.to_dict(orient="records"), f)

    # Print the number of tweets collected and sleep for 5 seconds
    print(f"Number of tweets collected for {current_start}: {len(data)}")
    time.sleep(30)
    
    # Move on to the next day
    start_date += pd.DateOffset(days=1)
