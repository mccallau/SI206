import requests
import json
import sqlite3
import matplotlib.pyplot as plt
import datetime
import numpy as np
from pprint import pprint
import access_token #Fbook API access token
access_token = access_token.at
import sys #Had unicode encoding errors 
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)



try:
    f = open("fbcache.json",'r')
    fbcache = json.load(f)
    f.close()
except:
    baseurl = "https://graph.facebook.com/v2.9/me/"
    url_params = {}
    url_params["access_token"] = access_token
    url_params["fields"] = "posts.limit(1000)" #gets up to 1000 posts from FB
    fb_request = requests.get(baseurl,params=url_params)
    fbprecache = fb_request.json()
    fbcache = {"posts":[]}
    for obj in fbprecache["posts"]["data"]: #limits data that's kept to 100 posts from FB
        if len(fbcache["posts"])<100:
            fbcache["posts"].append(obj)
    f = open("fbcache.json",'w')
    json.dump(fbcache,f)
    f.close()

conn = sqlite3.connect('proj4.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Posts')
cur.execute("CREATE TABLE Posts (postid TEXT PRIMARY KEY,posttype TEXT,datetime TEXT,weekday TEXT)")

days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
postdays = []
for posts in fbcache["posts"]:
    dt = posts["created_time"].split("T")
    date = dt[0].split("-")
    time = dt[1].split(":")
    dt = datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]),int(time[2].split("+")[0]))
    tup = (posts["id"],list(posts.keys())[0],dt,days[dt.weekday()])
    postdays.append(days[dt.weekday()])
    cur.execute("INSERT INTO Posts (postid,posttype,datetime,weekday) VALUES (?,?,?,?)",tup)

conn.commit()
conn.close()

totalpostdays = (postdays.count("Monday"),postdays.count("Tuesday"),postdays.count("Wednesday"),postdays.count("Thursday"),
    postdays.count("Friday"),postdays.count("Saturday"),postdays.count("Sunday"))


plt.figure(figsize=(8, 4.5))
plt.bar(range(len(totalpostdays)),totalpostdays,tick_label=days)
plt.show()