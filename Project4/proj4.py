import requests
import json
from pprint import pprint
import access_token #Fbook API access token

import sys #Had unicode encoding errors 
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

access_token = access_token.at

 
r = requests.get("https://graph.facebook.com/v2.3/me/feed",params={"limit":2, "access_token":access_token})

baseurl = "https://graph.facebook.com/v2.9/me/feed"

# Building the Facebook parameters dictionary
url_params = {}
url_params["access_token"] = access_token
url_params["fields"] = "comments{comments{like_count,from,message,created_time},like_count,from,message,created_time},likes,message,created_time,from" # Parameter key-value so you can get post message, comments, likes, etc. as described in assignment instructions.
url_params["limit"] = 1000

# Write code to make a request to the Facebook API using paging and save data in fb_data here.
fb_request = requests.get(baseurl,params=url_params)
fb_data = fb_request.json()
count=0
for mes in fb_data['data']:
    try:
        if mes['message'] and mes['from']['name']=="Austin McCall":
            mes['message'] 
            count+=1
    except:
        pass
print(count)