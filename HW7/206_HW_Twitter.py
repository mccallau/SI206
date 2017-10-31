import unittest
import tweepy
import requests
import json

## SI 206 - HW
## COMMENT WITH:
## Your section day/time: Thursday 8:30am
## Any names of people you worked with on this assignment:


## Write code that uses the tweepy library to search for tweets with three different phrases of the 
## user's choice (should use the Python input function), and prints out the Tweet text and the 
## created_at value (note that this will be in GMT time) of the first FIVE tweets with at least 
## 1 blank line in between each of them, e.g.


## You should cache all of the data from this exercise in a file, and submit the cache file 
## along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets 
## about "rock climbing", when we run your code, the code should use CACHED data, and should not 
## need to make any new request to the Twitter API.  But if, for instance, you have never 
## searched for "bicycles" before you submitted your final files, then if we enter "bicycles" 
## when we run your code, it _should_ make a request to the Twitter API.

## Because it is dependent on user input, there are no unit tests for this -- we will 
## run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

##SAMPLE OUTPUT
## See: https://docs.google.com/a/umich.edu/document/d/1o8CWsdO2aRT7iUz9okiCHCVgU5x_FyZkabu2l9qwkf8/edit?usp=sharing



## **** For extra credit, create another file called twitter_info.py that 
## contains your consumer_key, consumer_secret, access_token, and access_token_secret, 
## import that file here.  Do NOT add and commit that file to a public GitHub repository.

import twitter_info #extra credit

## **** If you choose not to do that, we strongly advise using authentication information 
## for an 'extra' Twitter account you make just for this class, and not your personal 
## account, because it's not ideal to share your authentication information for a real 
## account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these 
## with variables rather than filling in the empty strings if you choose to do the secure way 
## for EC points
consumer_key = twitter_info.consumer_key 
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret

## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Set up library to grab stuff from twitter with your authentication, and 
# return it in a JSON-formatted way



## Write the rest of your code here!

def cachedat(): #Creates and grabs caching dictionary if available
	cache = {}
	try:
		cached = open("twittercache.json",'r')
		cache = json.load(cached)
		cached.close()
	except:
		pass
	return cache

def graborcache(userinput): #Retrieves user input tweets from cache or fetches from Twitter if not in cache
	cache = cachedat() #Caching object to add fetched Tweets to
	if userinput in cache.keys():
		print("using cache")
		tweets=[]
		for tweet in cache[userinput]['statuses']: #Retrieves 5 most updated tweets from cache including the user input
			if len(tweets)<5:
				if userinput in tweet["text"]:
					tweets.append(tweet)
		returnobj = {userinput: tweets}
		return returnobj
	else:
		print("fetching from Twitter")
		api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
		tweets = []
		result = api.search(q=userinput) #Retrieves 5 most updated tweets from Twitter including the user input
		cache[userinput]=result #Takes current cache definitions and adds term along with result to them
		for tweet in cache[userinput]['statuses']: #Orders through the result tweets to retrieve the first 5 including the exact user input
			if len(tweets)<5:
				if userinput in tweet["text"]:
					tweets.append(tweet)
		returnobj = {userinput:tweets}
		cachewrite = open("twittercache.json",'w')
		json.dump(cache, cachewrite) 
		return returnobj


import sys #Had unicode encoding errors 
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

exit=0
while exit<3: #Loops three times asking user for input, calls function to cache or fetch and prints tweets and time
	userinp = input("Enter Tweet term: ")
	obj = graborcache(userinp)
	for tweets in obj[userinp]:
		print("\n")
		uprint("TEXT: ",tweets['text'])
		print("CREATED AT: ", tweets['created_at'],"\n\n")
	exit+=1