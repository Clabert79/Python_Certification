# https://docs.python.org/3/howto/functional.html

# https://www.youtube.com/playlist?list=PLP8GkvaIxJP1z5bu4NX_bFrEInBkAgTMr <<<
from functools import reduce

my_list = [1,2,3,5,6]

print("******************************************")
print('MAP')
print("******************************************")
'''
map permette di eseguire una funzione su una serie iterabile
'''

#1 Capitalize all of the pet names and print the list

print('Es. 1')
my_pets = ['sissi', 'bib', 'titti', 'pippo']

result_1 = list()
for pet in my_pets:
    result_1.append(pet.capitalize())

print(result_1)

def capitalize(string:str):
    return string.capitalize()

result_2 = list(map(capitalize, my_pets)) 
print(result_2)

result_3 = list(map(lambda pet: pet.capitalize(), my_pets))
print(result_3)


counters = [1, 2, 3, 4]
list(map((lambda x: x + 3), counters))

print('Es. 2')
print((pow(x, 2) for x in [1, 2, 3, 4]))  # Use () parens to generate items instead

print('Es. 3')
# in some cases, map may be faster to run than a list comprehension
print(list(map(pow, [1, 2, 3, 4],[2] * 4)))

print('Es. 4')
#esempio con molti parametri
print(list(map(pow, [1, 2, 3,],[2, 3, 4])))

print('Es. 5')

print(list(filter((lambda x: x > 0), range(-5, 5))))

# equal
[x for x in range(-5, 5) if x > 0]

print('Es. 6')
#square
my_list_4 = [5, 4, 3]
new_list_4 = list(map(lambda num: num**2, my_list_4))
print(new_list_4)

print("******************************************")
print('FILTER')
print("******************************************")

print('Es. 1')

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def is_smart_student(score):
    return score > 50

print(list(filter(is_smart_student, scores)))

print('Es. 2')
print(list(filter((lambda x: x % 2 == 0), range(5))))

print('Es. 2')
my_list_3 = [1,2,3,4,5,99,45,24]
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd,my_list_3)))
print(my_list_3)

print("******************************************")
print('LAMBDA')
print("******************************************")
#Lambda expression

#lambda par1, par2,..., parN: espressione

# lambda param: action(param)
print('Es 1')
print("-----------------------------------------------")
print(list(map(lambda item: item * 2, my_list )))

print(list(filter(lambda item: item % 2 !=0, my_list )))

print(reduce(lambda acc, item: acc + item, my_list ))
print("-----------------------------------------------")


print('Es 2')
print("-----------------------------------------------")
my_list_1 = [5, 4, 3]
new_list = list(map(lambda num: num**2, my_list_1))
print(new_list)

print('Es 3')
print("-----------------------------------------------")

my_list_2 = [(0, 2), (4, 3), (10, -1), (9, 9)]
my_list_2.sort()
print(my_list_2)

my_list_2.sort(key = lambda x: x[1]) # << da vedere
print(my_list_2)

#2 Zip the 2 list into a list of tuples, but sort thr numbers from lowest of highest

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

print("******************************************")
print('REDUCE')
print("******************************************")

'''
Combine all of numbers that are in a list on this file using reduce
It accepts an iterable to process,
but it’s not an iterable itself—it returns a single result.

from functools import reduce # Import in 3.X, not in 2.X <<

https://www.pythontutorial.net/python-basics/python-reduce-list/ <<<
https://www.youtube.com/watch?v=ZrZ6vJGiE8I <<<
'''

print('Es. 1')
def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))

print('Es. 2')
def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

print(reduce(accumulator, my_list, 10))
print(my_list)

print('Es. 3')

print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))
print((lambda x, y: x * y),[1,2,3,4])
# reduce((lambda x, y: x + y), [1, 2, 3, 4])

print('Es. 4')
import operator, functools
import itertools

res = functools.reduce(operator.add, [2,4,8])
print(type(res))
print(res)

res = functools.reduce((lambda x, y: x + y), [2, 4, 6])
print(type(res))
print(res)

print('Es. 5')

lis = [1, 3, 4, 10, 4]
print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(lis, lambda x, y: x+y)))

print("The summation of list using reduce is :", end="")
print(functools.reduce(lambda x, y: x+y, lis))

print('Es. 6')
scores = [75, 65, 80, 95, 50]
# no functional
total = 0
for score in scores:
    total += score
print('Total no reduce:', total)

from functools import reduce

def sum_reduce(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b

total_reduce = reduce(sum_reduce, scores)

print('total_reduce', total_reduce)

total_reduce_lambda = reduce(lambda a, b: a + b, scores)
print('total_reduce_lambda', total_reduce_lambda)


invitees = [{"email": "alex@example.com", "name": "Alex", "status": "attending"},
{"email": "brian@example.com", "name": "Brian", "status": "declined"},
{"email": "carol@example.com", "name": "Carol", "status": "pending"},
{"email": "david@example.com", "name": "David", "status": "attending"},
{"email": "maria@example.com", "name": "Maria", "status": "attending"}]

'''
Dont WORK
def transform_invitees_data(invitees):
    def trasform_data(acc, invitee):
        acc[invitee["mail"]] = invitee["status"]
    
    results = reduce(trasform_data, invitees, {})
    return results
'''


# print(transform_invitees_data(invitees)) Dont WORK

print("******************************************")
print('ZIP')
print("******************************************")

print('Es. 1')

# zip pairs items, truncates at shortest
s2 = 'abcde'
s3 ='xyz123'

print(list(zip(s2,s3)))

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]

# using zip() to map values
mapped = zip(name, roll_no)

print(list(mapped))

list_com_2 = list( map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(10))))
print(list_com_2)

capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

capitals_countries = list(zip(capitals,countries))

for record in capitals_countries:
    print(f"The capital of {record[1]} is {record[0]}")

print("-------->>> ", capitals_countries)

spanish_num = ("uno", "dos", "tres", "cuatro", "cinco")
portugues_num = ("um", "dois", "três", "quatro", "cinco")
english_num = ("one", "two", "three", "four", "five")

numbers = list(zip(spanish_num, portugues_num, english_num))

print("numbers -------->>> ", numbers)

products = {"apple":0.5, "pineapple": 0.7}
tech_prod = {"IPhone":1000, "Window":500}
products_and_tech = zip(products.values(), tech_prod)
prod_list = list(products_and_tech)
print(prod_list)

print("products_and_tech ZIP -------->>> ", prod_list)

print("******************************************")
print('My Function')
print("******************************************")

def my_map_1(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
        return res

print(my_map_1(abs, [-2,-1,0,1,2]))
print(my_map_1(pow, [1, 2, 3], [2, 3, 4, 5]))

def my_map_2(func, *seqs):
    res = []
    for args in zip(*seqs):
        yield func(*args)

def my_zip_1(*seqs):
    #crea una lista di liste
    seqs = [list(S) for S in seqs]
    print('seqs', seqs)
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
        print('res', res)
    return res

S1, S2 = 'abc', '1234'
print(my_zip_1(S1, S2))

print('my_zip_2')
def my_zip_2(*seqs):
                # crea un generatorn
    minlen = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]

print(my_zip_2(S1, S2))
# def my_map_pad(*seqs, pad = none):

nums = [1, 3, 6 , 8 , 12, 15]
square_01 = (x*x for x in nums) #create a generator

for n in square_01:
    print(n)

square_02 = map(lambda x: x*x, nums)

for n in square_02:
    print(n)

for n in filter(lambda x: x%2 == 0 ,nums):
    print(n)

'''
reduce() accumulates values left-to-right on the supplied iterable. 
This is known as a left-fold operation. 
Here is pseudocode for reduce(func, items, initial):

def reduce (func, items, initials):
    result = initials
    for item: items:
        result = func(result, item)
    return result
'''
from functools import reduce

total = reduce(lambda x, y: x + y, nums)
print(total)

product = reduce(lambda x, y: x * y, nums, 1)
print(product)

pairs = reduce(lambda x, y:(x,y), nums, None)
print(pairs)  


nums = [1, 2, 3, 4, 5, 6]

total = reduce(lambda x, y: x + y, nums)
product = reduce(lambda x, y: x * y, nums)

pairs = reduce(lambda x, y: (x, y), nums, None)
print(pairs)

numbers =[10, 9, 49, 1, 81, 2, 4, 8, 25, 12]

list_result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(list_result)

fahrenheit = [41, 32, 212]

list_result = list(map(lambda x: (x, (x -32) * 5/9), fahrenheit))
print(list_result)

colors = ['Rosso', 'arancione', 'Giallo', 'verde', 'Blu']
print(min(colors, key=lambda s: s.lower()))

print(max(colors, key=lambda s: s.lower()))

names = ['Bob', 'Sue', 'Amanda']
grade_point_averages = [3.5, 4.0, 3.75]

#  zip permette di iterare su diversi iterabili nello stesso momento
for name, gpa in zip(names, grade_point_averages):
    print(f'Nome={name}; Media={gpa}')

obj_zip = zip(names, grade_point_averages)

print(tuple(obj_zip))

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
countries = ['USA', 'UK', 'Canada']

data = list(zip(names, ages, countries))

format_data = [f">> Name: {name}, Age: {age}, Country: {country} <<" for name, age, country in data ]

print(format_data)

fruits = ['banana', 'apple', 'pear']
colors = ['yellow', 'red', 'green']

zipped = zip(fruits, colors)
unzipped_fruits, unzipped_colors = zip(*zipped)

print(unzipped_fruits)
print(unzipped_colors)

zipped_02 = zip(fruits, colors)

for zip0 in zipped_02:
    print(type(zip0), "----> ", zip0)

'''
output
<class 'tuple'> ---->  ('banana', 'yellow')
<class 'tuple'> ---->  ('apple', 'red')
<class 'tuple'> ---->  ('pear', 'green')
'''


# Without ZIP
a = [1, 2, 3, 4]
b = [1, 2, 3, 5]

are_equal = True
for i in range(len(a)):
    if a[i] != b[i]:
        are_equal = False

print(are_equal)

are_equal = True
#With ZIP
a = [1, 2, 3, 4]
b = [1, 2, 3, 5]

for num1, num2 in zip(a, b):
    if num1 != num2:
        are_equal = False

print(are_equal)


zip_obkect = zip(a, b)

print('type ', type(zip_obkect))
print('zip ', zip_obkect)

print(list(map(ord, 'spam'))) # ord() function returns the Unicode code point of a character
print([ord(x) for x in 'spam'])


l = list(map(lambda x: x ** 2, range(10)))

print(l)

list_result = [x for x in range(5) if x%2 == 0]
print(list_result)

# equivalente in forma più funzionale
list_result = list(filter((lambda x: x%2 == 0), range(5)))
print(list_result)

list_result = [x ** 2 for x in range(10) if x % 2 == 0]
print(list_result)

list_result = list(map((lambda x: x ** 2), filter((lambda x: x%2 == 0), range(10))))
print(list_result)