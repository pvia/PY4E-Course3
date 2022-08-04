# The program will use urllib to read the HTML from the data files, 
# extract the href= vaues from the anchor tags, scan for a tag that is in a
# particular position relative to the first name in the list, follow that
# link and repeat the process a number of times and report the last
# name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

for i in range(7):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count + 1

        if count > 18:
            break
        url = tag.get('href', None)

print(url)
