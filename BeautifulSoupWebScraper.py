# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_tags(addr):
    html = urllib.request.urlopen(addr, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    # for tag in tags:
    #     print(tag.get('href', None))
    return tags


def find_name(addr, repeatCnt, tagPos):
    name = "na"
    for idx in range(repeatCnt):
        tags = get_tags(addr)
        tag = tags[tagPos-1]
        addr = tag['href']
        name = tag.text
    return name

# url = input('Enter - ')

# url = "http://py4e-data.dr-chuck.net/known_by_Fikret.htm"
# print(find_name(url, 4, 3))

url = "http://py4e-data.dr-chuck.net/known_by_Regina.html"
print(find_name(url, 7, 18))