import Tweepy
import random

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

followers = tweepy.Cursor(api.followers).items()

for follower in followers:
	num = random.randint(0,9)
	if num == 1:
		follower.follow()
		print('I just followed ' + follower.screen_name + '!')
