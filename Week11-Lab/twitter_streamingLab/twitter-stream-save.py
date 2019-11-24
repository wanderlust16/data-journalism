import tweepy
import json

consumer_key = 'bw5hox6zAolb8vJrMcE0jjgk7'
consumer_secret = 'Py0I2s2qerylZlViWVxtxvDbnj3Juo1TPTT0GiJxu7stVhSDXV'
access_token = '1193801853923758080-Kl4FlscU99SJljxFMdsDOlBxH0UXe4'
access_secret = '2enFNME8mZiVrEP9DzgdpTjZ7yEsG9kJtvNH6j80XwlbU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

class MyListener(tweepy.StreamListener):

    def on_status(self, data):
        print(data.text + "\n----")

    def on_data(self, data):
        try:
            with open('tweet_stream.json', 'a') as file:
                file.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on_data: {}".format(str(e)))
        return True

twitter_stream = tweepy.Stream(auth, MyListener())
twitter_stream.filter(track=['trump', 'clinton'])
