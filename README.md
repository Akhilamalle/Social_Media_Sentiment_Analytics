# Social Media Sentiment Analytics

## Overview
This project analyzes customer sentiment on social media posts for brand monitoring using a pipeline that includes:
- Twitter API for data ingestion
- Spark NLP for sentiment analysis
- PostgreSQL for data warehousing

## Folder Structure
- `sql/`: SQL scripts for table creation
- `scripts/`: Python scripts for fetching tweets, analyzing sentiment, and loading to PostgreSQL
- `data/`: Sample data files

## Technologies
- Python
- Tweepy
- Spark NLP
- PostgreSQL
- SQLAlchemy

## Usage
1. Run `fetch_tweets.py` to collect tweets.
2. Run `sentiment_nlp.py` to analyze sentiment.
3. Run `load_to_postgres.py` to store results in PostgreSQL.
