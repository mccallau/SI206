# Import statements
import unittest
import sqlite3
import requests
import json
import re
import tweepy
import twitter_info # still need this in the same directory, filled out
import sys #Had unicode encoding errors 
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)


consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Set up library to grab stuff from twitter with your authentication, and return it in a JSON format
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# And we've provided the setup for your cache. But we haven't written any functions for you, so you have to be sure that any function that gets data from the internet relies on caching.
CACHE_FNAME = "twitter_cache.json"
try:
    cache_file = open("UMSItwittercache.json",'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}

## [PART 1]

# Here, define a function called get_tweets that searches for all tweets referring to or by "umsi"
# Your function must cache data it retrieves and rely on a cache file!


def get_tweets(): # Part 1, if cache is not available, collects tweets from UMSI page and a 'umsi' twitter search
	if CACHE_DICTION == {}:
		UMSItweets = api.user_timeline(id="umsi",count=199) #Collected all tweets FROM umsi but not referring to umsi, grabbing the max 199 tweets from umsi
		umsisearch = api.search(q="@umsi",count=100)["statuses"] #Wanted to collect tweets referring to @umsi
		for tw1 in umsisearch: 
			if tw1["user"]["screen_name"] != "umsi": #Compensates for the fact that we already collected tweets FROM umsi, don't want duplicates
				UMSItweets.append(tw1)
		CACHE_DICTION["umsiuser"] = UMSItweets
		cachewrite = open("UMSItwittercache.json",'w')
		json.dump(CACHE_DICTION, cachewrite) 
		cachewrite.close()
	return CACHE_DICTION
			

## [PART 2]
# Create a database: tweets.sqlite,


# And then load all of those tweets you got from Twitter into a database table called Tweets, with the following columns in each row:

## tweet_id - containing the unique id that belongs to each tweet
## author - containing the screen name of the user who posted the tweet (note that even for RT'd tweets, it will be the person whose timeline it is)
## time_posted - containing the date/time value that represents when the tweet was posted (note that this should be a TIMESTAMP column data type!)
## tweet_text - containing the text that goes with that tweet
## retweets - containing the number that represents how many times the tweet has been retweeted

# Below we have provided interim outline suggestions for what to do, sequentially, in comments.

# 1 - Make a connection to a new database tweets.sqlite, and create a variable to hold the database cursor.
conn = sqlite3.connect('hw8.sqlite')
cur = conn.cursor()

# 2 - Write code to drop the Tweets table if it exists, and create the table (so you can run the program over and over), with the correct (4) column names and appropriate types for each.
# HINT: Remember that the time_posted column should be the TIMESTAMP data type!
cur.execute('DROP TABLE IF EXISTS Tweets')
cur.execute("CREATE TABLE Tweets (tweet_id INTEGER, author TEXT, time_posted TIMESTAMP, tweet_text TEXT, retweets INTEGER)")

# 3 - Invoke the function you defined above to get a list that represents a bunch of tweets from the UMSI timeline. Save those tweets in a variable called umsi_tweets.
umsi_tweets = get_tweets()["umsiuser"]

# 4 - Use a for loop, the cursor you defined above to execute INSERT statements, that insert the data from each of the tweets in umsi_tweets into the correct columns in each row of the Tweets database table.
for tweets in umsi_tweets:
	tup = (tweets["id"],tweets["user"]["screen_name"],tweets["created_at"],tweets["text"],tweets["retweet_count"])
	cur.execute('''INSERT INTO Tweets (tweet_id, author, time_posted, tweet_text, retweets) VALUES (?,?,?,?,?)''', tup)
#  5- Use the database connection to commit the changes to the database
conn.commit()

# You can check out whether it worked in the SQLite browser! (And with the tests.)

## [PART 3] - SQL statements
# Select all of the tweets (the full rows/tuples of information) from umsi_tweets and display the date and message of each tweet in the form:

    # Mon Oct 09 16:02:03 +0000 2017 - #MondayMotivation https://t.co/vLbZpH390b
    #
    # Mon Oct 09 15:45:45 +0000 2017 - RT @MikeRothCom: Beautiful morning at @UMich - It’s easy to forget to
    # take in the view while running from place to place @umichDLHS  @umich…
# Include the blank line between each tweet.
        
sqlstr = "SELECT tweet_id, author, time_posted, tweet_text, retweets FROM Tweets"
for obj in cur.execute(sqlstr):
	uprint(obj[2]," - ",obj[3],"\n")


# Select the author of all of the tweets (the full rows/tuples of information) that have been retweeted MORE
# than 2 times, and fetch them into the variable more_than_2_rts.
# Print the results
sqlstr = "SELECT tweet_id, author, time_posted, tweet_text, retweets FROM Tweets WHERE retweets > 2"
more_than_2_rts = []
for obj in cur.execute(sqlstr):
	more_than_2_rts.append(obj)
uprint(more_than_2_rts)
cur.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)