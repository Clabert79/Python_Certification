
# http://www.andreaminini.com/python/passaggio-molti-parametri-funzione-python

def func_1(c,d):
    print(c,d)
    return

a = 'foo'
b = 'bar'

func_1(a, b)

func_1(d = 'bar', c='foo') # verrà mantenuto la corrispondenza dei parametri


def func_2(*nomevar):
    print(nomevar)
    return

a = 'foo'
b = 'bar'
c = 'pippo'

func_2(a, b, c)

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4

# func(**args)                          # Same as func(a=1, b=2, c=3, d=4)
# func(*(1, 2), **{'d': 4, 'c': 3})     # Same as func(1, 2, d=4, c=3)
# func(1, *(2, 3), **{'d': 4})          # Same as func(1, 2, 3, d=4)
# func(1, c=3, *(2,), **{'d': 4})       # Same as func(1, 2, c=3, d=4)
# func(1, *(2, 3), d=4)                 # Same as func(1, 2, 3, d=4)
# func(1, *(2,), c=3, **{'d':4})        # Same as func(1, 2, c=3, d=4)

def adder(*num):
    sum = 0

    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)


def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)


'''
*args and **kwargs are special keyword which allows function to take variable length argument.
*args passes variable number of non-keyworded arguments list and on which operation of the list can be performed.
**kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.
*args and **kwargs make the function flexible.
'''

print('----------------------------------------')
# https://towardsdatascience.com/whats-the-difference-between-is-and-in-python-dc26406c85ad
# https://realpython.com/python-is-identity-vs-equality/

spam = 1234567899999999999999
maps = spam
eggs = 1234567899999999999999

# in questo caso spam e maps puntano allo stesso oggetto
print(spam is maps)
print(spam is maps)
print(spam is eggs) 
print(id(spam), id(maps), id(eggs))

print('----------------------------------------')

# the is statement is syntactic sugar ---> for id(a) == id(b)
pippo = "12345"
pippo_n = "12345"
pippo_c1 = pippo
pippo_c2 = pippo[:]

print("pippo is pippo_n ---> ", pippo is pippo_n)
print("pippo == pippo_n ---> ", pippo == pippo_n)

print("pippo is pippo_c1 ---> ", pippo is pippo_c1)
print("pippo == pippo_c1 ---> ", pippo == pippo_c1)

print("pippo is pippo_c2 ---> ", pippo is pippo_c2)
print("pippo == pippo_c2 ---> ", pippo == pippo_c2)


print("Explosion Variable ... ")

seq_01 = [1,2,3,4,]
a, b, c, d = seq_01
print("a, b, c, d ", " --> ", a, b, c, d)

a, *b = seq_01
print("a, *b", " --> ", a, b)


*a, b = seq_01
print("a, *b", " --> ", a, b)