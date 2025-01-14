import tweepy

# brew install python@3.12
# /opt/homebrew/Cellar/python@3.12/3.12.8/bin/python3.12 -m venv myenv1
# source myenv1/bin/activate
# pip install tweepy
# python delete_tweets.py

# Replace with your own Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

def delete_all_tweets():
    try:
        # Authenticate with Twitter
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        # Fetch all tweets from your timeline
        print("Fetching tweets...")
        tweets = api.user_timeline(count=200, tweet_mode='extended')

        if not tweets:
            print("No tweets found.")
            return

        # Loop through tweets and delete each one
        for tweet in tweets:
            print(f"Deleting tweet ID: {tweet.id} - {tweet.full_text[:50]}...")
            api.destroy_status(tweet.id)
        print("All tweets deleted successfully!")

    except tweepy.TweepError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    delete_all_tweets()