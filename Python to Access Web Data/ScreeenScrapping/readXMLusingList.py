import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
      <age>26</age>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
      <age>27</age>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print(item)
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('age', item.find('age').text)
    print('Attribute', item.get('x'))
