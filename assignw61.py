# The program will prompt for a URL, read the JSON data from a URL
# using urllib and then parse and extract the comment counts from the
# JSON data, compute the sum of the numbers in the file and enter the sum.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read()

tree = json.loads(data)
suma = 0

for nests in tree['comments']:
    suma += int(nests['count'])

print(suma)
