# Python script for streaming and harvesting tweets.
import json
from datetime import date

import couchdb

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


from testTimeline import getTimeline

class myListener(StreamListener):

	def on_data(self, data):
		# jData = json.parse(data)

		if data[0].isdigit():
			# print(data)
			pass
		else:
			jData = json.loads(data)
			uId = jData['user']['id_str']
			uCreationYear = int(jData['user']['created_at'][-4:])
			
			# insert into database if doesn't exist
			db[uId] = { 'user_year' :  uCreationYear }

			# call get timeline for current user
			## CALL HERE

			# getTimeline(uId, c_server, auth)


			# print(uId, uCreationYear)
			# exit(0)

	def on_error(self, status) :
		print (status)


keyId = 1
keys = None

cityId = 0
cityBounds = None

dbname = 'twitter_results'
c_server = None

with open('apiKeys.json') as fKeys:
	keys = json.load(fKeys)

if keys == None:
	print('Failed to load apiKeys.\nExitting.')
	exit(0)

with open('boxBounds.json') as fBounds:
	cityBounds = json.load(fBounds)[cityId]

if cityBounds == None:
	print('Failed to load city bounds.\nExitting.')
	exit(0)

try:
	user = "server_admin"
	password = "password"
	c_server = couchdb.Server("http://%s:%s@localhost:5984/" % (user,password))

except:
	print ("Cannot connect to DB.\nExitting.")
	exit(0)

if dbname in c_server:
	db = c_server[dbname]
else:
	db = c_server.create(dbname)


auth = OAuthHandler( keys[keyId]['consumer']['key'], keys[keyId]['consumer']['secret'] )
auth.set_access_token( keys[keyId]['access']['key'], keys[keyId]['access']['secret'] )

twitterStream = Stream(auth, myListener())
twitterStream.filter(locations=cityBounds['box'])
