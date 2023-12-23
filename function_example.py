'''
f.__name__ --> Function name

f.__qualname__ --> Fully qualified name (if nested)

f.__module__ --> Name of module in which defined

f.__doc__ --> Documentation string

f.__annotations__ --> Type hints

f.__globals__ --> Dictionary that is the global namespace

f.__closure__ -- Closure variables (if any)

f.__code__ --> Underlying code object

def func(*args, **kwargs):
    # args is a tuple of positional args
    # kwargs is dictionary of keyword args
    ...
'''

def foo1(a, b, c=3, d=4):
	print(a, b, c, d, sep='|')

foo1("primo",d="quarto",b="secondo")
# comportamento da tenere a mente nelle funzioni 
# il parametro di default è sempre lo stesso 
# quindi se sono oggetti mutabili verranno modificati semore gli stessi
def foo2(a=[1, 2, 3]):
	a.append(100)
	print(a)

foo2()
foo2()

def foo3(arg=None, value=0):
	arg=[] if arg == None else arg
	arg.append(value)
	return arg

print(foo3())
print(foo3())
print(foo3([1]))
print(foo3())

def foo4(*varargs):
	for element in varargs:
		print(element)

foo4('a', 'b', 'c', 'd', 'e')
foo4(1, 2, 3, 4, 5)

def foo5(a, b, c):
	print(a, b, c)

# se il numero degli elementi nell'oggeto iterabile 
# è = al numero di parametri viene spacchettato 
foo5(*[11, 22, 33])

def foo6(*varargs):
	for arg in varargs:
		print(arg, end='')

foo6(*range(4))
foo6(*range(5))

# trasforma i parametri in dizionario 
# (sempre in coda agli altri eventuali parametri)
def foo7(**kwargs):
	print(kwargs)

foo7()
foo7(a=1,c=22,e=333,z=7)

def foo8(a,*,b=3):
	print(a,b)

foo8('Python' ,b='2')
foo8('Python')

# equivalente
def foo9(a, **kwargs):
	b = kwargs.get('b',3) # se non esiste mette il default
	print(a,b)

foo9('Python' ,b='2')
foo9('Python')

def foo10(a, b, c):
	print(a, b, c)

foo10(**{'b':22, 'a':11, 'c':33})

# possiamo disenteressarci del numero dei parametri 
# (le chiavi devono essere stringe)

def foo11(**kwargs):
	for k, v in kwargs.items():
		print(k,v)

foo11(**{'nome':'pippo', 'anno':1985})

def say_hello(name='Darth Vader', side='sith'):
	print(f'hello {name} {side}')

say_hello()
say_hello("darth Maul")

say_hello('Yoda','jedi')
say_hello('sinth','duko')
say_hello(side='jedi',name='luke')


def min_1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

def min_2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first

def min_3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

print(min_1(3, 4, 1, 2))
print(min_2("bb", "aa"))
print(min_3([2,2], [1,1], [3,3]))

# Recursive
def mysum(L):
	if not L:
		return 0
	else:
		return L[0] + mysum(L[1:]) # Call myself recursively

print(mysum([1, 2, 3, 4, 5]))

# solution not recursive

list3 = [1, 2, 3, 4, 5]
sum = 0
for x in list3: sum += x
print(sum)
print('---------------------------')
def sum_tree(list_in):
	tot = 0
	items = list(list_in)
	while items:
		front = items.pop(0)
		if not isinstance(front, list):
			tot += front
		else:
			items[:0] = front
		print(tot)

	return tot

list4 = (1,2,3,4,5)

sum_tree(list4)


def make(label): # Make a function but don't call it
	def echo(message):
		print(label + ':' + message)
	return echo

F = make('Spam') # Label in enclosing scope is retained

F('Ham!')
F('Eggs!')

def func(d):
	e = 'spam'
	return d * e

print(func(8))

print(func.__name__)
print(dir(func))
print(func.__code__.co_varnames)
print(func.__code__.co_argcount)

print('partial function')

def multiply(a, b):
    return a*b

def double(a):
    return multiply(a,2)

result = double(10)
print(result)    

# functools.partial(fn, /, *args, **kwargs)
from functools import partial

triple = partial(multiply, b=3)

result = triple(10)
print(result)

def key_value_func(**kwargs):
	print("Key: ", kwargs.keys())
	print("Value: ", kwargs.values())

	for k in kwargs.keys():
		print(k)

key_value_func(name="mike", weight=200, age=27)

def key_list_items(key, **kwargs):
	value_list = kwargs[key]
	return value_list[-2]

result = key_list_items("people", things=['books', "tv", "shoes"], people=['pete', 'mike', 'jan'], age=[20, 30, 40])

print(result)


def read_data(filename, *, debug=False):
	return filename

# data = read_data('Data.csv', True)        # NO. TypeError
data = read_data('Data.csv', debug=True)  # Yes. Deve essere definito in maniera esplicita


# This means that all arguments appearing before the slash can only be specified by position
def func_02(x, y, /):
	pass

func_02(1, 2) 	# Ok
# func(1, y=2)   # Error

import time

def after(seconds, func, /, *args, **kargs):
	time.sleep(seconds)
	return func(*args, **kargs)

def duration(*, seconds, minutes, hours):
	return seconds + 60 * minutes + 3600 * hours

result = after(5, duration, seconds=20, minutes=3, hours=2)
print(result)

# Nested Function
def countdown(start):
	n = start
	def dispay():
		print('T-minun', n)
	def decrement():
		nonlocal n
		n -=1 #modifies the outer
	
	while n> 0:
		dispay()
		decrement()

countdown(20)


class Result:
	def __init__(self, value=None, exc=None) -> None:
		self._value = value
		self._exc = exc

	def result(self):
		if self._exc:
			raise self._exc
		else:
			return self._value
		

def after(seconds, func, *args) -> Result:
	time.sleep(seconds)

	try:
		return Result(value=func(*args))
	except Exception as err:
		return Result(exc=err)

def add(*arg):
	total = 0
	for n in arg:
		total += n

	return total

r = after(1, add, 2, 3)

print(r.result())

# s = after("1", add, "2", 3) #Immediatly raises a TypeError. Bad sleep() arg

t = after(1, add, "2", 3)
# print(t.result())  Raise Type error after exec 

# esempio di utiizzo con la concorrenza di primitive as esempio treads e processs

from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(16)

r = pool.submit(add, 2, 3)
print(r.result())

def add(x, y):
    def do_add():
        return x + y
    return do_add

a = add(2, 3)

print(a.__closure__)
print(a.__closure__[0].cell_contents)

import inspect
def func_sig(x: int, y:float, debug=False) -> float:
	pass

sig = inspect.signature(func_sig)
print(sig)


def func_local():
	y = 20
	locs = locals()
	locs['y'] = 30 # Try to change y

	print(locs['y'])   # Prints 30
	print(y)	# Prints 20


def spam(x, y):
	z = x + y
	grok(z)

import sys
def grok(a):
    b = a * 10
    print(sys._getframe(0).f_locals)    # myself
    print(sys._getframe(1).f_locals)    # my caller

print(inspect.currentframe().f_locals)

spam(2, 3)

'''
f.f_back Previous stack frame (toward the caller)

f.f_code Code object being executed

f.f_locals Dictionary of local variables (locals())

f.f_globals Dictionary used for global variables (globals())

f.f_builtins Dictionary used for built-in names

f.f_lineno Line number
'''

print('--------------------------------------------------------------')

from collections import ChainMap

def debug(*varnames):
	f = inspect.currentframe().f_back
	vars = ChainMap(f.f_locals, f.f_globals)

	print(f'{f.f_code.co_filename} : {f.f_lineno}')

	for name in varnames:
		print(f'   {name} = {vars[name]!r}')

#Examples use
def func_inspect(x, y):
	z = x + y
	debug('x', 'y')

	return z

print(func_inspect(5,7))

sig = inspect.signature(func_inspect)

print(sig)
print(list(sig.parameters))

for p in sig.parameters.values():
	print('name', p.name)
	print('Kind', p.kind)
	print('Default', p.default)

#crea in maniera dinamica una funzione

def make_init(*names):
	params = ','.join(names)
	code = f'def __init__(self, {params}):\n'
	for name in names:
		code += f' self.{name} = {name}\n'
	
	d = { }
	exec(code, d)
	return d['__init__']

# esempio
class Vecotr:
	__init__ = make_init('x', 'y', 'z')



