'''
def nome_funzione(lista_parametri):
    return espressione

    lambda lista_parametri: espressione

'''


'''
avvalersi delle lambda laddove serve una piccola funzione con utilizzo limitato a una espressione
'''

#lambda par1, par2,..., parN: espressione


names = ['pippo', 'pluto', 'paperino']
print(list(map(lambda x : x[::-1], names)))

# lambda argument1, argument2,... argumentN : expression using arguments

f = lambda x, y, z: x + y + z
print(f(1, 2, 3))

L = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

for f in L: print(f(2))
print(L[0](3))

# simile ad un print
import sys
showall = lambda x: list(map(sys.stdout.write, x))
t = showall(['spam\n', 'toast\n', 'eggs\n'])

# Nested
action = (lambda x: (lambda y: x + y))
act = action(99)

print(act(3))

res = ((lambda x: (lambda y: x + y))(99))(4)

print(res)

counters = [1, 2, 3, 4]

# senza lambda

updated = []
for x in counters:
    updated.append(x + 10)

print(updated)

# MAP

a_1 = [1,2,3,4,5,6,7]
a_2 = map(lambda x: x*x, a_1)
print(type(a_2))
a_3 = list(a_2)
print(type(a_3))

def inc(x): return x + 10
print(list(map(inc, counters))) # uso di map (uses of map are equivalent to for loops) *

def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res

print(list(map(inc, [1, 2, 3])))

print(mymap(inc, [1, 2, 3]))
pow(3, 4)                               # 3**4
list(map(pow, [1, 2, 3], [2, 3, 4]))    # 1**2, 2**3, 3**4

# è simile alla comprension
print(list(map(inc, [1, 2, 3, 4])))

print([inc(x) for x in [1, 2, 3, 4]]) # Use () parens to generate items instead

#-----------------------------------------------------------------------------------------

#REDUCE

def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally

print(myreduce((lambda x, y: x + y), [1, 2, 3, 4, 5]))
print(myreduce((lambda x, y: x * y), [1, 2, 3, 4, 5]))


# con lambda
list(map((lambda x: x + 3), counters))

list(filter((lambda x: x > 0), range(- 5, 5)))

print(list( map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(10))) ))

# --------------------------------------
# --------------------------------------
lambda x, y: x * y # Genera una funzione

f1 = lambda x,y:print(x * y)
f2 = lambda a,b,c: print(min(a, b, c))

f1(10, 11)
f2(100, 200, 30)

print(f1.__name__)
print(f2.__name__)

f3 = f = lambda a, b=2, *varargs, **kwargs: print(a, b, varargs, kwargs)

f3(1)

f3(1, 'due', 11, 22, 33, c=333, nome='python')

f4 = lambda *, x, y:  print(x + y)

f4(y=1, x=2)

notable_dates = [(20, 7, 1969), (1666,), (11, 1918), [9, 11, 1989], (25, 11, 1915), ()]

# ci serve solo per gestire il caso specifico usiamo la lambda senza dover definire una funzione
notable_dates = [(20, 7, 1969), (1666,), (11, 1918), [9, 11, 1989], (25, 11, 1915), ()]
notable_dates.sort(key=lambda seq:seq[-1] if seq else 0, reverse=True)
print(notable_dates)

func_list = [lambda x: x ** y for y in range(5)]
print([f(10) for f in func_list])


def maker(N):
    return lambda X: X ** N # lambda functions retain state too

h = maker(3) # mette la funzione nella variabile

print(h)
print(h(4)) # 4 ** 3 again



def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action

act = knights() # istanzia la funzione lambda
msg = act('Robin') # esegue l'azione
print(msg)
print(act)

L = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

for f in L: print(f(2))


print(L[0](3))

lower = (lambda x, y: x if x < y else y)
print(lower('bb', 'aa'))

punti_cartesiani = [(2,1), (4,2), (10,3), (3,9)]
# il paramtro key mi permette di modificare la chiave di ordinamento 
punti_cartesiani_ordinari = sorted(punti_cartesiani, key = lambda x: x[0] + x[1])
print(punti_cartesiani_ordinari)

i = 5 
add = lambda x: x+i
print(add(4))
lambda_functions = [lambda x: x+j for j in range(3)]
first_lambda_function = lambda_functions[0]

print(first_lambda_function(2)) #non funziona mette solo l'ultima perchè viene creata a run time
lambda_moltipication = lambda a, b: a*b

print(lambda_moltipication(5, 6))


l1 = [1, 2, 3, 4, 5]
final_list = list(map(lambda x : x**2, l1))

print(final_list)

max_lambda = lambda x,y: x if x > y else y
min_lambda = lambda x,y: x if x < y else y

print(max_lambda(9, 11))
print(min_lambda(9, 11))

fruits = {'apple':20, 'avocado':10, 'grapes':30, 'banana':15}
filtered_fruits = filter(lambda t:t[1] > 15, fruits.items())
print(type(filtered_fruits))
print(list(filtered_fruits))

filtered_fruits = filter(lambda t:t[1] > 15, fruits.items()) # vanno ricaricati i valori
print(dict(filtered_fruits))


# Find anagram

word = "code"
list_words = ["code", "deco", "ecod", "first", "strif", "frist"]

sorted_word = sorted(word)

result = list(filter(lambda x: sorted(x) == sorted_word, list_words))
print(result)

la = lambda x, y, z: (x + y) * z

r1 = la(2, 3, 5)
print(r1)

r2 = la(3, 3, 6)
print(r2)

x = 2
fun1 = lambda y: x * y
print(fun1(10))

x = 3
fun2 = lambda y: x * y

# late binding la x prende cmq l'ultimo valore

print(fun1(10))
print(fun2(10))

print('---------------------------------------')
print('per gestire il late binding:')
print('---------------------------------------')

x = 2
fun1 = lambda y, x=x: x * y

'''
x=x
This works because default argument values are only evaluated at the time of function definition
and thus would capture the current value of x
'''

x = 3
fun2 = lambda y, x=x: x * y

print(fun1(10))
print(fun2(10))

#closure
def make_greetings(names):
    funcs = []
    for name in names:
        funcs.append(lambda name=name: print('Hello ', name))

    return funcs

a, b, c = make_greetings(['Guido', 'Ada', 'Margaret'])

a()
b()
c()

x=2
f = lambda y, x=x: x * y
x=5
g = lambda y, x=x: x * y

print(f(10))       # --> prints 20
print(g(10))       # --> prints 50
