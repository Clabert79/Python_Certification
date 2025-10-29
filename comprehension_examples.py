#List, Dictionary, set

# [ expression for target in iterable ]


numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

print("List of ...")
for value in (x ** 2 for x in numbers if x % 2 != 0):
    print(value, end=' ')

squares_of_odds = (x ** 2 for x in numbers if x % 2 != 0)
print("Generator of ...")
for odd in (x ** 2 for x in squares_of_odds if x % 2 != 0):
    print(odd, end=' ')


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

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
res = [M[row][col] * N[row][col] for row in range(3) for col in range(3)]
print(res)

res = [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
print(res)

# Equivalente
res = []
for row in range(3):
    tmp = []
    for col in range(3):
        tmp.append(M[row][col] * N[row][col])
    res.append(tmp)

print(res)

res = []

res = [[col1 * col2 for (col1, col2) in zip(row1, row2)] for (row1, row2) in zip(M, N)]

print(res)

listoftuple = [('bob', 35, 'mgr'), ('sue', 40, 'dev')]

print([age for (name, age, job) in listoftuple])
print(list(map((lambda row: row[1]), listoftuple)))

['a' for i in range(10)] # stesso valore

[x ** 2 for x in range(10) if x % 2 == 0]

# print(list(map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(10)))))

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]

# print(res)

# Update in place
l7 = [[1, 2, 3], [4, 5, 6]]
for i in range(len(l7)):
    for j in range(len(l7[i])):
        l7[i][j] += 10

print(l7)

l8 = [[1, 2, 3], [4, 5, 6]]
l9 = [col + 10 for row in l8 for col in row]

print(l9)

l8 = [[col + 10 for col in row] for row in l8]

print(l8)

matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]


print([matrix_1[row][col] * matrix_2[row][col] for row in range(len(matrix_1)) for col in range(len(matrix_1))])
print([[matrix_1[row][col] * matrix_2[row][col] for col in range(3)] for row in range(3)])

# Equivalente con il ciclo for
res = []
for row in range(3):
    tmp = []
    for col in range(3):
        tmp.append(M[row][col] * N[row][col])

    res.append(tmp)

print(res)

print([[col1 * col2 for (col1, col2) in zip(row1, row2)] for (row1, row2) in zip(M, N)])

x = [1, 2, 3, 4]
x_squared = [item * item for item in x if item > 2]
print(x_squared)

x_squared_dict = {item: item * item for item in x}
print(x_squared_dict)


my_tuple = (1,2,3,4)
print(id(my_tuple))

my_tuple2 = (1,2,3)
print(id(my_tuple2))

vectors = [(1, 2), (3, 4), (5, 6)]

from math import sqrt

magnitudes = []

for vector in vectors:
    magnitude = sqrt(vector[0] ** 2 + vector[1] ** 2)
    magnitudes.append(magnitude)


magnitudes = [sqrt(vector[0] ** 2 + vector[1] ** 2) for vector in vectors]


m = [[ 1 if row == col else 0 for col in range(3)] for row in range(3)]
print(m)


# Dictionary comprehension
widgets = ['widget 1', 'widget 2', 'widget 3', 'widget 4']
sales = [10, 5, 15, 8]

d = {}
for i in range(len(widgets)):
    if sales[i] >= 0:
        d[widgets[i]] = sales[i]

# soluzione con comprehension
d = {widgets[i]: sales[i] 
     for i in range(len(widgets)) 
     if sales[i] >= 0
}

numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10] 
s = {number ** 2 for number in numbers if number % 2 == 0}
print(s)

res = []
for x in [0, 1, 2]:
    for y in [100, 200, 300]:
        res.append(x + y)
print(res)
#equivale

res = [x + y for x in [0, 1, 2, 3] for y in [100, 200, 300]]
print(res)

res = []

for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append((x, y))
print(res)

#equivale
res = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print(res)

res = []
for row in range(3):
    tmp = []
    for col in range(3):
        tmp.append(M[row][col] * N[row][col])
    res.append(tmp)

print(res)

#equivale
res = [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]

res = [M[row][col] * N[row][col] for row in range(3) for col in range(3)]
print(res)