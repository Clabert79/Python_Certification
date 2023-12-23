import json
import sys
from tkinter.tix import Tree
print(sys.version_info)

# pip install requests
# import requests

''' import requests
https://realpython.com/python-json/

response = requests.get("https://jsonplaceholder.typicode.com/todos")
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
# print(response)
todos = json.loads(response.text)
'''

name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
print(rec)
json.dumps(rec) # serializza in memeoria

S = json.dumps(rec)
print(S)
O = json.loads(S)
print(O)
print(O == rec)

json.dump(rec, fp=open('testjson.txt', 'w'), indent=4) # serializza e scrive su disco
print(open('testjson.txt').read())
P = json.load(open('testjson.txt')) #legge dal file e trasforma in oggetto
print('Job:',P.get('job'))
print('Age:',type(P.get('age')))
print('----------------------------------------<<<<<<<')

data = {
    "president":{
        "name":"Zaphod Beebleborox",
        "species":"Betelgeusian"
    }
}

'''
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
'''

json_string = json.dumps(data, indent=4)

# print(json_string)

print('----------------------------------')

with open("data_file.json", "r") as read_file:
    data_f = json.load(read_file)

print(data_f)

x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
j_y = json.loads(x)
print(j_y["age"])

j_x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

j_y_1 = json.dumps(j_x)

print(j_y_1)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# ordina le chiavi
print(json.dumps(j_x, indent=4, sort_keys=True))


json_string_01 = '{"linguaggio": "python", "framework": "django"}'
json_dict = json.loads(json_string_01) # deserializza i valori in un dizionario
print(json_dict)
print(json_dict["linguaggio"])


with open("test.json") as json_file:
    json_data = json.load(json_file) # parsing da file

print(json_data)

json_data["test"] = "test1"
son_string_02 = json.dumps(json_data) # trasforma un oggetto in stringa

# scrive il file sulla macchina
with open("test_copy.json", "w") as json_file:
    json.dump(json_data, json_file)


data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
},
{ "id" : "009",
"x" : "7",
    "name" : "Brent"
  }
]'''


info = json.loads(data)
print('User count:', len(info))

for item in info:
    print(f"Name:{item['name']}")


json_string_02 =  '{"name": "John", "age": 30, "city": "New York"}'
json_dict_02 = json.loads(json_string_02)

print(type(json_dict_02))

json_string_03 = json.dumps(json_dict_02)

print(type(json_string_03))

# le stringhe sono uguali ma nella trasformazione vengono modificati gli spazi 
if json_string_02 == json_string_03:
    print("sono uguali !!!") 
else:
    print('json_string_02: ',json_string_02)
    print('json_string_03: ', json_string_03)

# trasformo il dizionario in un oggetto JSON
json_object_01 = json.dumps(json_dict_02, indent = 4, sort_keys=True)
print(type(json_object_01))
print(json_object_01)

# Esempio Advanced
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json = json.dumps(person)
# use different formatting style
person_json_format = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)
person_json2 = json.dumps(person, indent=4, sort_keys=True)

# the result is a JSON string:
print(person_json)
print(person_json_format)

person2 = json.loads(person_json2)

with open('person_test_2.json', 'w') as f:
    json.dump(person_json2, f, indent=2, sort_keys=True) # you can also specify indent etc...


with open('person_test_2.json', 'r') as f:
    person2x = json.load(f) #da file 'load' <<<

print('------>>>', person2)
#print('------>>>', person2x)

person3_json = """
{
    "age": 30,
    "city": "New York",
    "hasChildren": false,
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""
person3 = json.loads(person3_json) # da Stringa loads <<<<

# Working with Custom Objects


numbers = [2, 3, 5, 7, 11, 13]
contet = json.dumps(numbers)
print(type(contet)) # tipo stringa
print(contet)