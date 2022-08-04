# The program will prompt for a URL, read the XML data from a URL
# using urllib and then parse and extract the comment counts from the
# XML data, compute the sum of the numbers in the file.

# You are to look through all the <comment> tags and find the <count>
# values sum the numbers.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(data)
nests = tree.findall('comments/comment')
suma = 0

for val in nests:
    suma += int(val.find('count').text)

print(suma)
