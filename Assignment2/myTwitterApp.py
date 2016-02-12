#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#import json
#import pandas as pd
#import matplotlib.pylot as plt

#The portions of this code was acquired by the following Twipper tutorial links:
#------------------------------------------------------------------------------------------------------
#http://adilmoujahid.com/posts/2014/07/twitter-analytics/   
#http://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file-in-python
#http://docs.tweepy.org/en/latest/getting_started.html
#http://social-metrics.org/twitter-user-data/
#------------------------------------------------------------------------------------------------------


#Variables that contains the user credentials to access Twitter API 
access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['.org', '.com', '.net', 'tinyurl','t.co', 'bit.ly', 'goo.gl', 'http'])
#
