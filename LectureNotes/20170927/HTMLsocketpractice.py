#sockets
#import socket
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('http://www.dr-chuck.com/page1.htm')) #protocol, then host, then document

# Request response cycle for web pages

from bs4 import BeautifulSoup#crummy.com
soup = BeautifulSoup()