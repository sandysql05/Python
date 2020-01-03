import xml.etree.ElementTree as ET
import re
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print('Attr_Type:', tree.find('phone').get('type'))
print('Attr_Type:', tree.find('phone').text)
