# For Twitter API v2 Instead of v1.1

import tweepy
import pandas as pd

# Replace with your own Bearer Token (from Developer Portal)
bearer_token = "YOUR_BEARER_TOKEN"

# Set up the Tweepy v2 Client
client = tweepy.Client(bearer_token=bearer_token)

# Fetch recent tweets from a user (Elon Musk’s user ID is needed)
user_id = "44196397"  # Elon Musk's user ID

# Fetch latest tweets
response = client.get_users_tweets(id=user_id, max_results=10, tweet_fields=["created_at", "public_metrics"])

tweets_data = []
for tweet in response.data:
    tweets_data.append({
        "text": tweet.text,
        "created_at": tweet.created_at,
        "retweets": tweet.public_metrics["retweet_count"],
        "likes": tweet.public_metrics["like_count"]
    })

df = pd.DataFrame(tweets_data)
df.to_csv("elonmusk_tweets_v2.csv", index=False)
print(df.head())
