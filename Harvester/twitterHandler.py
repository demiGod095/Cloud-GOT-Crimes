# Python script for streaming and harvesting tweets.
import json
from datetime import date

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from TwitterSearch import *

class listener(StreamListener):

	def on_data(self, data):
		# jData = json.parse(data)

		if data[0].isdigit():
			# print(data)
			pass
		else:
			jData = json.loads(data)
			# print(json.dumps(jData, indent = 4))
			print(jData['user']['screen_name'])
			exit(0)

	def on_error(self, status):
		print (status)


keyId = 0
keys = None

with open('apiKeys.json') as fKeys:
	keys = json.load(fKeys)

if keys == None:
	print('Failed to load apiKeys.\nExitting.')
	exit(0)



auth = OAuthHandler( keys[keyId]['consumer']['key'], keys[keyId]['consumer']['secret'] )

auth.set_access_token( keys[keyId]['access']['key'], keys[keyId]['access']['secret'] )

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['food'])

