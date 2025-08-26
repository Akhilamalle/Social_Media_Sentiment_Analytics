-- create_tables.sql

CREATE TABLE dim_platform (
    platform_id SERIAL PRIMARY KEY,
    platform_name VARCHAR(50) NOT NULL
);

CREATE TABLE dim_campaign (
    campaign_id SERIAL PRIMARY KEY,
    campaign_name VARCHAR(100),
    start_date DATE,
    end_date DATE,
    target_keywords TEXT
);

CREATE TABLE fact_sentiment (
    tweet_id VARCHAR(50) PRIMARY KEY,
    timestamp TIMESTAMP,
    sentiment_score FLOAT,
    sentiment_label VARCHAR(20),
    platform_id INT REFERENCES dim_platform(platform_id),
    campaign_id INT REFERENCES dim_campaign(campaign_id)
);
