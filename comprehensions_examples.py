#List, Dictionary, set

'''
[ expression for target1 in iterable1 if condition1 for target2 in iterable2 if condition2 ...
for targetN in iterableN if conditionN ]
'''
friends =  ["Rolf", "ruth", "charlie", "Jen"]
guests = ["josè", "Bob", "Rolf", "Charlie", "Micheal"]

friends_lower = [f.lower() for f in friends]

present_friends = [
    name.title() 
    for name in guests 
    if name.lower() in friends_lower
]

print(present_friends)

y = [x**2 for x in range(4)]
print(y)

names = ['pippo', 'pio', 'pluto', 'mio']

name_len_3 = [s.upper() for s in names if len(s) == 3]
print(name_len_3) 

# MATRIX
M = [[1, 2, 3], # A 3 × 3 matrix, as nested lists [4, 5, 6], # Code can span lines if bracketed
[7, 8, 9],[4,5,6]]

diag = [M[i][i] for i in [0, 1, 2]]
print(diag)

print('-------------------------------------------------------------------')
my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list)

# my_list = [param for param in iterable]
my_list_c1 = [char for char in 'hello']
print(my_list_c1)

my_list_c2 = [num for num in range(0, 100)]
print(my_list_c2)

my_list_c3 = [num**2 for num in range(0, 100)]
print(my_list_c3)

my_list_c4 = [num**2 for num in range(0, 100) if num % 2 == 0]
print(my_list_c4)

print('-------------------------------------------------------------------')

my_dir_c0 = {i : sum(M[i]) for i in range(3)}
print(my_dir_c0)

my_dir_c1 = {char for char in 'hello'}
print(my_dir_c1)

my_dir_c2 = {num for num in range(0, 100)}
print(my_dir_c2)

my_dir_c3 = {num**2 for num in range(0, 100)}
print(my_dir_c3)

my_dir_c4 = {num**2 for num in range(0, 100) if num % 2 == 0}
print(my_dir_c4)

# my_dict = {key:value for key,value in }
simple_dict = {
    'a' : 1,
    'b' :2
}
my_dict_c1 = {k:v ** 2 for k,v in simple_dict.items() if v % 2 == 0}

print(my_dict_c1)

some_list = ['a', 'b', 'b', 'c', 'd', 'c', 'b']

duplicated = [x for x in some_list if some_list.count(x) > 1]
print(duplicated)

# possono essere annidate
matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
transpose = [[row[i] for row in matrix] for i in range(4)]
print(transpose)

# another examples
my_list_c0 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col_2 = [row[1] for row in my_list_c0]

print('Col2: ' + str(col_2))

#-----------------------------
print([row[1] + 1 for row in my_list_c0])
print([row[1] for row in my_list_c0 if row[1] % 2 == 0])
print([[x, x**2, x / 2] for x in range(-6, 7, 2) if x % 2 == 0])

#-----------------------------

my_list_c5 = [x + y for x in 'abc' for y in 'lmn']
print(my_list_c5)

# Nested
print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])



l6 = [[num for num in range(0, 3)] for iteraction in range(0, 3)]

print(l6) #[[0, 1, 2], [0, 1, 2], [0, 1, 2]]

line = 'aa bbb c'

res = ''.join(x for x in line.split() if len(x) > 1)

#filter
res = ''.join(filter(lambda x: len(x) > 1, line.split()))

res = ''.join(x.upper() for x in line.split() if len(x) > 1)

#map
res =''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split())))


list_com = [ord(x) for x in 'spam']


print(sorted(x ** 2 for x in range(4)))
print(sorted((x ** 2 for x in range(4)), reverse=True))


line = 'aa,bbb,ccccc'
print(''.join([x.upper() for x in line.split(',')])) # Makes a pointless list
print(''.join(x.upper() for x in line.split(','))) # Generates results
print(''.join(map(str.upper, line.split(',')))) # Generates results
print(''.join(map(lambda x: x * 2, line.split(','))))

print(''.join(x.upper() for x in line.split(',') if len(x) > 3))
print(''.join(map(str.upper, filter(lambda x: len(x) > 3, line.split(',')))))

#dictionary
my_dict_c2 = {num:num*2 for num in [1,2,3]}
print(my_dict_c2)

some_list = ['a', 'b', 'b', 'c', 'd', 'n', 'd','n','n']
my_dict_c3 =  {k:some_list.count(k)  for k in some_list if some_list.count(k) > 1}

print(my_dict_c3)


temperature_fahrenheit = [32, 212, 275]

degrees_celsius = [(degrees_fahrenheit-32)*(5/9) for degrees_fahrenheit in temperature_fahrenheit]

print(degrees_celsius)

square = [n**2 for n in range(10)]
print(square)