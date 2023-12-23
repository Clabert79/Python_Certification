print('---------------------')
print('Vari import')
print('---------------------')

from collections import Counter, defaultdict, OrderedDict

# import antigravity
import itertools
# vari tipi di modi di importare librerie
# come Stringa
import importlib
s = importlib.__import__('sys')

import sys
print(s is sys)
print(s.platform)
enc = importlib.import_module('encodings')
print(enc.__name__)
# ---------------------------------

print('---------------------')
print('Test loop item ...')
print('---------------------')

my_list_6 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a,b,c in my_list_6:
	print(a, b , c)

print('---------------------')

my_list_5 = [1, 2, 3]
I = iter(my_list_5)			# Obtain an iterator object from an iterable
print(I.__next__())			# Call iterator's next to advance to next item
print(next(I))
#----------------------------------

#inserendo il nome del modulo

module_name = "re"
my_module = importlib.__import__(module_name)
print('Hai importato il modulo', my_module .__name__)

print(sys.modules)
print('---------------------')

# *args(tutti i parametri in ingresso)  **kwargs(chiave velore)
def super_func(*args, **kwargs):
	print(args)
	print(kwargs)
	total = 0
	for item in kwargs.values():
		total += item
	return sum(args)

print(super_func(1,3,4,5,6, num1 = 7,num2 = 8))
print("----------------------")

my_list = (1,2,3,4,5,6,7)

# Verifico se è iterabile un oggettp 
#---------------------------------------------------
if hasattr(my_list, '__iter__'):
	print(f'{my_list} is iterable')

from collections.abc import Iterable
if isinstance(my_list, Iterable):
	print(f"{my_list} is iterable")


#---------------------------------------------------

for item  in my_list:
	# nel caso si verifichi la condizione non esegue il codice seguente
	if(item == 2):
		continue
	# esce dal looop
	if(item == 6):
		break

	print(item)

print("----------------------")

for item  in my_list:
	if(item == 2):
		continue
	if(item == 6):
		break

	print(item)

for number in range(0 , 100):
	print(number)
for _ in range(0, 10, 2):
	print(_)
for _ in range(10, 0, -1):
	print(_)

i = 0
while i < 20:
	print(i)
	i += 1
	if i > 22:
		break
else:
	print('done with all the work') # viene stampato solo se vengono eseguiti tutti i loop


x = 0

while x < 5:
	print(f'the current number is {x}')
	x += 1
else:
	print('x is not less 5')

i1 = 0
while i1 < len(my_list):
	print(my_list[i1])
	i += 1
	break

some_list = ['a', 'b', 'c', 'd', 'f', 'n', 'n', 'a']

duplicate = []

for value in some_list:
	if some_list.count(value) > 1:
		if value not in duplicate:
			duplicate.append(value)

print(duplicate)


import operator

# notable_dates = [(20, 7 , 1969), (1966),(9, 11, 1989),(11, 1918),(25, 11,1915)]

# notable_dates.sort(key=operator.itemgetter(1))

notable_dates = [(20, 7 , 1969), (9, 11, 1989), (25, 11,1915), (11, 1918)]
getcount = operator.itemgetter(-1)

order_notable_dates = sorted(notable_dates, key=getcount)

print(order_notable_dates)

notable_dates_with_zero = [(20, 7 , 1969), (9, 11, 1989), (25, 11,1915), (11, 1918),()]

def last(seq):
	return seq(-1) if seq else 0

## notable_dates_with_zero.sort(key=lambda seq:seq[-1] else 0)
# order_notable_dates_with_zero = sorted(notable_dates_with_zero, key=lambda seq:seq[-1] else 0)

print(notable_dates_with_zero)


iterator = iter(range(5))

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
def g_wondrous(n):
	""" generatore di numeri HOTPO, a partire da N """
	while n!=1:
		yield n
		n = n // 2 if n% 2 == 0 else 3 * n + 1
	else:
		yield 1

## prende gli elementi per cui la funzione che passiMO è True
from itertools import dropwhile
for i in dropwhile(lambda num: num < 4,g_wondrous(29)):
	print(i)

for item in itertools.chain([1, 2, 3], 'abc', (11, 12, 13)):
	print(item)

#crea un oggetto iterabile
for item in itertools.chain.from_iterable([[1, 2, 3], 'abc', {'uno': 1, 'due': 2}]):
	print(item)

# per motivi di efficenza è più conveniente utilizzare 'itertools.chain.from_iterable()'
# che sum()

#iterazione inversa
for item in reversed(['a', 'b', 'c', 'd']):
	print(item)

simple_dict = {
    'a' : 1,
    'b' :2
}

my_dict_c1 = {key:value for key,value in simple_dict.items()}
print(my_dict_c1)

# sliching
print('---------------------------')
print('Slicing')
print('---------------------------')

sl = slice(4)
print(type(sl))

my_list_1 = list(range(10))
print(my_list_1[sl])

sl = slice(3, 10, 2)
print(sl.start)
print(sl.stop)
print(sl.step)

my_list_2 = ['a', 'b', 100, (1,2,3)]
my_list_2[0:2] = ['python'] # Inserisce 'python' al posto di mylist[0:2]
print(my_list_2)

my_list_2[0:1] = 'python' # Spacchetta la stringa 'python'
print(my_list_2)

del my_list_2[:6]

print(my_list_2)

my_list_3 = [1, 2, 3]
my_list_3 *= 3
print(my_list_3)

my_list_3 = [4, 5, 6]
my_list_3 = my_list_3 * 3
print(my_list_3)

# test veridicità
print(bool(''),bool(' '))

print(bool([]),bool(['']))

print(bool(()),bool(('',)))

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)

# solo numeri pari in un iterazione Generetor expression
# PEP-0289

for i in (x ** 2 for x in range(10) if x % 2 == 0):
	print(i, end =' ')

print(sum((x**2 for x in range(6) if x % 2 !=0 ), 20)) # aggiunge 10 alla somma

print(locals())


my_list_4 = [1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7,7]
print(Counter(my_list_4))
print(Counter(my_list_4).get(7))

squares = [x** 2 for x in [1,2,3,4,5,6]]
print(squares)
# equivalente
squares_1 = []
for x in [1,2,3,4,5,6]:
	squares_1.append(x ** 2)
print(squares_1)

#simula il ciclo until true

'''
while True:
	...loop body...
	if exitTest(): break
'''
'''
break
	Jumps out of the closest enclosing loop (past the entire loop statement)

continue
	Jumps to the top of the closest enclosing loop (to the loop’s header line)
pass
	Does nothing at all: it’s an empty statement placeholder
'''
print('----------------------------------------------------')

y = 11

x = y // 2
while x > 1:
	print('Test with ', x, ' ...')
	if y % x == 0:
		print(y, 'has factor', x)
		break
	x -= 1
else:
	print(y, 'is prime')

# DIZIONARI
diz_1 = {'a':1, 'b':2, 'c':3}

for key in diz_1.keys():
	print(key, diz_1[key])

iter_1 = iter(diz_1)

# mostra le chiavi
print(next(iter_1))
print(next(iter_1))
print(next(iter_1))

# test iterartor
R = range(3)

# next(R)  errore non è un iterartor

# in questo primo caso vengono creati 2 iterator separati
I1 = iter(R)
print(next(I1))
print(next(I1))

# in questo secondo l'iteratore è come se fosse uno non tiene le 2 iterazioni separate
I2 = iter(R)
print(next(I2))
print(next(I2))

Z = zip((1, 2, 3, 4), (10, 11, 12, 13), (100, 110, 120, 130), (1000, 1100, 1200, 1300), (10000, 11000, 12000, 13000))
I5 = iter(Z)
I6 = iter(Z)

print(next(I5))
print(next(I5))

print(next(I6))
print(next(I6))

M = map(abs, (-1, 0, 1))
I3 = iter(M); I4 = iter(M)
print(next(I3), next(I3), next(I4))

# print(next(I3)) va in errore perchè sono finiti gli elementi

R2 = range(3)
I7 = iter(R2); I8 = iter(R2)
print(next(I7), next(I7), next(I7))
print(next(I8), next(I8), next(I8))

D = dict(d=4, a=1 , c=3, b=2)
for (k, v) in D.items(): print(k, v, end=' ')

print("\n -----------------\n")
for k in sorted(D.keys()): print(k, D[k], end=' ')


iter_3 = [x ** 2 for x in range(4)] # List comprehension: build a list

iter_4 = (x ** 2 for x in range(4)) # Generator expression: make an iterable

iter_5 = list(x ** 2 for x in range(4)) # List comprehension equivalence

print(''.join(x.upper() for x in 'aaa,bbb,ccc'.split(',')))

import math
list_d = list(map(math.sqrt, (x ** 2 for x in range(4)))) # Nested combinations

print(list_d)

L, S = [1, 2, 3], 'spam'

print(S[1:] + ' - ' + S[:1])

def scramble_1(seq):
	res = []
	for i in range(len(seq)):
		res.append(seq[i:] + seq[:i])
	return res

print(scramble_1('spam'))

def scramble_2(seq):
	return[seq[i:] + seq[:i] for i in range(len(seq))]

print(scramble_2('spam'))


def permute(seq):
	print('--->', seq)
	if not seq:
		yield seq
	else:
		print('<---', seq)
		for i in range(len(seq)):
			rest = seq[:i] + seq[i+1:]
			for x in permute(rest):
				yield seq[i:i+1] + x

G = permute('abc')

print('>>', next(G))
print('>>',next(G))
print('>>',next(G))

my_list_7 = [1 ,2 ,3, 4]
my_list_8 = ['a' ,'b' ,'c' ,'d']
my_list_9 = [100, 200, 300, 400]

'''''
for item in zip(my_list_7, my_list_8, my_list_9):
	print(item)
'''

def myzip(*args):
	iters = list(map(iter, args)) # Allow multiple scans
	while iters:
		res = [next(i) for i in iters]
		yield tuple(res)

# print(list(myzip('abc', 'lmnop')))


X = 'aaa'
Y = 'bbb'
print(''.join(Z for Z in X + Y))


word = 'abcd'
for item in enumerate(word):
	print(item) #tuple

for index, letter in enumerate(word):
	print(index)
	print(letter)
	print('\n')


list(enumerate('spam'))

for i,char in enumerate(list(range(49,55))):
	print(i, char)
	if char == 50:
		print(f'index of range is {i}')

for i, char in enumerate('hello'):
	print(str(i) + ' - ' + char)


enumerate_1 = enumerate('spam')
iter_2 = iter(enumerate_1)

print(next(iter_2))
print(next(iter_2))

values = ["a", "b", "c"]
for value in values:
	print(value)


# index
# A il metodo più semplice per avere un indice

index = 0

for value in values:
	print(index, ":", value)
	index += 1

# B Secondo metodo con range che crea un indice al volo
# evitando il problema di doversi ricordare di tenerlo aggiornato

for index in range(len(values)):
	value = values[index]
	print(index, ":", value)


# C con enumerate non c'è bisogno di fare nulla di più questa è la python wy
for index, value in enumerate(values):
	print(index, ":", value)

i2 = 0
while i2 < 13:
	i2 += 1

	if(i2 == 5):
		print("continue") # in questa casistica non va alla fine del ciclo e riparte
		continue

	if(i2 == 10):
		print("break")
		break


	print("i ", " ---> ", i2)


largest = None
print('Befeore:', largest)
for intervar in [3, 42 ,34, 54 , 99, 23 ,57]:
	if largest is None or intervar > largest:
		largest = intervar
	print('Looop: ' , largest)



list13 = [10, -4, 1, 5, -2, 3]

result_1 = 0
for num in list13:
	if num > 0:
		result_1 += num

	print(result_1)
print("tot: ", result_1)

# con continue
result_2 = 0
for num in list13:
	#continue salta tutto il blocco successivo
	if num < 0:
		continue

	result_2 += num
	print(">> ", result_2)

print("tot: ", result_2)

for num in range(1, 5):
    print("*" * num)

list15 = [5, 2, 3, 4, 5, 6, 7, 8]

def sum_tree(L):
	tot = 0
	for x in L:
		print('--------->>>')
		if not isinstance(x, list):
			tot += x
		else:
			print('Tot partial: ' + tot )
			tot += sum_tree(x)
	return tot

print(sum_tree(list15))

'''
Test the relative speed of itaration tool alternatives
https://realpython.com/python-timer/
'''
# timer solo da Python 3.3

print("Test timer ....")


'''
Python’s enumerate() lets you write Pythonic for loops 
when you need a count and the value from an iterable. 
The big advantage of enumerate() is that it returns a tuple with the counter and value, 
so you don’t have to increment the counter yourself.

https://realpython.com/python-enumerate/#:~:text=Python's%20enumerate()%20lets%20you%20write%20Pythonic%20for%20loops%20when,to%20increment%20the%20counter%20yourself.

'''

list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]

for item in enumerate(list_names):
	name = item[1]
	start_chr = name[0]
	index = item[0]
	
	if start_chr == 'M':
		print(index)


list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

sum_even = 0

sum_odd = 0

for number in list_numbers:
	if number % 2 :

		sum_odd += number
	
	else:

		sum_even += number 

print("Odd ", sum_odd)
print("Even ", sum_even)

number = 10
while number >= 0:
    print(number)
    number -= 1

number = 50
while number >= 0:
    
    if (not number % 5) and (number is not 0) :
        print(f"This numeber {number} is divisible by 5 ")
        
    number -= 1


list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for number in list_numbers:
	if number < 0:
		break

	print(number)

my_list = list(range(2500, 2586)) #range deve essere inserito un numero maggiore di uno per visoualizzare il numero che ci interessa
print(my_list)

my_list = list(range(3, 301, 3))
print(my_list)

# TIPS

# NO
numbers = [10, 20, 33, 40]
for idx in range(len(numbers)):
	print(idx, numbers[idx])

# USE ENUMERATE
for idx,val in enumerate(numbers):
	print(idx, val)


#NO
a1 = [1, 2, 3]
b1 = ["a", "b", "c", "d"]

for idx in range(len(a1)):
	print(a1[idx], b1[idx])

#ZIP
for val_zip_1, val_zip_2 in zip(a1, b1):
	print(val_zip_1, val_zip_2)

# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

s = [ (1, 2), (3, 4, 5), (6, 7, 8, 9, 10) ]

for x,y, *extra in s:
	print(x)
	print(y)
	print(extra) # 1)[] 2)[5] 3) [8,9,10]
	print("-------------------")

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print(f"Verify user: {current_user}")
	confirmed_users.append(current_user)


print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
pets = ['cat','dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
	print("Remove ...")
	pets.remove('cat')# ne rimuove uno per volta

print(pets)

xs : list[int] = [10, 20, 30]
ind : int = 0
while ind < len(xs):
	item:int = xs[ind]
	print(ind, ' -- ' , item) 
	ind+=1

letters:list[str] = ['a', 'b', 'c', 'd', 'e', 'f']
for l in range(1, len(letters), 2):
	print(letters[l])
	
for l in range(0, len(letters)):
	print(l)
	print(letters[l])
#------------------------------------------------------
# STUDIO PERFORMANCE SUI LOOP LIST
#------------------------------------------------------

'''
Link:
https://towardsdatascience.com/the-art-of-speeding-up-python-loop-4970715717c


numpy
https://towardsdatascience.com/a-super-fast-way-to-loop-in-python-6e58ba377a00#:~:text=A%20faster%20way%20to%20loop%20in%20Python%20is%20using%20built,inside%20the%20range%20of%20numbers.
'''


