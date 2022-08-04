#  The program will use urllib to read the HTML from the data files and
# parse the data, extracting numbers and compute the sum of the
# numbers in the file.

# You are to find all the <span> tags in the file and pull out the
# numbers from the tag and sum the numbers.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

numlist = []

tags = soup('span')
for tag in tags:
    tag = tag.decode().rstrip()
    nostr = re.findall('[0-9]+', tag)
    numlist.extend(nostr)

intgr = [int(i) for i in numlist]
suma = sum(intgr)

print(suma)
