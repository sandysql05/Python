import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''




data1 = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

#using list
info1 = json.loads(data1)
print('User count:', len(info1))

print('User count:', info1)

for item in info1:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

print('____________________________')


info = json.loads(data)
print('User count:', len(info))
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
print('Number:', info["phone"]["number"])
print('Number Type:', info["phone"]["type"])
