import copy
import shelve


# https://www.youtube.com/watch?v=qX0qqEVpP5s
# https://www.youtube.com/watch?v=2B8Nh3pJEFE

def lookup_inverse(d, v):
	for k in d:
		if d[k] == v:
			return k
	raise LookupError()

#Ordinare un dizionario
#-------------------------------------------
diz_4 = {'a':1, 'b':2, 'c':3, 'f':5, 'e':6}
print(diz_4)
ks = list(diz_4.keys())
ks.sort()
print(ks)
for k in ks:
	print(k, '=>', diz_4[k])

print(diz_4)
for k in sorted(diz_4):
	print(k, '==>', diz_4[k])
#-------------------------------------------

d = {'nome':'pippo','professione':['studente','lavoratore']}
print(d['nome'])
print(len(d))

# test sulle chiavi
if not 'cognome' in d:
	print('no cognome')

if 'nome' in d:
	print("si nome")

##  un oggetto mutabile
d_num ={1:['uno'],2:['due','two']}
print(d_num)
d_num[3] = ['tre','three']
print(d_num)

# del cancella
del d_num[3]
print(d_num)

# i valori di un dizionario sono riferimenti ad oggetti

mylist = d_num[1]

print(mylist)
d_num[1].append('one')
print(mylist)

# si posso creare con la classe 'dict' un lista di chiavi valore

d_dict_a = dict([('colore','giallo'),('numero',33)])

print(d_dict_a)

# chiave velore

d_dict_b = dict(colore='giallo', numero=33)

print(d_dict_b)

print(len(d_num))

d_dict_c = dict(zip(['name', 'job', 'age'], ['Bob','dev',40]))
print (d_dict_c)

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
		'jobs': ['dev', 'mgr'],
		'age': 40.5}
rec['jobs'].append('janitor')

if not 'hobby' in rec:
	print("MISSING")

print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
diz_1 = {k:bin(k**2) for k in range(5) if k % 2 == 0}
print(diz_1)
print( [name for name in dir(dict) if not name.startswith('__')])
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
# ** funzione zip in python
s = 'ABCD' # oggetto itereabike
l = ["alfa", "beta", "gamma", "delta"]

for i in zip(s, l):
		print(i)
print("-----------------------------")

# A dictionary comprehension takes the form {key: value for (key, value) in iterable}
keys = ['a', 'b', 'c', 'd', 'e']

values = [1, 2, 3, 4, 5]

d_com_1 = {k:v for (k,v) in zip(keys, values)}
print(d_com_1)

d_com_2 = dict(zip(keys, values))

print(d_com_2)

d_com_3 = {k: bin(k**2) for k in range(5) if k % 2 == 0}

print(d_com_3)

d_com_4 = {x: x**2 for x in [1, 2, 3, 4, 5]}

print(d_com_4)

d_com_5 = {100:100, 'numeri':[1,2,3], 'lettere': ['a', 'b', 'c']}

d_com_6 = d_com_5.copy()

#stesso riferimentp
print(d_com_5["numeri"] is d_com_6["numeri"])

d_com_7 = copy.deepcopy(d_com_5)

#diverso riferimento
print(d_com_5["numeri"] is d_com_7["numeri"])

# se si accede a una chiave con esiste viene sollevata un'eccezione
# per gestirlo in maniera precisa usare il metodo GET

print(d_com_6.get("nessuno", "'nessono no esiste'"))

d_num_no_keys = {1:'uno', 2:'due'}

#cerca se esiste si comporta come un put se no lo inserisce con il valore di default
print(d_num_no_keys.setdefault(1))

#se non esiste aggiunge la chiave con valore none
print(d_num_no_keys.setdefault(3))
print(d_num_no_keys)

print(d_num_no_keys.setdefault(4, 'quattro'))
print(d_num_no_keys)

d_com_8 = dict(nome='Python', creatore='Guido')
print(d_com_8)

d_com_8.update(creatore='Guido van Rossum')
print(d_com_8)

d_com_8.update(versione='3.8')
print(d_com_8)

print(">>>>>>>> SORT <<<<<<<<<<<")
d_sort = {'a': 3, 'b': 2, 'c': 1}
print(d_sort)
k_d_list = list(d_sort.keys())
k_d_list.sort()

print(d_sort['a'])

for kx in d_sort:
	print(kx, '-->', d_sort[kx])


#Iterazione
d_com_9 = {11:'undici', 22:'ventidue', 33: 'trentatre'}
for k in d_com_9:
	print(k)

for k in sorted(d_com_9, reverse=True):
	print(k, d_com_9[k])

for v in d_com_9.values():
	print(v)

for item in d_com_9.items():
	print(item)

d_com_1a = dict(a=1,b=2,c=3)
for k1 in d_com_1a.keys():
	print(k1)
d_com_1b = dict(d=4,e=5)
# d_com_1b.keys() & d_com_1b.keys()

from collections import OrderedDict

#does not order the elements for you, it preserves the order you give it.
d_ord_1 = OrderedDict()
d_ord_1[33]= 'trentatre'
d_ord_1[22]= 'ventidue'
d_ord_1[24]='ventiquattro'

print(d_ord_1)

mydict = {'b':2,'a':1,'d':3,'c':4}

orddict = OrderedDict(mydict)

print(mydict)
print(orddict)
sort_dic = sorted(mydict.items())
print(sort_dic)
print(orddict)

mydict.popitem()
orddict.popitem(True)

print(mydict)
print(orddict)

user = {
	'basket':[1,2,3],
	'greet': 'hello',
	'name': 'pippo'
}
# se non esiste la chiave crea il default
print(user.get('age'),55)

#print('basket' in user)


print('Items ...')
for key, value in user.items():
	print("Key: " + str(key) + " Value: " + str(value) )

print('Values ...')
for val in user.values():
	print(val)

print('Keys ...')
for k in user.keys():
	print(k)

########################
#defaultdict
########################

from collections import defaultdict

def def_value():
	return '*'

dir_d = defaultdict(def_value)
dir_d["A"] = 1
dir_d["B"] = 2

print(dir_d["A"])
print(dir_d["B"])
print(dir_d["C"])

diz_2 = dict(a=1, b=2, c=3)
diz_3 = dict(a=2, d=4)

print(diz_2.keys() | diz_3.keys())
print(diz_2.keys() & diz_3.keys())

# esempio di serializzazione

shelf = shelve.open("myshelf")
shelf['name'] = 'Albert Eistein'
shelf['city'] = 'Ulm'
shelf.close()

shelf_2 = shelve.open('myshelf')
print(shelf_2['name'])
print('**********************************')
print('SPACCHETTAMENTO')
print('**********************************')

def foo(**kwargs):
	for k, v in kwargs.items():
		print(k, v)

foo(**{'name':'mickey', 'nickname':'pisi', 'anno':1985})


dx = {'uno':1 ,'due':2, 'tre': 3}

print("--------->>", dx)

dx = {'quattro':4, 'uno':1 ,'due':2, 'tre': 3}

print(dx)

dx_1 = {10 : 'a',20 : 'b',}
dx_2 = {30 : 'c'}

l1 = dx_1.items()
l2  = dx_2.items()

dx_3 = dict(l1)
dx_3.update(l2)

print(dx_3)

# dict Comprehesion
a = 'python'
dx_4 = {k:ord(k) for k in a}
print(dx_4)

dx_5 = {'spam': 2, 'ham': 1, 'eggs': 3}

l3 = list(dx_5.values())
print(l3)

l4 = list(dx_5.items())
print(l4)

if dx_5.get("toast") == None:
	print('Not exist !')
	print(dx_5.get("toast"),4)

print(dx_5.get('spam'))

dx_5a = {'toast':4, 'muffin':5}
dx_5.update(dx_5a)
print(dx_5)
print(dx_5.pop('muffin')) #retsituisce il valore ma toglie l'elemento dal dizionario
print(dx_5)

table_movies = {'1975':'Holy Graal','1979':'Life of Brain','1983':'The Meaning of life'}
year = '1983'
movie = table_movies[year]
print(movie)

for year in table_movies:
	print(year + '\t' + table_movies[year])

table_movies = {'Holy Graal':'1975','Life of Brain':'1979','The Meaning of life':'1983'}

print(list(table_movies.items()))
selected_title = [title for (title, year) in table_movies.items() if year == '1975']
print(selected_title)

k_movie = 'Holy Graal'
print(table_movies[k_movie])

v_movie = '1975'
selected_movie = [key for (key, value) in table_movies.items() if value == v_movie]

print(selected_movie)

selected_movie = [key for key in table_movies.keys() if table_movies[key] == v_movie]

print(selected_movie)

d_dict_d =  {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(d_dict_d)

d_dict_e  = {x: x ** 2 for x in range(1,5)}
print(d_dict_e)

d_dict_f = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(d_dict_f)

d_dict_g = dict.fromkeys('spam')
print(d_dict_g)

d_dict_h = {'a': 1, 'b': 2, 'c': 3}
print(d_dict_h.keys() & d_dict_h.keys())
print(d_dict_h.keys() & {'b'})
print(d_dict_h.keys() & {'b': 1})
print(d_dict_h.keys() | {'b', 'c', 'd'})

flat = {'rooms' : 2, 'floor' :'3rd', 'bathrooms': 1, 'apartament' : 306}

print("Key: ", flat.keys())
print('rooms' in flat.keys())

print("Values: ",flat.values())
print('3rd' in flat.values())

print("Items: ",flat.items())


eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

print(eng2sp['two'])

len(eng2sp)

vals = list(eng2sp.values())

print('uno' in vals)

word = 'brontosaurus'
d = dict()
for c in word:
	d[c] = d.get(c, 0) + 1

print(d)

message = "Hello Sam!"
mytable = message.maketrans("S", "P")
print(mytable)
print(message.translate(mytable))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))

import string

line = 'Pippo Pippo cade dalla sedia, si rialza e cade di nuovo.'

counts = dict()

line = line.translate(line.maketrans('', '', string.punctuation))

print('Line', line)

line = line.lower()
words = line.split()

for word in words:
	if word not in counts:
		counts[word] = 1
	else:
		counts[word] += 1

print(counts)


# scorrere chiavi e valori

for key, val in list(counts.items()):
	print(key, val)


person = {}
type(person)
person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralf', 'Betty', 'Joel']
person['pets'] = {'dog':'Fido', 'cat':'Sox'}


print(person['children'])

print(person['pets']['cat'])


diz_5 = {int: 1, float: 2, bool: 3}

print(diz_5.values())

# deve essere trasformato in una lista

l5 = list(diz_5.values())

print(l5)

diz_6 = {'a': 10, 'b': 20, 'c': 30}

l6 = list(diz_6.items())

print(l6)

l7 = list(diz_6.keys())

print(l7)


diz_7 = {'a': 10, 'c': 20, 'f': 30}
diz_8 = {'b': 100, 'd': 400}

diz_7.update(diz_8)

print(diz_7)

#non modifica il riferimento a diz_7
diz_8.update([('m', 700), ('l', 800)])

print(diz_8)

diz_8 = {k:v**2 for k,v in zip(['a', 'b'], range(2))}

print(diz_8)


capitals = {"New York":"Albany"}
capitals["Texas"] = "Houston"
capitals["California"] = "Sacramento"

for state in capitals:
        print(f"The capital of {state} is {capitals[state]}")

for state, capital in capitals.items():
	print(f"The capital of {state} is {capital}")


diz_9 = {"brand": "fender", "model": "Telecaster", "prezzo": 1000}
print(diz_9.items())

for copy_element in diz_9.items():
	print(copy_element)


#per spacchettare gli elementi
for key, value in diz_9.items():
	print(key)
	print(value)

#comprehesion
diz_10 = {num: "even" if num % 2 == 0 else "odd" for num in range(1,20)}

for key, value in diz_10.items():
	print(key)
	print(value)


list12 = [["brand", "fender"], ["model", "Telecaster"], ["prize", 10000]]

diz_12 = {item[0]: item[1] for item in list12}

print(diz_12)

diz_13 = {key: value for key, value in list12}

if(diz_13 == diz_12):
	print(diz_13)

diz_14 = {'a':0, 'b':1, 'c':2, 'd':3}

diz_14_rev = {v :k.upper() for k,v in diz_14.items()}

print(diz_14_rev)

diz_15 = {
	"A":"B",
	"B":"H",
	"C":"A",
	"D":"Z"
}

list12 = [k for k in diz_15.keys() if k in diz_15.values()]
print(list12)

def funk(**kwargs):
	for k,v in kwargs.items():
		print(f"{k}, {v}")

# unpacking
diz_16 = {'a':1, 'b':2, 'c':3}
diz_17 = {'d':4, 'e':5, 'f':6}
#coppia shallow
diz_16_c = {**diz_16}

#union
diz_16_17 = {**diz_16, **diz_17}

# creo dei dizionari da liste con zip
stoks =["apple", "tesla", "meta"]
prices = [2175, 1127, 2750]

new_dict_zip = {stoks : prices for stoks,
				prices in zip(stoks, prices)
}

print(new_dict_zip)


my_dict = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}

dict_point = my_dict["points"]
print(my_dict["points"]["points2"][1])

my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}
my_dict.update(occupation = "Editor")
my_dict.update(age = 36)
my_dict.update(country = "Colombia")
print(my_dict)


dictionary_ages = {"Tony":55, "Paulie":42, "Meadow":78, "Vito":44, "Ralph":24, "Sarah":35, "Evan":19, "Jean":2 ,"Ned":49}
minimum_age = min(dictionary_ages.values())
print(minimum_age)
last_name = max(dictionary_ages)
print(last_name)
diz_18 = {1: 55, 2:[10, 20, 30], 3:{'s1':100,'s2':200}}
print(type(diz_18[2]), diz_18[2])

diz_19 = {'1':'a', '2':'b'}
print(diz_19)

diz_19[3] = 'c_n' # aggiunge un elemento al dizionario (int num: elemento)
print(diz_19)

diz_19 ['3'] = 'c'
print(diz_19)


#concatenare

diz_19.update(diz_18) # solo un elemento nei paramtri
print(diz_19)


diz_19a = {'k1': 1, 'k2': 2}
diz_19b = {'k1': 100, 'k3': 3, 'k4': 4}

diz_19a.update(k2=200, k3=3, k4=4) # aggiunge chiavi str e valori
print(diz_19a)

diz_19a.update([('k1', 100), ('k3', 300), ('k4', 400)])
print(diz_19a)

diz_19c = {'k1': 1, 'k2': 2}

keys_1 = ['k1', 'k3', 'k4']
values_1 = [100, 300, 400]

diz_19c.update(zip(keys_1, values_1))
print(diz_19c)
# print(d1z_19a | d1z_19b) da python 3.9
# print(d1z_19 | d1z_19a | d1z_19a) da python 3.9

A = {1, 2, 3,}
B = {4, 5, 6}

# checks if set A and set B are disjoint
print(A.isdisjoint(B))

diz_20_a = {1: 'One', 2: 'Two', 3: "Tre"}
diz_20_b = {0: 'zero', 1: 'one', 3:'Tree'}

diz_20_a.update(diz_20_b) # unisce i vari indici e sovrascrive indici uguali il secondo
print(diz_20_a)


#trasformare 2 liste in dizionario
names = ['pippo','luca', 'giovanni','francesco']
countries = ['italia', 'argentina', 'stati uniti', 'messico']
names_countries = dict(zip(names, countries))
print(names_countries)

'''
{} 			Creates an empty dictionary 								x={}
len			Returns the number of entries in a dictionary				len(x)
keys		Returns a view of all keys in a dictionary					x.keys()
values		Returns a view of all values in a dictionary				x.values()
items		Returns a view of all items in a dictionary					x.items()
del			Removes an entry from a dictionary							del(x[key])
in			Tests whether a key exists in a dictionary					'y'in x
get			Returns the value of a key or a configurable default		x.get('y', None)

setdefault	Returns the value if the key is in the dictionary;			x.setdefault('y','') 
			otherwise, sets the value for the key to the default 
			and returns the value

copy		Makes a shallow copy of a dictionary						y = x.copy()
update		Combines the entries of two dictionaries					x.update(z)
'''

dictionary = {"Zat": "chat", "Pog": "chien", "porse": "heval"} #restituisce l'ordine delle chiavi

dic_sorted = sorted(dictionary)  #restituisce l'ordine delle chiavi in una lista
print(type(dic_sorted))


dic_items = dictionary.items()
print(dic_items) # [('Zat', 'chat'), ('Pog', 'chien'), ('porse', 'heval')] assomiglia a d una lista di tuple


pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

if "zamek" in pol_eng_dictionary: # lavora sulle chiavi
    print("Yes")
else:
    print("No")

print(len(pol_eng_dictionary))    # outputs: 3
del pol_eng_dictionary["zamek"]    # remove an item
print(len(pol_eng_dictionary))    # outputs: 2


# d_dict_i = dict(5='Python', 6='Guido') non si puo' crearlo in questo modo
d_dict_i = {5:'Pyhton', 6:'Guido'}
print(type(d_dict_i.keys()))

dict_keys = d_dict_i.keys()

# print(dict_keys[5]) TypeError: 'dict_keys' object is not subscriptable
'''
You can resolve this error by first converting the dict_keys() object to a list object using the list() built-in method 
and then accessing the i-th element using indexing. This works because unlike dict_keys() objects, 
lists are subscriptable
'''

print('d_dict_i item key 1: ')
print(list(d_dict_i.keys())[1]) #lista di keys

d_dict_i_b = {'apples': 6, 'mangos': 3, 'onions': 5,
                  'garlic': 2, 'peaches': 4, 'melons': 3, 'elenco':[1, 2, 3]}

index = 0

for item in d_dict_i:
    if(index == 1):
        print('d_dict_i  item key using a for loop:')
        print(item)
    index = index + 1


d_dict_i.update(d_dict_i_b) # merge dictionaries
print(d_dict_i)
d_dict_i['elenco'] = [6, 3, 5]
print(d_dict_i_b)


# d_dict_l : dict[str, int] # non è bloccante

d_dict_l = dict()

d_dict_l["pippo"] = 1
d_dict_l["pluto"] = "pipppo"

print(d_dict_l)

#------------------------------------------------------
# https://pythonguides.com/python-dictionary-search-by-value/

import random
import urllib.request
import ssl
import time
# pip install PyOpenSSL

word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
# Create unverified context in SSL
context = ssl._create_unverified_context()
response = urllib.request.urlopen(word_url, context=context)

long_txt = response.read().decode()
words = long_txt.splitlines()

''' Initialize a dictionary with n key-value pairs. '''
dict_words = {}

for i in range(10_000_000):
    dict_words[i] = random.choice(words)


find_value =  'baaar'

dict_words[10_000_001] = find_value

# https://pynative.com/python-get-execution-time-of-program/
# print(dict_words)

print("Start es 1 ... ")
start_1 = time.time()

for key,val in dict_words.items():
	if val == find_value:
		break
end_1 = time.time()

elapsed_time = end_1  - start_1
print("End es 1 duration ------->>", elapsed_time)


print("Start es 2 ... ")  # comprension è  più veloce
start_2 = time.time()

result = [new_k for new_k in dict_words.items() if new_k[1] == find_value][0][0]

end_2 = time.time()

elapsed_time = end_2  - start_2
print(f"End {result} es 2 duration ------->> ", elapsed_time)


print("Start es 3 ... ") # questa versione con i filtri la sua velocità è molto migliorata con la versione 11
start_3 = time.time()

result = list(filter(lambda x: x[1] == find_value, dict_words.items()))[0][0]

end_3 = time.time()

elapsed_time = end_3  - start_3
print(f"End {result} es 3 duration ------->> ", elapsed_time)


print("Start es 4 ... ")  # questo metodo che sfrutta gli indici è 2 volte ancora più veloce
start_4 = time.time()

values = list(dict_words.values())
index = values.index(find_value)
result = list(dict_words.keys())[index]

end_4 = time.time()
elapsed_time = end_4  - start_4

print(f"End {result} es 4 duration ------->> ", elapsed_time)

# FILTER
dict_m = {8:'u',4:'t',9:'z',10:'j',5:'k',3:'s'}

new_filt = dict(filter(lambda val:val[0] % 3 == 0, dict_m.items()))

print(new_filt)

ages = [
    {'name': 'Evan', 'age': 25},
    {'name': 'John', 'age': 30},
    {'name': 'Jane', 'age': 27},
    {'name': 'Jack', 'age': 32},
]

filtered = list(filter(lambda x: x['age'] >= 30, ages))
print(filtered)

from typing import Dict

team: Dict[int, str] = {}
team[23] = "Jordan"
team[33] = "Pippen"
print(team)

team[22] = "Rodman"

# ------------------------------------------------
# DEFAULT DIC
# https://www.geeksforgeeks.org/defaultdict-in-python/ <<


d_dict_i_1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("Dictionary:") 
print(d_dict_i_1)
print(d_dict_i_1[1])

# Uncommenting this print(Dict[4])
# will raise a KeyError as the
# 4 is not present in the dictionary

from collections import defaultdict

# Function to return a default
# values for keys that is not
# present

d_dict_i_2 = defaultdict(lambda: "Not Present")  # accetta anche una funzione standard
d_dict_i_2["a"] = 1
d_dict_i_2["b"] = 2

print(d_dict_i_2["a"])
print(d_dict_i_2["b"])
print(d_dict_i_2["c"])


# __missing__(): This function is used to provide the default value for the dictionary.

# Provides the default value 
# for the key
print(d_dict_i_2.__missing__('a'))
print(d_dict_i_2.__missing__('d'))


# Defining a dict
d_dict_i_3 = defaultdict(list)

for i in range(5):
    d_dict_i_3[i].append(i)

print("Dictionary with values as list:")
print(d_dict_i_3)
print(type(d_dict_i_3[0])) # LIst

#https://www.accelebrate.com/blog/using-defaultdict-python

d_dict_m_1 = { 'x': '1', 'y': '2', 'z': '3' } 
d_dict_m_2 = { 'x': '2', 'a': '2', 'z': '3' }

print(type(d_dict_m_2))
dict_inter = d_dict_m_1.keys() & d_dict_m_2.keys()
print(type(dict_inter)) # è di tipo SET
print(dict_inter)

# Key values can be any immutable object, such as strings, numbers, and "tuples"

d_dict_n = { }
d_dict_n[1,2,3] = "foo"
d_dict_n[1,0,3] = "bar"

print(type(d_dict_n))
print(d_dict_n)

fruits = {'apple': 40, 'grapes':50, 'orange':20}

ordered_fruit_list = sorted(fruits, key= lambda fruit:fruits[fruit])

print(ordered_fruit_list)


dictionary = {}
my_list = ['a', 'b', 'c', 'd']
 
for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )
 
for i in sorted(dictionary.keys()):
    k = dictionary[i]

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


names_and_countries_a = dict([('Adam', 'Argentina'),
                             ('Beth', 'Bulgaria'),
                             ('Charlie', 'Colombia'),
                             ('Dani', 'Denmark'),
                             ('Ethan', 'Estonia')])

names_and_countries_b = dict(Adam='Argentina',
                           Beth='Bulgaria',
                           Charlie='Colombia',
                           Dani='Denmark',
                           Ethan='Estonia')

names = ['Adam', 'Beth', 'Charlie', 'Dani', 'Ethan']
countries = ['Argentina', 'Bulgaria', 'Colombia', 'Denmark', 'Estonia']

names_and_countries_c = dict(zip(names, countries))

names_and_countries_copy = names_and_countries_c.copy()
print(names_and_countries_copy)

import copy
names_and_countries_deep_copy = copy.deepcopy(names_and_countries_c)
print(names_and_countries_deep_copy) 

from pprint import pprint
pprint(names_and_countries_deep_copy) #stampa più verticale


d_dict_i_2 = {'a': 97, 'b': 98}
print("setdefault() returned:", d_dict_i_2 .setdefault('b', 99)) 
#setdefault non sostiusce ma inserice
# restuisce il valore che trova

print("After using setdefault():", d_dict_i_2 )

people = ['Adam', 'Bella', 'Cara',
          'Adam', 'Bella', 'Cara',
          'Adam', 'Bella', 'Cara',]
food = ['soup', 'bruschetta', 'calamari',
        'burger', 'calzone', 'pizza',
        'coca-cola', 'fanta', 'water']
# Cost of each item in £
prices = [3.20, 4.50, 3.89,
          12.50, 15.00, 13.15,
          3.10, 2.95, 1.86]
# starter
# main
# drink
# Zip data together to allow iteration
# We only need info about the person and the price
meal_data = zip(people, prices)

total = {}
for (person, price) in meal_data:
    # get method returns 0 the first time we call it
    # and returns the current value subsequent times
    total[person] = total.get(person, 0) + price

print(total)
total.clear()

print(total)
for (person, price) in meal_data:
    # Set the initial value of person to 0
	total.setdefault(person, 0)
    # Increment by price
	total[person] += price


# https://realpython.com/python-defaultdict/#:~:text=Understanding%20the%20Python%20defaultdict%20Type,-The%20Python%20standard&text=So%2C%20you%20can%20say%20that,automatically%20given%20to%20that%20key%20.
from collections import defaultdict

print(set(dir(defaultdict)) - set(dir(dict))) # {'__copy__', 'default_factory', '__missing__'}
# .__copy__()	Provides support for copy.copy()
# .default_factory	Holds the callable invoked by .__missing__() to automatically provide default values for missing keys
# .__missing__(key)	Gets called when .__getitem__() can’t find key

# Initialise with int to do numerical incrementation
total_default = defaultdict(int)

# Increment exactly as we want to!
for (person, price) in meal_data:
    total[person] += price   

print(total_default)

print(total_default.get("foo"))

# no default
users = {
	'Nik':'Toronto',
	'Katie':'Toronto',
	'Evan':'London',
	'Kyra':'New York',
	'Jeff':'New York'
}

location_old = {}
for person, location in users.items():
	if location in location_old:
		location_old[location].append(person)
	else:
		location_old[location] = [person]

print(location_old)

# Now with defaultdict
location_default = defaultdict(list)
for person, location in users.items():
	location_default[location].append(person)

# in questo caso gestisce da solo la casistica e non c'è bisogno di checks
print(location_default)


from collections import Counter
counter = Counter('mississippi')
print(counter['i']) #type counter ma funziona come un dizionario

incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00),]

dd = defaultdict(float)
for product, income in incomes:
    dd[product] += income

for product, income in dd.items():
    print(f'Total income for {product}: ${income:,.2f}')
    

dd = defaultdict(list)
print(dd['missing']) # questo restituisce []
print(dd.get('another_missing')) # questo restituisce None
print(dd.__getitem__('another_missing')) # questo restituisce []

dd['string'] = 'some string'
dd['list'] # aggiunge questa chiave al dizionario con una lista vuota

print(dd)

# con .default_factory to None il dizionario si comporta come uno standard

'''
Note: You can assign any type of Python object using .setdefault(). 
This is an important difference compared to defaultdict 
if you consider that defaultdict only accepts a callable or None
'''

# differrenza di perfomance
from timeit import timeit

animals = [('cat', 1), ('rabbit', 2), ('cat', 3), ('dog', 4), ('dog', 1)]
std_dict = dict()
def_dict = defaultdict(list)

def group_with_dict():
    for animal, count in animals:
        std_dict.setdefault(animal, []).append(count)
    return std_dict

def group_with_defaultdict():
    for animal, count in animals:
        def_dict[animal].append(count)
    return def_dict

print(f'dict.setdefault() takes {timeit(group_with_dict)} seconds.')
print(f'defaultdict takes {timeit(group_with_defaultdict)} seconds.')

# come è internamente sviluppato il defaultdict

import collections
class my_defaultdict(collections.UserDict):
	def __init__(self, default_factory=None, *args, **kwargs):
		super().__init__(*args, **kwargs)
		if not callable(default_factory) and default_factory is not None:
			raise TypeError('first argument must be callable or None')
		self.default_factory = default_factory
	
	def __missing__(self, key):
		if self.default_factory is None:
			raise KeyError(key)
		if key not in self:
			self[key] = self.default_factory()
		return self[key]

# Passare una lambda
lst = [1, 1, 2, 1, 2, 2, 3, 4, 3, 3, 4, 4]
def_dict = defaultdict(lambda: 1)
for number in lst:
	def_dict[number] *= number

print(def_dict)

# Counter
from collections import Counter

def find_counts(list_of_elements):
	counts = Counter(list_of_elements)
	result = dict()
	for element, count in counts.items():
		result[count] = result.setdefault(count, []) + [element]

	return result

find_count = find_counts(["apple", "grapes", "apple", "watermelon", "apple","grapes", "grapes"])

print(find_count) # {3: ['apple', 'grapes'], 1: ['watermelon']}

people_weight_dict = {'jhon':134,
						'mike':170,
						'robert':165,
						'items':['ornage', {'k1':'some value'}],
						'tuple':(1, 2, 3, 4)
						}

print(people_weight_dict['items'][1]['k1'])

my_tuple = people_weight_dict['tuple']

print(type(my_tuple), "  " ,my_tuple)
employees = {"pippo":10000, "pluto":25000, "paperino":15000}

for key, value in employees.items():
	print(key)

# from typing import TypedDict # ???????????
# Movie = TypedDict('Movie', {'name': str, 'year': int})


#https://realpython.com/iterate-through-dictionary-python/
#change value int interaction

fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}
for fruit, price in fruits.items():
	fruits[fruit] = round(price * 0.9, 2)

print(fruits)

dict_01 = {"dog": "chien",  "horse": "cheval","cat": "chat"}
print(dict_01.keys())
dict_01_key_ord = sorted(dict_01.keys())
print(dict_01_key_ord)