# sentiment analyzer
# importing our tweeter library
import tweepy
# importing our natural language library TextBlob
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# setting the api variable
api = tweepy.API(auth)

#  search for tweets that takes a single argument
public_tweets = api.search('Warriors')

# creating a for loop to increment to every value
for tweet in public_tweets:
    print(tweet.text)
    # store our analysis
    analysis = TextBlob(tweet.text)
    # show sentiment analysis
    print(analysis.sentiment)
    print("\n")
