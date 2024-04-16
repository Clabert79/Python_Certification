import sys

foo = (1, 2, 3)
print(foo.index(3)) # cerca l'elemento e retituisce l'indice se non esiste restuisce un valuerror

print(2 ** 3 ** 2 ** 1) # 2 elevato alla 9

#-----------------------------------------------------------------------------

x = float("2")
y = float("4")
print(y ** 0.5) # 2.0

print('Peter' 'Wellert') # unisce in automatico le 2 stringhe

x = 'Now'
y = 'just right'
print(f'{x} that is {y}!')

print('0000000000000000000000000000000000000000000000000000000000000000000000')

print(1//2*3)
# First, Python will evaluate 1 // 2, which is 0. Then, 0 * 3 = 0.
# Therefore the order of operations here is: ** -> // -> * -> / -> % -> +

x = 2
y = 4

x = x / y
print(x)
y = y / x
print(1 / 1)

zero = 0 % 2

print(zero)

x = 9
y = 12
result = x // 2 * 2 / 2 + y % 2 ** 3
print(result)     
print(9 // 2 * 2 / 2 + 12 % 2 ** 3)
print(9 // 2 * 2 / 2 + 12 % (2 ** 3))
print(9 // 2 * 2 / 2 + 12 % 8)
print((9 // 2) * 2 / 2 + 12 % 8)
print(4 * 2 / 2 + 12 % 8) 
print((4 * 2) / 2 + 12 % 8) 
print(8 / 2 + 12 % 8) 
print((8 / 2) + 12 % 8)
print(4.0 + 12 % 8) 
print(4.0 + (12 % 8))
print(4.0 + 4) 
print(8.0)   

print('1111111111111111111111111111111111111111111111111111111111111111111111')

my_list_1 = [1, 2, 3]
for v in range(len(my_list_1)):
    print(v)
    my_list_1.insert(1, my_list_1[v]) # inserisce 1 nelle posizioni 1,2,3

print(my_list_1)

print('222222222222222222222222222222222222222222222222222222222222222222222222')
i = 0
while i <= 3:
    i += 2
    print("*")

print('333333333333333333333333333333333333333333333333333333333333333333333333')

my_list_2 = [[0, 1, 2, 3] for i in range(2)]
print(my_list_2)
# print(my_list_2[2][0])

for i in range(1):
    print("*")
else:
    print("*")

my_list_3 = [i for i in range(-1, 2)]
print(my_list_3) # [-1, 0, 1]

print('444444444444444444444444444444444444444444444444444444444444444444444444')

t = [[3 - i for i in range(3) ] for j in range (3)]
s = 0
print(t)
for i in range (3):
    print("[i][i] ---->", t[i][i])
    s += t[i][i]

print(s)

print('555555555555555555555555555555555555555555555555555555555555555555555')
a = 1
b = 0

c = a & b # False 0
d = a | b # True 1
e = a ^ b # True 1

print("c -> ",c)
print("d -> ", d)
print("e -> ", e)

print(c + d + e)

print('66666666666666666666666666666666666666666666666666666666666666666666')

var = 1
while var < 10:
    print(var)
    print("#")
   
    var = var << 1 # moltiplica per 2

print('77777777777777777777777777777777777777777777777777777777777777777777')
i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break

    print("*")

print('888888888888888888888888888888888888888888888888888888888888888888888')

my_list_4 = [3, 1, -2]

my_list_4_b = my_list_4[4:5] # non va in errore ma la lista è vuota
print(my_list_4_b)

print(my_list_4[my_list_4[-1]])

print('99999999999999999999999999999999999999999999999999999999999999999999')

vals = [0, 1, 2]
vals.insert(0, 1) # insert aggiunge un elemento non lo sovrascrive
del vals[1]
print(vals)
total = 0
[total := total + x for x in vals]
print(total)

print('1010101010101010101010101010101010101010101010101010101010101010101010')

my_list_5 = [1, 2, 3]
my_list_5_b = []

for v in my_list_5:
    my_list_5_b.insert(0, v) #inverte l'ordine

print(my_list_5_b)

print('12121212121212121212121212121212121212121212121212121212121212121212121')

print('AAAAAAAAAAAAA-11111111111111111111111111111111111111111111111111111111')

my_list_6 = [1, 2, 3]
my_list_6_b = my_list_6[-2:-1]
my_list_6_c = my_list_6[-1:2] # non prende nulla pechè l'ultimo elelmento della selezione viene escluso

# print(my_list_6_b,my_list_6_c,)

ratings = [3.0, 4.7, 6.3, 4.5, 6.7]
print(ratings[1:-2]) # [4.7, 6.3]
print(ratings[0:-4]) # [3.0]
print(ratings[-1:-4]) # []  quando si incircaino non recupara nulla

print('BBBBBBBBBBBB-11111111111111111111111111111111111111111111111111111111')

temp_list = [1, 2, 3]
for i in range(len(temp_list)):
    #prima posizione dove viene inserito , seconda dove
    temp_list.insert(i, 0) 
print(temp_list)

print('CCCCCCCCCCC-11111111111111111111111111111111111111111111111111111111')

# la prima lista è l'elemento mentre la seconda lista è il contenitore (qusnte volte viene insierito)
my_numbers = [[i for i in range(3)] for j in range(4)]
print(my_numbers)

values = [[3 - x for x in range(2)] for y in range(5)]
print("Values", values )

sum = 0.0
for row in values:
  for cell in row:
    sum += cell
 
print(sum)

print('DDDDDDDDDDDD-11111111111111111111111111111111111111111111111111111111')

my_list_7 = [0, 1, 2] * 3 + [0] # 9 elementi + 1 

print(my_list_7)
print(len(my_list_7)) 

print('EEEEEEEEEEEE-11111111111111111111111111111111111111111111111111111111')

vals = (1, 2, 3, 4)
vals = vals[1:-1]
print(vals)
vals = vals[1]
print(vals)

print('FFFFFFFFFF-11111111111111111111111111111111111111111111111111111111')
dictionary = {0: 'one', 1: 'two', 2: 'three'}
value = 0
for x in range(len(dictionary)):
    print(x)
    value = dictionary[x]

print(value)

print(dictionary[1])

print('GGGGGGGGGGG-11111111111111111111111111111111111111111111111111111111')

nicks = {'Adam': 'Smasher', 'Kate': 'k4t3', 'John': 'xJohnx'}
 
if 'k4t3' in nicks.keys():
  print('a')
 
if 'k4t3' in nicks.values():
  print('b')

print('HHHHHHHHHHH-11111111111111111111111111111111111111111111111111111111')

def list_sum(lst):
    s = 0

    if hasattr(lst, '__iter__'):
        for elem in lst:
            s += elem
        #modifica la lista esterna
        lst.append(s)

        return s
    else:
        return lst

my_list_8 = [5, 4, 3]

print(list_sum(my_list_8))
print(my_list_8)

print('L!LL!L!L!L!!L!L!L!L!L-11111111111111111111111111111111111111111111111111111111')

tup = (1, ) + (1, )
tup = tup + tup
print(tup)
print(len(tup))

tup = (1, 2, 3, 4, 8)
tup = tup[1:-1]
print("1 ->> ", tup)
tup = tup[0]
print("2 ->> ", tup)
'''
def fun_1(in = 3, out=3):  VA IN ERRORE perchè la variabile non si puo' chiamer "IN" <<
    ...

*****
attenzione agli input() passano delle stringhe perchè cerca di ingannarti su questp particolare


'''

print('LLLLLLLLLLLLLL-11111111111111111111111111111111111111111111111111111111')
dict_1 = {'one': 'two', 'three':'one', 'two':'three'}
v1 = dict_1['one']

for k in range(len(dict_1)):
    v1 = dict_1[v1]
    print("--->> ", v1)

print(v1)


print('MMMMMMMMMMMMMMMMM-11111111111111111111111111111111111111111111111111111111')

def func(x):
    global y_1
    y_1 = x * x
    return y_1

func(2)
print(y_1)


def func2(x=0):
    if x % 2 == 0:
        return 1
    else:
        return  #restituisce None

func2()

print('NNNNNNNNNNN-11111111111111111111111111111111111111111111111111111111')
def f1(x):
    if x == 0:
        return 0
    return x + f1(x -1)

print(f1(3))

print('OOOOOOOOOOOO-11111111111111111111111111111111111111111111111111111111')

tup = (1, 2, 4, 8)
tup = tup[1: -1]
tup = tup[0]
print(tup)

def any():
    print(var1 + 1, end='')

var1 = 1
any()
print(var1)

print('PPPPPPPPPPP-11111111111111111111111111111111111111111111111111111111')

boolean_test = 0

if boolean_test:
    print("True ---> ", boolean_test)
else:
    print("False ---> ", boolean_test) # '0' è False

boolean_test = 1
if boolean_test:
    print("True --->  ", boolean_test)
else:
    print("False ---> ", boolean_test)

boolean_test = -1 
if boolean_test:
    print("True ---> ", boolean_test)
else:
    print("False ---> ", boolean_test)


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a[2:5]     # [2, 3, 4]
a[:3]      # [0, 1, 2]
a[-3:]     # [7, 8, 9]
a[::2]     # [0, 2, 4, 6, 8 ]
a[::-2]    # [9, 7, 5, 3, 1 ]
a[0:5:2]   # [0, 2]
a[5:0:-2]  # [5, 3, 1]
a[:5:1]    # [0, 1, 2, 3, 4]

a[:5:-1]   # [9, 8, 7, 6]
a[5::1]    # [5, 6, 7, 8, 9]
a[5::-1]   # [5, 4, 3, 2, 1, 0]
a[5:0:-1]  # [5, 4, 3, 2, 1]”

print('QQQQQQQQQQQQQQQQQQ-11111111111111111111111111111111111111111111111111111111')
print(30.11E9)        # 30110000000.0 

# print(30E11.9)      # SyntaxError: invalid syntax
# print(30.11E9.0)    # SyntaxError: invalid syntax
# print(30.11*10^9)   # TypeError: unsupported operand ...

nums = [3, 4, 5, 20, 5, 25, 1, 3]
num = nums.pop(1)
print(num) # contiene il numere che viene estratto dalla lista

print(float('1.3'))

data = 'abbabadaadbbaccabc'
print(data.count('ab', 1))

x = 9
y = 12
result = x // 2 * 2 / 2 + y % 2 ** 3 # da ricordarsi la potenza ha precednza e se ci sono divisioni diventano float
print(result)

num2 = 4 / 2 # --> 2.0
print(type(num2))  # float

num3 = 4 // 2 # --> 2
print(type(num3)) # int

x = """
"""
print(len(x)) #1

print('RRRRRRRRRRRRRRRR-11111111111111111111111111111111111111111111111111111111')
data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
for i in range(0, 4):
    print(data[i].pop(), end=' ') # la funzione pop estrapola l'elemento 4

people = {}

print("--------")
 
def add_person(index):
    if index in people:
        people[index] += 1
    else:
        people[index] = 1
 
 
add_person('Peter')
add_person('Paul')
add_person('peter')
 
print(len(people))

a = [1, 2, 3, 4, 5]
print(a[3:0:-1])

def fun_exp(n):
    n **= n
    return n
print(fun_exp(3)) #27

data = {'1': '0', '0': '1'}
 
for d in data.values():
    print(d, end=' ')


data = [4, 2, 3, 2, 1]
res = data[0]
 
for d in data:
    if d < res:
        res = d
 
print(">> ", res)

print(">>>>>>>>>>>>>")
data = [[0, 1, 2, 3] for i in range(2)]
print(data)

print(">>>>>>>>>>>>>")
x = 1
while x < 10:
    print('*')
    x = x << 1

x = '\\\\'
print(len(x))

print(1 // 2 * 3)

print(chr(ord('z') - 2))

data = {}

def func(d, key, value):
    d[key] = value
 
 
print(func(data, '1', 'Peter'))

x = 1 + 1 // 2 + 1 / 2 + 2

print(x)

z = 3
y = 7
x = y == z and y > z or z > y and z != y     # False
print(x)                                     # False
print(7 == 3 and 7 > 3 or 3 > 7 and 3 != 7)  # False
print(False and True or False and True)      # False
print((False and True) or (False and True))  # False
print(False or False)                        # False
print(False)                                 # False

print('Peter' 'Wellert' 'pippp')

a = 10

bb = a <= 10 & 1 < a

print(bb)

bb = (a <= 10) & (1 < a)

print(bb)

vals = [0, 1, 2]
vals.insert(0, 1) #attezione che non sostituice un valore in quella posizione ma lo sostituisce
del vals[1]

print(30.11E9)          # 30110000000.0
print(30.11 * 10 ** 9)  # 30110000000.0
# print(30E11.9)        # SyntaxError: invalid syntax
# print(30.11E9.0)      # SyntaxError: invalid syntax
# print(30.11*10^9)     # TypeError: unsupported operand


x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)                          # 17.5

# Therefore the order of operations here is: ** -> / -> // -> + -> +
 
print(1 / 2 + 3 // 3 + (4 ** 2))  # 17.5
print(1 / 2 + 3 // 3 + 16)        # 17.5 
print((1 / 2) + 3 // 3 + 16)      # 17.5
print(0.5 + 3 // 3 + 16)          # 17.5
print(0.5 + (3 // 3) + 16)        # 17.5
print(0.5 + 1 + 16)               # 17.5
print((0.5 + 1) + 16)             # 17.5
print(1.5 + 16)                   # 17.5
print(17.5)                       # 17.5


 
print(5 + 4 / 2 - (1 + 3))        # 3.0 c'è la divisione che trasforma in float
print(5 + 2 - (1 + 3))            # 3 è int

# funzione pow
x = pow(5, 3, 10)
print("pow(5, 3, 10) --->", x)
print((5 * 5 * 5) % 10)

print('SSSSSSSSSSSSSSSSS-11111111111111111111111111111111111111111111111111111111')

x = 1
y = 1.0 
z = "1"

if x == y: # sono uguale
    print("One")

if x == int(z):
    print("Two")
elif x == y:
    print("Three")
else:   print("Four")


print('TTTTTTTTTTTTTTTTTTTTTT-11111111111111111111111111111111111111111111111111111111')

x = 1
y = 0
#   
print(((x == y) and (x == y))) # False
print(not (x == y)) # True
z = ((x == y) and (x == y)) or not(x == y)
print(False or True)# True
print(not(z))

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
#---

x_2 = 0
y_2 = 1
a_2 = x_2 ^ y_2
b_2 = x_2 | y_2
c_2 = x_2 & y_2

print(a_2 + b_2 + c_2)
'''
That's because: 
a = 0 ^ 1 = 1, 
b = 0 | 1 = 1, 
c = 0 & 1 = 0. 

Then: a + b + c = 1 + 1 + 0 = 2
'''





import sys
print('System Version')
print(sys.version)
x = 'Now'
y = 'just right'
print(f'{x} that is {y}!')

x = 2
y = 4

x = x / y
print(x)
y = y / x
print(1 / 1)

zero = 0 % 2

print(zero)

print('1111111111111111111111111111111111111111111111111111111111111111111111')

my_list_1 = [1, 2, 3]
for v in range(len(my_list_1)):
    print(v)
    my_list_1.insert(1, my_list_1[v]) # inserisce 1 nelle posizioni 1,2,3

print(my_list_1)

print('222222222222222222222222222222222222222222222222222222222222222222222222')
i = 0
while i <= 3:
    i += 2
    print("*")

print('333333333333333333333333333333333333333333333333333333333333333333333333')

my_list_2 = [[0, 1, 2, 3] for i in range(2)]
print(my_list_2)
# print(my_list_2[2][0])

for i in range(1):
    print("*")
else:
    print("*")

my_list_3 = [i for i in range(-1, 2)]
print(my_list_3) # [-1, 0, 1]

print('444444444444444444444444444444444444444444444444444444444444444444444444')

t = [[3 - i for i in range(3) ] for j in range (3)]
s = 0
print(t)
for i in range (3):
    print("[i][i] ---->", t[i][i])
    s += t[i][i]

print(s)

print('555555555555555555555555555555555555555555555555555555555555555555555')
a = 1
b = 0

c = a & b # False 0
d = a | b # True 1
e = a ^ b # True 1

print("c -> ",c)
print("d -> ", d)
print("e -> ", e)

print(c + d + e)

print('66666666666666666666666666666666666666666666666666666666666666666666')

var = 1
while var < 10:
    print(var)
    print("#")
   
    var = var << 1 # moltiplica per 2

print('77777777777777777777777777777777777777777777777777777777777777777777')
i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break

    print("*")

print('888888888888888888888888888888888888888888888888888888888888888888888')

my_list_4 = [3, 1, -2]

my_list_4_b = my_list_4[4:5] # non va in errore ma la lista è vuota
print(my_list_4_b)

print(my_list_4[my_list_4[-1]])

print('99999999999999999999999999999999999999999999999999999999999999999999')

vals = [0, 1, 2]
vals.insert(0, 1) # insert aggiunge un elemento non lo sovrascrive
del vals[1]
print(vals)

total = 0
# [total := total + x for x in vals]
print(total)

print('1010101010101010101010101010101010101010101010101010101010101010101010')

my_list_5 = [1, 2, 3]
my_list_5_b = []

for v in my_list_5:
    my_list_5_b.insert(0, v) #inverte l'ordine

print(my_list_5_b)

print('12121212121212121212121212121212121212121212121212121212121212121212121')

print('AAAAAAAAAAAAA-11111111111111111111111111111111111111111111111111111111')

my_list_6 = [1, 2, 3]
my_list_6_b = my_list_6[-2:-1]
my_list_6_c = my_list_6[-1:2] # non prende nulla pechè l'ultimo elelmento della selezione viene escluso

# print(my_list_6_b,my_list_6_c,)

ratings = [3.0, 4.7, 6.3, 4.5, 6.7]
print(ratings[1:-2]) # [4.7, 6.3]
print(ratings[0:-4]) # [3.0]
print(ratings[-1:-4]) # []  quando si incircaino non recupara nulla

print('BBBBBBBBBBBB-11111111111111111111111111111111111111111111111111111111')

temp_list = [1, 2, 3]
for i in range(len(temp_list)):
    #prima posizione dove viene inserito , seconda dove
    temp_list.insert(i, 0) 
print(temp_list)

print('CCCCCCCCCCC-11111111111111111111111111111111111111111111111111111111')

# la prima lista è l'elemento mentre la seconda lista è il contenitore (qusnte volte viene insierito)
my_numbers = [[i for i in range(3)] for j in range(4)]
print(my_numbers)

values = [[3 - x for x in range(2)] for y in range(5)]
print("Values", values )

sum = 0.0
for row in values:
  for cell in row:
    sum += cell
 
print(sum)

print('DDDDDDDDDDDD-11111111111111111111111111111111111111111111111111111111')

my_list_7 = [0, 1, 2] * 3 + [0] # 9 elementi + 1 

print(my_list_7)
print(len(my_list_7)) 

print('EEEEEEEEEEEE-11111111111111111111111111111111111111111111111111111111')

vals = (1, 2, 3, 4)
vals = vals[1:-1]
print(vals)
vals = vals[1]
print(vals)

print('FFFFFFFFFF-11111111111111111111111111111111111111111111111111111111')
dictionary = {0: 'one', 1: 'two', 2: 'three'}
value = 0
for x in range(len(dictionary)):
    print(x)
    value = dictionary[x]

print(value)

print(dictionary[1])

print('GGGGGGGGGGG-11111111111111111111111111111111111111111111111111111111')

nicks = {'Adam': 'Smasher', 'Kate': 'k4t3', 'John': 'xJohnx'}
 
if 'k4t3' in nicks.keys():
  print('a')
 
if 'k4t3' in nicks.values():
  print('b')

print('HHHHHHHHHHH-11111111111111111111111111111111111111111111111111111111')

def list_sum(lst):
    s = 0

    if hasattr(lst, '__iter__'):
        for elem in lst:
            s += elem
        #modifica la lista esterna
        lst.append(s)

        return s
    else:
        return lst

my_list_8 = [5, 4, 3]

print(list_sum(my_list_8))
print(my_list_8)

print('L!LL!L!L!L!!L!L!L!L!L-11111111111111111111111111111111111111111111111111111111')

tup = (1, ) + (1, )
tup = tup + tup
print(tup)
print(len(tup))

tup = (1, 2, 3, 4, 8)
tup = tup[1:-1]
print("1 ->> ", tup)
tup = tup[0]
print("2 ->> ", tup)
'''
def fun_1(in = 3, out=3):  VA IN ERRORE perchè la variabile non si puo' chiamer "IN" <<
    ...

*****
attenzione agli input() passano delle stringhe perchè cerca di ingannarti su questp particolare


'''

print('LLLLLLLLLLLLLL-11111111111111111111111111111111111111111111111111111111')
dict_1 = {'one': 'two', 'three':'one', 'two':'three'}
v1 = dict_1['one']

for k in range(len(dict_1)):
    v1 = dict_1[v1]
    print("--->> ", v1)

print(v1)


print('MMMMMMMMMMMMMMMMM-11111111111111111111111111111111111111111111111111111111')

def func(x):
    global y_1
    y_1 = x * x
    return y_1

func(2)
print(y_1)


def func2(x=0):
    if x % 2 == 0:
        return 1
    else:
        return  #restituisce None

func2()

print('NNNNNNNNNNN-11111111111111111111111111111111111111111111111111111111')
def f1(x):
    if x == 0:
        return 0
    return x + f1(x -1)

print(f1(3))

print('OOOOOOOOOOOO-11111111111111111111111111111111111111111111111111111111')

tup = (1, 2, 4, 8)
tup = tup[1: -1]
tup = tup[0]
print(tup)

def any():
    print(var1 + 1, end='')

var1 = 1
any()
print(var1)

print('PPPPPPPPPPP-11111111111111111111111111111111111111111111111111111111')


boolean_test = 0

if boolean_test:
    print("True ---> ", boolean_test)
else:
    print("False ---> ", boolean_test) # '0' è False

boolean_test = 1
if boolean_test:
    print("True --->  ", boolean_test)
else:
    print("False ---> ", boolean_test)

boolean_test = -1 
if boolean_test:
    print("True ---> ", boolean_test)
else:
    print("False ---> ", boolean_test)


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a[2:5]     # [2, 3, 4]
a[:3]      # [0, 1, 2]
a[-3:]     # [7, 8, 9]
a[::2]     # [0, 2, 4, 6, 8 ]
a[::-2]    # [9, 7, 5, 3, 1 ]
a[0:5:2]   # [0, 2]
a[5:0:-2]  # [5, 3, 1]
a[:5:1]    # [0, 1, 2, 3, 4]

a[:5:-1]   # [9, 8, 7, 6]
a[5::1]    # [5, 6, 7, 8, 9]
a[5::-1]   # [5, 4, 3, 2, 1, 0]
a[5:0:-1]  # [5, 4, 3, 2, 1]”

print('QQQQQQQQQQQQQQQQQQ-11111111111111111111111111111111111111111111111111111111')
print(30.11E9)        # 30110000000.0 

# print(30E11.9)      # SyntaxError: invalid syntax
# print(30.11E9.0)    # SyntaxError: invalid syntax
# print(30.11*10^9)   # TypeError: unsupported operand ...

nums = [3, 4, 5, 20, 5, 25, 1, 3]
num = nums.pop(1)
print(num) # contiene il numere che viene estratto dalla lista

print(float('1.3'))

data = 'abbabadaadbbaccabc'
print(data.count('ab', 1))

x = 9
y = 12
result = x // 2 * 2 / 2 + y % 2 ** 3 # da ricordarsi la potenza ha precednza e se ci sono divisioni diventano float
print(result)

num2 = 4 / 2 # --> 2.0
print(type(num2))  # float

num3 = 4 // 2 # --> 2
print(type(num3)) # int

x = """
"""
print(len(x)) #1

print('RRRRRRRRRRRRRRRR-11111111111111111111111111111111111111111111111111111111')
data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
for i in range(0, 4):
    print(data[i].pop(), end=' ') # la funzione pop estrapola l'elemento 4

people = {}

print("--------")
 
def add_person(index):
    if index in people:
        people[index] += 1
    else:
        people[index] = 1
 
 
add_person('Peter')
add_person('Paul')
add_person('peter')
 
print(len(people))

a = [1, 2, 3, 4, 5]
print(a[3:0:-1])

def fun_exp(n):
    n **= n
    return n
print(fun_exp(3)) #27

data = {'1': '0', '0': '1'}
 
for d in data.values():
    print(d, end=' ')


data = [4, 2, 3, 2, 1]
res = data[0]
 
for d in data:
    if d < res:
        res = d
 
print(">> ", res)



print(">>>>>>>>>>>>>")
data = [[0, 1, 2, 3] for i in range(2)]
print(data)

print(">>>>>>>>>>>>>")
x = 1
while x < 10:
    print('*')
    x = x << 1

x = '\\\\'
print(len(x))

print(1 // 2 * 3)

print(chr(ord('z') - 2))

data = {}

def func(d, key, value):
    d[key] = value
 
 
print(func(data, '1', 'Peter'))

x = 1 + 1 // 2 + 1 / 2 + 2

print(x)

z = 3
y = 7
x = y == z and y > z or z > y and z != y     # False
print(x)                                     # False
print(7 == 3 and 7 > 3 or 3 > 7 and 3 != 7)  # False
print(False and True or False and True)      # False
print((False and True) or (False and True))  # False
print(False or False)                        # False
print(False)                                 # False

print('Peter' 'Wellert' 'pippp')

a = 10

bb = a <= 10 & 1 < a

print(bb)

bb = (a <= 10) & (1 < a)

print(bb)

vals = [0, 1, 2]
vals.insert(0, 1) #attezione che non sostituice un valore in quella posizione ma lo sostituisce
del vals[1]

print(30.11E9)          # 30110000000.0
print(30.11 * 10 ** 9)  # 30110000000.0
# print(30E11.9)        # SyntaxError: invalid syntax
# print(30.11E9.0)      # SyntaxError: invalid syntax
# print(30.11*10^9)     # TypeError: unsupported operand



x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)                          # 17.5

# Therefore the order of operations here is: ** -> / -> // -> + -> +
 
print(1 / 2 + 3 // 3 + (4 ** 2))  # 17.5
print(1 / 2 + 3 // 3 + 16)        # 17.5 
print((1 / 2) + 3 // 3 + 16)      # 17.5
print(0.5 + 3 // 3 + 16)          # 17.5
print(0.5 + (3 // 3) + 16)        # 17.5
print(0.5 + 1 + 16)               # 17.5
print((0.5 + 1) + 16)             # 17.5
print(1.5 + 16)                   # 17.5
print(17.5)                       # 17.5


print(5 + 4 / 2 - (1 + 3))        # 3.0 c'è la divisione che trasforma in float
print(5 + 2 - (1 + 3))            # 3 è int

# funzione pow
x = pow(5, 3, 10)
print(x)
print((5 * 5 * 5) % 10)


xx = 1
yx = 0

zx = ((xx == yx) and (xx == yx)) or not(xx == yx)
print(not(zx)) # false

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print('SSSSSSSSSSSSSS-11111111111111111111111111111111111111111111111111111111')

def test(a, b, c, d):
    print("a", a, "b", b, "c", c, "d", d)

test(1,2,3,4) 
test(1,2,3, d=4)
test(a=1, b=2, c=3, d=4)
test(d=1, c=2, b=3, a=4)

# tutte le altre combinazioni vanno i errore
# test(a=1, b=2, c=3, 4) Errore
# test(1, 2, c=3, 4) Errore
# test(a=1, 2, 3, 4) Errore



print("a = x & y ", a)
print("b = x | y ", b)
print("c = ~x ", c)
print("d = x ^ 5 ", d)
print("e = x >> 2 ", e)
print("f = x << 2 ", f)

for i in range(-1, 1): # l'indice va da -1 a 0
    print(i, "#")

my_list_9 = [3, 1, -1]
my_list_9[-1] = my_list_9[-2]
print(my_list_9) #[3, 1, 1]

my_list_9 = [0 for i in range(1, 3)] # in pratica mette tanti 0 qunati sono gli elementi
print(my_list_9) #[0, 0]

print("--------------------------------")
for ind in range(1):
    print("#")
else:
    print("#")

my_list_10 = [1, 2, 3]
my_list_10_b = []

for v in my_list_10:
    my_list_10_b.insert(0, v)

print(my_list_10_b)

t = [[3-i for i in range(3)] for j in range(3)]
print("t --> ", t)
s = 0
for i in range(3):
    s +=t[i][i]
    print(s)

print("Final s --> ", s)

my_list_11 = [1, 2, 3]
for v in range(len(my_list_11)):
    my_list_11.insert(1, my_list_11[v])

print(my_list_11)

my_list_12 = [[0, 1, 2, 3] for i in range(2)]
# print(my_list_12[2][0]) error 
my_list_11 = [1, 2, 3]
vals = my_list_11[-1:-2]
print("Vals", vals)

var = 0
while var < 6:
    var +=1
    if var % 2 == 0:
        continue
    print("#")


my_list_12 = [i for i in range(-1, 2)]

print(my_list_12)

my_list_12 = [1, 2, 3, 4]
print(my_list_12[-3:-1]) # --> [2, 3]

for num in range(2, 11, 2):#(devo mettere 11 perchè range si ferma al numero precedente)
    print(num) # tutti i numeri pari fini a 10 compreso

'''
def fun(in=2, out=3): !!! "in" non puo' essere usato
	return in*out
'''

tup = (1, ) + (1, )
print(tup)
tup = tup + tup
print(tup)
print(len(tup))


def any():
	print(var, end='') # <-- non fa andare a capo
    
var = 1
any()
print(var) # 11

value = input("Enter value")
# print(value/value) typeError 
print("---------------------")
tup = (1,2,4,8)
tup = tup[-2:-1]
print(tup) # (4,)
tup = tup[-1]
print(tup)
print(tup)

print("---------------------")
a1 = 1
b0 = 0
a1 = a1 ^ b0
print(a1, b0) # 1 0
b0 = a1 ^ b0
print(a1, b0) # 1 1
a1 = a1 ^ b0
print(a1, b0) # 0 1

print(1 % 2) # 1

print("---------------------")
print("a", "b", "c", sep="sep")

print("---------------------")
dct = {'one':'two', 'three':'one', 'two':'three'}
v = dct['three']

for k in range(len(dct)):
    print(v)
    v = dct[v]

print("end -->", v)

data = [1, {}, (2,), (), {3}, [4, 5]]
points = 0
 
for i in range(len(data)):
    if type(data[i]) == list:
        points += 1
    elif type(data[i]) == tuple:
        points += 10
    elif type(data[i]) == set:
        points += 100
    elif type(data[i]) == dict:
        points += 1000
    else:
        points += 10000
 
print(points)


print(1 // 2) # 0

#-----------------------------------------------------------------

chr(ord('p') + 3) # aumeta la lettera in oridine alfabetico


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x[::2]) # [1, 3, 5, 7, 9]
x[::2] = 10, 20, 30, 40, 50 # devono avere lo stesso numero di elementi in questo caso 5
print(x[::2])

x = float('23.42')
tot = bool(x) + True
print(tot) # --> 2

list1 = ['Peter', 'Paul', 'Mary', 'Jane']
list2 = ['Peter', 'Paul', 'Mary', 'Jane']
 
print('list1 is not list2', list1 is not list2)
print('list1 != list2', list1 != list2)
 
list1 = list2
print(" After list1 = list2 ...")
print("list1 is not list2", list1 is not list2) # qui diventa False perchè adesso punta alla stessa area di memoria
print("list1 != list2", list1 != list2)

data = {}
data[1] = 1
data['1'] = 2
data[1.0] = 4 # questo sovrascrive l'indice 1
 

names = ['Peter', 'Paul', 'Mary', 'Jane', 'Steve']

names = names[2:] # parte dal terzo elemento Mary

res = []
for name in names:
    res.append(name[:3].upper()) # prende le prime 3 lettere

a = 1
b = 0
c = a & b
print("c = a & b ---> ", c)

d = a | b
print("d = a | b ---> ", d)

e = a ^ b
print("e = a ^ b ---> ", e)

print(c + d + e)


# Fare esercizi simile <<<<<
print((3 * (1 + 2) ** 2 - (2 ** 2) * 3))

str = 'Hello World'
print(str[::-1]) # la riporta speculare 'dlroW olleH' -<<<<<

print('------------------>>')
# Senza not scrive solo i valori
print(not 0) # True 0 è False in booleano
print(not 23) # False
print(not '') # True
print(not 'Peter') # False
print(not None) # True


