# fetch_tweets.py

import tweepy
import csv

def fetch_tweets(api_key, api_secret, query, count=100):
    auth = tweepy.AppAuthHandler(api_key, api_secret)
    api = tweepy.API(auth)
    tweets = api.search_tweets(q=query, count=count, lang='en')
    with open('data/sample_tweets.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['tweet_id', 'timestamp', 'text'])
        for tweet in tweets:
            writer.writerow([tweet.id_str, tweet.created_at, tweet.text])
