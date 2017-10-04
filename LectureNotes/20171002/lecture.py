from bs4 import BeautifulSoup
import urllib.request, urllib.error
site = open('html_doc.html')
soup = BeautifulSoup(site,'html.parser')
print(soup.find_all())
