from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('span')
numlist = []
for strings in tags:
	numlist.append(int(strings.string))
print("Count: ",len(numlist))
print("Sum: ",sum(numlist))