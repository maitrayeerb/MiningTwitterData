import tweepy
from tweepy import OAuthHandler
import codecs, json

consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def process_or_store(tweet):
    with codecs.open('test.json', 'w', 'utf8') as f:
        f.write(json.dumps(tweet, sort_keys=True, ensure_ascii=False))

        #    with open('no.txt', 'w') as txtfile:
        #json.dump(tweet, txtfile)

## read our own timeline
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)

   ## store the json
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)

## list of our followers
for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)


## list of all our tweets
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)