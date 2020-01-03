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

url = 'http://py4e-data.dr-chuck.net/known_by_Zoubaeir.html'#'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#input('Enter - ')
maxloopcounter = int(input('Enter Loop count:'))
position= int(input('Enter position:'))
loopcounter=0
poscounter=1
linkname=''

while loopcounter< maxloopcounter:
    print('loopcounter, poscounter:',loopcounter,poscounter)
    poscounter=1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

        # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        if poscounter==position:
            #print('position, poscounter:',position, poscounter)
            url=tag.get('href', None)
            linkname=tag.contents[0]
            print("Retrieving:",url)

                    #print(tag.contents[0])

        poscounter=poscounter+1

    loopcounter=loopcounter+1

print(linkname)
