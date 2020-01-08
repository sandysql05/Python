import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

url = input('Enter Location:')
#'http://py4e-data.dr-chuck.net/comments_42.xml'
#

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url, context=ctx).read()
Sum= 0
stuff = ET.fromstring(html)
lst = stuff.findall('comments/comment')
print(stuff)
for item in lst:
     Sum=Sum+int(item.find('count').text)
print('User count:', len(lst))
print('Sum:', Sum)
#for item in lst:
#    print('Name', item.find('name').text)
#    print('Id', item.find('id').text)
#    print('age', item.find('age').text)
#    print('Attribute', item.get('x'))
