from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
url = (input('Enter URL - ')).strip()
count = int(input('Enter Count - '))
position = int(input('Enter Position - '))
print("Retrieving URL: ",url)
for x in range(count):
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html,'html.parser')
	tags = soup('a')
	print("Retrieving URL: " ,tags[position-1].get("href",None))
	url = tags[position-1].get("href",None)