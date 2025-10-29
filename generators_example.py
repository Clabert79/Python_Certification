# riferimenti PEP-0255.
# riferimanti PEP- 0380.

from itertools import dropwhile
from itertools import islice

#PEP-0342.

print("-------------------------------------------------------")
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

G = (sum(row) for row in m)
print(next(G))
print(next(G))
print(next(G))
print("-------------------------------------------------------")

# funzione base di generators
def generator_function():
    for i in range(10):
        yield i

def wondrous(n):
    """ Resstituisci una lista di numeri HOTPO, a partire da n"""
    my_list = []
    while n!=1:
        my_list.append(n)
        n = n//2 if n%2 == 0 else 3*n + 1

    else:
        my_list.append(1)

    return my_list

for i in wondrous(5):
    print(i)

list_1 = list(wondrous(23))
print(list_1)

# prende come primo parametro una funzione e come secondo un iteratore
# per i quali fun(i) restituisce True
for i in dropwhile(lambda num: num > 4, wondrous(23)):
    print(i)

# intervallo di elementi
for i in islice(wondrous(23), 10, None):
    print(i)

for i in islice(wondrous(23), 0, 2):
    print(i)

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
def conteggio(n):
    i = 0
    while i <= n:
        yield i
        i += 1
for i in conteggio(10):
    print(i)

lista = list(conteggio(5))
print(lista)

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
def foo(seq):
    print("inizia l'esequzione ...")
    for item in seq:
        yield item
        print(item)

g = foo('a1cd')
print(type(g))

g.__next__()
g.__next__()

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

def g_wondrous(n):
    """ generatore di numeri HOTPO, a partire da N """
    while n!=1:
        yield n
        n = n // 2 if n% 2 == 0 else 3 * n + 1
    else:
        yield 1

g1 = g_wondrous(5)

print(g1.__next__())
print(g1.__next__())
print(g1.__next__())
g1.__next__()
print(g1.__next__())
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print("genearator expression")
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
my_list = [1, 3, 6]
a = (x**2 for x in my_list) ## genearator expressiona = (x**2 for x in my_list)
print(next(a))
print(next(a))
print(next(a))

# PEP-0342.

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print("Coroutine")
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

def c_foo():
    print("Inizia esecuzione del codice ...")
    while True:
        x = (yield)
        print(x)
        print("termina esecuzione")

c = c_foo()
print(c)
c.__next__()
c.send('Python')
c.send(1)

c.close()

def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        name = (yield)
        if prefix in name:
            print(name)

corou = print_name("Dear")
corou.__next__() ## ci deve essere se no va in errore
corou.send("Atul")
corou.send("Dear Atul")

print("-----------------------------")
print("Fibonacci")
print("-----------------------------")
def wondrous_of_fibonacci(n, start=1):
    a, b = start, start + 1
    while a < n:
        # si puo' omettere per una gestione più efficente

        # g = wondrous(a)
        # for item in g:
        #    yield item
        #
        yield from wondrous(a)
        a, b = b, a + b

print(list(wondrous_of_fibonacci(8)))


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator) ## stamap dove l'ogggetto è allocato
            print(next(iterator))
        except StopIteration:
            break

special_for([1, 2, 3, 4])

# Fibonacci example
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(10):
    print(x)


def wondrous(n):
    """ Resstituisci una lista di numeri HOTPO, a partire da n"""
    my_list = []
    while n!=1:
        my_list.append(n)
        n = n//2 if n%2 == 0 else 3*n + 1

    else:
        my_list.append(1)

    return my_list

for i in wondrous(5):
    print(i)

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
def conteggio(n):
    i = 0
    while i <= n:
        yield i
        i += 1
for i in conteggio(10):
    print(i)

lista = list(conteggio(5))
print(lista)

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
def foo(seq):
    print("inizia l'esequzione ...")
    for item in seq:
        yield item
        print(item)

g = foo('a1cd')
print(type(g))

g.__next__()
g.__next__()

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

def g_wondrous(n):
    """ generatore di numeri HOTPO, a partire da N """
    while n!=1:
        yield n
        n = n // 2 if n% 2 == 0 else 3 * n + 1
    else:
        yield 1

g1 = g_wondrous(5)

print(g1.__next__())
print(g1.__next__())
print(g1.__next__())
g1.__next__()
print(g1.__next__())
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print("genearator expression")
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
my_list = [1, 3, 6]
a = (x**2 for x in my_list) ## genearator expressiona = (x**2 for x in my_list)
print(next(a))
print(next(a))
print(next(a))



print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print("Coroutine")
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

def c_foo():
    print("Inizia esecuzione del codice ...")
    while True:
        x = (yield)
        print(x)
        print("termina esecuzione")

c = c_foo()
print(c)
c.__next__()
c.send('Python')
c.send(1)

c.close()

def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        name = (yield)
        if prefix in name:
            print(name)

corou = print_name("Dear")
corou.__next__() ## ci deve essere se no va in errore
corou.send("Atul")
corou.send("Dear Atul")


print('--------------------------------------------')
def gen(x):
    for i in range(x): yield i ** 2

G = gen(5)
print(G.__iter__() == G) # Both methods exist on the same object

I = iter(G)
print(next(I))
print(next(I))

print(list(gen(5))) # Iteration contexts automatically run iter and next

print('--------------------------------------------')

class Squares:                          # __iter__ + yield generator
    def __init__(self, start, stop):    # __next__ is automatic/implied
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

    def gen(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

for i in Squares(1, 5):
    print(i, end=' ')

# same result
for i in Squares(1, 5).gen():
    print(i, end=' ')


S = Squares(1, 5)
I = iter(S)

next(I)
next(I)
next(I)
next(I)
next(I)
# next(I)

# Multi active iterators
S1 = Squares(1, 5)
I1 = iter(S1)

print(next(I1)); print(next(I1))

I2 = iter(S1)

print(next(I2));
print(next(I1))


print('--------------------------------------------')
print('SEND')
print('--------------------------------------------')

def gen():
    for i in range(10):
        X = yield i
        print(X)

G_1 = gen()
next(G_1)
G_1.send(77)
print('--')
print(G_1.send(88))

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
# generatori comprehension
exampple_gen = (i/2 for i in [0, 9, 21, 32] if i < 30)
for item in exampple_gen:
    print(item)

exampple_gen_2 = ((i, i**2, i**3) for i in range(5))
for item in exampple_gen_2:
    print(item)

exampple_gen_3 =(('pari' if i % 2 == 0 else 'dispari') for i in range(4))
for item in exampple_gen_3:
    print(item)

# alcuni esempi compatti
print(sum(i for i in range(100)))

import time

def prime_numbers():
    n = 2
    yield(n, 0)
    while True:
        start_time = time.time()
        n += 1
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            end_time = time.time() - start_time
            yield(n, end_time)

# pip install matplotlib
import matplotlib.pyplot as plt

x = []
y = []


# In[59]:


prime_numbers = prime_numbers()


# In[60]:


for i in range(1000):
    result = next(prime_numbers)
    x.append(result[0])
    y.append(result[1])


# In[61]:


plt.plot(x,y)
plt.title("Time taken to calculate prime numbers")
plt.xlabel("Prime numbers")
plt.ylabel("Time in seconds")


