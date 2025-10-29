
from collections import namedtuple
'''
Le tuple vengono usate al posto delle liste
quando abbiamo bisogno che l'oggetto non sia modificato
e quando ci serve avare delle performance migliori
alle tuple si puo' accedere per chiave

articolo interessante per approfondire le tuple nel modo di untillizzarle
https://medium.com/@venk.achintalwar/best-practices-and-common-mistakes-while-working-with-python-tuples-bfaa25bfdc90

'''

def min_max(t):
	return min(t), max(t)
def stampa_tutti(*args):
	print(args)
def corrispondenza_totale(t1,vt2):
	print(zip(t1, t2))
	for x,y in zip(t1, t2):
		print("x:" + str(t1) + " y:" + str(t2))
		if  x == y:
			return True

	return False


my_tuple_1 = (1, 3, 2, 6, 4, 5,4)
print('Count: ' + str(my_tuple_1.count(4)))
my_tuple_2 = ('b','a','r','a','t','t','o')
print('Index: ' + str(my_tuple_2.index('a')))

# sono immutabili
# my_tuple[1] = 'z' genera un errore
print(my_tuple_1[1])
print(5 in my_tuple_1)
print(my_tuple_1.index(4))
print(my_tuple_1.count(5))


## x1, y1, z1, *other = (1, 2, 3, 4, 5, 6) da capire perchè non funzione
# print(z1)
# print(other)


indirizzo = 'pippo@gmail.com'
nome, dominio = indirizzo.split("@")
print(nome + " " + dominio)
a, b = nome, dominio
print(a + " - "+ b)
quoziente, resto = divmod(7, 3)
print(str(quoziente) + "  " + str(resto))
t1 = divmod(97, 3)
print(min_max(t1))

stampa_tutti(1, 2.0, '3')
t2 = (7, 3)
divmod(*t2)

s = 'abc'
t3 = [0, 1, 2]
for coppia in zip(s,t3):
	print(coppia)

print(list(zip(s,t3)))

tupla1 = (1, 7, 3)
tupla2 = (1, 7, 5)
print(corrispondenza_totale(tupla1, tupla2))

print(list(zip('Anna', 'Edo')))
for indice, elemento in enumerate('ABCD'):
	print(indice, elemento)

diz1 = dict(zip('abcd',range(4)))
print(diz1)

tupla3 = (0, 'Ni', 1.2, 3)
print(tupla3.index('Ni'))
print(tupla3[tupla3.index('Ni')])

tupla4 = (1, 2) + (3, 4)
print(tupla4)
print(tupla4[0], tupla4[1:3])

tupla5 = (1, 2) * 4
print(tupla5)

T = ('cc', 'aa', 'dd', 'bb')
tmp1 = list(T)
tmp1.sort()
print(tmp1)

T = tuple(tmp1)
print(T)
sorted(T)
print(T)

# https://www.geeksforgeeks.org/namedtuple-in-python/
Student = namedtuple('Student',['name','age','DOB'])

S1 = Student('Nandini','19','2541997')

print ("The Student age using index is : ", end ="")
print (S1[1])

print ("The Student name using keyname is : ",end ="")
print (S1.name)

print ("All the fields of students are : ")
print (S1._fields)

'''
you construct a new object with slicing,
concatenation, and so on, and assign it back to the original reference, if needed:
'''

tupla6 = (1, 2, 3)
# tupla6[2] = 4 # Error!
tupla6 = tupla6[:2] + (4,) # OK: (1, 2, 4)

print(tupla6)
len(tupla6)

tupla7 = ("pippo1", "pippo2", "pippo3")

print(tupla7[-2])

print("ordinata", "->", tupla7)
l1 = list(tupla7)

from random import shuffle
shuffle(l1)


print("Random", "< >", l1)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#confronto tra tuple : confronta gli elenti dal primo al l'ultimo e se trova uno più grande smette
print((0, 1, 2) < (0, 3, 4))

#ordinamento
txt = 'but soft what light in yonder window breaks'
words = txt.split()

t = list()
for word in words:
	print(len(word), word)
	t.append((len(word), word))

t.sort(reverse = True)

res = list()
for lenght, word in t:
	res.append(word)

print(res)

tupla9 = ("pippo3", "pippo4", "pippo1","pippo2")

list9a = sorted(tupla9)

print(tupla9, "-", list9a)

guitar = ('fender','Stratocaster',1962,10000)

brand, model, year, price = guitar

print('Guitar: ',brand, model, year, price)


# crea una lista dei primi elementi
# che ragruppa tutto quello che eccede
*a, b, c = guitar

print(a, b, c)

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

numbers = 10, 20, 30 # crea una tupla
print(type(numbers))

r, g, *other = (192, 210, 100, 0.5)

print(r)
print(g)
print(other)

# he following example uses the * operator
# to unpack those tuples and merge them into a single

odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)

numbers = (*odd_numbers, *even_numbers)
print(numbers)


x_d = (7)
print(x_d, type(x_d))

x_d1 = (7,)
print(x_d1, type(x_d1), len(x_d1))


x_e = (1, 2, 3, 4, 6, 7)

a, *b, c = x_e

print(a, b, c)

a, b, c, d, *e = x_e

print(a, b, c, d, e)

'''
Note that the starred element receives all the surplus items as a list and that
if there are no surplus elements,
the starred element receives an empty list.
'''

[a, b] = [1, 2]
print([a, b])

# print([c, d] = 3, 4)

my_tuple = (1, 2, 3, 4) 

(a, b, c, d) = my_tuple

print(a, b, c, d)


porfolio = ((('AA', 100, 32.2), ('IBM', 50, 91.1)))

total = 0.0
for name, shares, price in porfolio:
	total += shares * price

print(f'The total is {total} ')

total = sum([shares * price for _,shares, price in porfolio])

print(f'The total is {total} ')

# hash() function on immutable objects like tuple

my_tuple_3 = (1, 2, 3, 4, 5)
cars = ('BMW', 'Audi', 'Ford', 'Fiat')

print('Hash value of my_tuple is:', hash(my_tuple_3))
print('Hash value of cars tuple is:', hash(cars))
#https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/built-in/hash/python-hash/

employee = ("Venkatesh", "Achintalwar", "Tech Lead", "New Delhi")
firstname, lastname, designation, city = employee
print(firstname +" " +lastname + " is a " +designation + " and lives in "+ city + "." )

'''
You can also create a tuple using a Python built-in function called tuple(). 
This is particularly useful when you want to convert a certain iterable (e.g., a list, range, string, etc.) to a tuple:
'''

print('----------------------------------')
print('SORT')
print('----------------------------------')
# https://realpython.com/sort-python-dictionary/
my_list = [2, 4, 6]
print(my_list)    # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'

people = {3:"jim", 2:"Jack", 4:"Jane", 1:"Jill"}

people_order = dict(sorted(people.items()))
print(people_order)

people_order_val = dict(sorted(people.items(), key=lambda item:item[1]))
print(people_order_val)


data = {
    193: {"name": "John", "age": 30, "skills": {"python": 8, "js": 7}},
    209: {"name": "Bill", "age": 15, "skills": {"python": 6}},
    746: {"name": "Jane", "age": 58, "skills": {"js": 2, "python": 5}},
    109: {"name": "Jill", "age": 83, "skills": {"java": 10}},
    984: {"name": "Jack", "age": 28, "skills": {"c": 8, "assembly": 7}},
    765: {"name": "Penelope", "age": 76, "skills": {"python": 8, "go": 5}},
    598: {"name": "Sylvia", "age": 62, "skills": {"bash": 8, "java": 7}},
    483: {"name": "Anna", "age": 24, "skills": {"js": 10}},
    277: {"name": "Beatriz", "age": 26, "skills": {"python": 2, "js": 4}},
}

def get_relevant_skills(item):
	""" Get the sum of Python and JavaScript skill"""
	skills = item[1]["skills"]

	#retutn default value that is equivalent to no skill
	return skills.get("python", 0 + skills.get("js", 0))

print(sorted(data.items(), key=get_relevant_skills, reverse=True))

#  namedtuple
# https://docs.python.org/3/library/collections.html#collections.namedtuple

from collections import namedtuple

Card = namedtuple('Card', ['face', 'suit'])
card = Card(face='Ace', suit='Spades')

print(card.face)
print(card.suit)

namedtuple_values = ['Queen', 'Hearts']
card_news = Card._make(namedtuple_values)

card._asdict() # restituisce un oggetto simile ad un dizionario OrderedDict([('face', 'Queen'), ('suit', 'Hearts')])