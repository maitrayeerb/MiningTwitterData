import tweepy
from tweepy import OAuthHandler

from tweepy import Stream
from tweepy.streaming import StreamListener
import time


class MyListener(StreamListener):
    def __init__(self, time_limit=60):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open('fifaworldcup.json', 'a')
        super(MyListener, self).__init__()

    def on_data(self, data):
        try:
            if (time.time() - self.start_time) < self.limit:
                self.saveFile.write(data)
                self.saveFile.write('\n')
                return True
            else:
                self.saveFile.close()
                return False

        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)



myStream = tweepy.Stream(auth=api.auth, listener=MyListener(time_limit=30))
myStream.filter(track=['#fifaworldcup'])