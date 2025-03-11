import tweepy  
import time  
import os  

# Load API keys from environment variables  
API_KEY = os.getenv("API_KEY")  
API_SECRET = os.getenv("API_SECRET")  
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")  
ACCESS_SECRET = os.getenv("ACCESS_SECRET")  

# Authenticate with Twitter API  
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)  
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)  
api = tweepy.API(auth, wait_on_rate_limit=True)  

# Function to tweet  
def tweet():  
    message = "🚩 जय श्री राम! #SanatanDharma"  
    api.update_status(message)  
    print("Tweeted:", message)  

# Run the bot every hour  
while True:  
    tweet()  
    time.sleep(3600)  # Wait for 1 hour  
