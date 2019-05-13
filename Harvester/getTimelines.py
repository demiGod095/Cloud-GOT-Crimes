import json
from datetime import date
import tweepy
from TwitterSearch import *

currentUser = 'shreyasAujc'

keyId = 0
keys = None

with open('apiKeys.json') as fKeys:
	keys = json.load(fKeys)

if keys == None:
	print('Failed to load apiKeys.\nExitting.')
	exit(0)

try:
	
	consumer_key = keys[keyId]['consumer']['key']
	consumer_secret = keys[keyId]['consumer']['secret']
	access_token = keys[keyId]['access']['key']
	access_token_secret = keys[keyId]['access']['secret']
	auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	
	api = tweepy.API(auth)

	# start asking Twitter about the timeline
	twitDoc = {}
	twitDoc['docs'] = []
	for status in tweepy.Cursor(api.user_timeline, screen_name='@'+currentUser, tweet_mode="extended").items():
		try:
			twitYear = status.created_at.year
			twitUserId = status.user.id
			twitUserName = status.user.name
			twitText = status.full_text
			twitRetweeted = status.retweeted
			twitScreenName = status.user.screen_name		
			twitDoc['docs'].append({'user_id':twitUserId,'screen_name':twitScreenName,'year':twitYear,'text':twitText,'user_name':twitUserName,'retweet_status':twitRetweeted})
		except:
			pass
	twitDoc['docs'].reverse()
					
	# INSERT INTO DB HERE
	print(json.dumps(twitDoc))


except TwitterSearchException as e: # catch all those ugly errors
	print(e)
