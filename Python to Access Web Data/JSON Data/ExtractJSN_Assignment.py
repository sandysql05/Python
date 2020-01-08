import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

#if api_key is False:
#    api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/comments_339781.json'
    #input('Enter location: ')
#else :
#    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#while True:
#    address = input('Enter location: ')
#    if len(address) < 1: break

#    parms = dict()
#    parms['address'] = address
#    if api_key is not False: parms['key'] = api_key
url = serviceurl #+ urllib.parse.urlencode(parms)
print('Retrieving', url)
html = urllib.request.urlopen(url, context=ctx).read()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


info = json.loads(html)
print('User count:', len(info))
print(info)

print('**************************************************')

print(info["comments"])


Sum=0

for item in info["comments"]:
    Sum= Sum+int(item['count'])

print('Count:',len(info["comments"]))
print('Sum:',Sum)
    #print (item['name'], item['count'])
    #    print(key, value)
    #print(item["comments"])
        #print(item['count'])


#data = urllib.request.urlopen(url, context=ctx).read()

#info = json.loads(html)
#print('User count:', len(info))
#print(info)
