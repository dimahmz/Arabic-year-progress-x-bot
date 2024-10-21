from dotenv import load_dotenv
import os
import tweepy
from hijri_year_progress import HijriYearProgress
from tweet_text import teweet_text_generator
from progress_bar import generate_progress_bar
from datetime import datetime




load_dotenv("src/.env.local")

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("bearer_token")



def main():
    # V1 Twitter API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # V2 Twitter API Authentication
    client = tweepy.Client(
        bearer_token,
        consumer_key, consumer_secret,
        access_token, access_token_secret,
        wait_on_rate_limit=True
    )
    # instanciate a new hijri year progress
    hijri_year_progress = HijriYearProgress(datetime(2024,12,18))

    # generate a new tweet for the that hijri year 
    tweet_text = teweet_text_generator(hijri_year_progress)

    # generate a progress image bar the that hijri year
    filename = generate_progress_bar(hijri_year_progress.percent)

    media_id = api.media_upload(filename).media_id_string

    response = client.create_tweet(
        text=tweet_text,
        media_ids=[media_id]
    )
    print(f"https://twitter.com/user/status/{response.data['id']}")


if __name__ == "__main__":
    main()
