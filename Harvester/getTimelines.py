import json
from datetime import date

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
	tuo = TwitterUserOrder(currentUser)
	base = tuo.create_search_url()
	base += '&tweet_mode=extended&trim_user=true'
	tuo.set_search_url(base)

	ts = TwitterSearch(
		consumer_key = keys[keyId]['consumer']['key'],
		consumer_secret = keys[keyId]['consumer']['secret'],
		access_token = keys[keyId]['access']['key'],
		access_token_secret = keys[keyId]['access']['secret']
	)

	# start asking Twitter about the timeline
	twitDoc = {}
	twitDoc['docs'] = []
	for c, tweet in enumerate(ts.search_tweets_iterable(tuo) ) :
		# print('%d - @%s tweeted: %s' % ( c, tweet['user']['screen_name'], tweet['text'] ))
		twitYear = int(tweet['created_at'][-4:])
		twitUserId = tweet['user']['id']
		
		# twitText = tweet['entities']['hashtags']
		if tweet['retweeted'] :
			twitText = tweet['retweeted_status']['full_text']
		else :
			twitText = tweet['full_text']

		twitDoc['docs'].append({'uid': twitUserId, 'year' : twitYear, 'text': twitText})

	twitDoc['docs'].reverse()

	# INSERT INTO DB HERE
	print(json.dumps(twitDoc))


except TwitterSearchException as e: # catch all those ugly errors
	print(e)