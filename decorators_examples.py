# -----------------------------------------------------------------------

# https://www.freecodecamp.org/news/python-decorators-explained-with-examples/
# https://realpython.com/primer-on-python-decorators/

#Patterns Decorathors
"""
I decoratori permettono di scrivere questo codice

def foo():
    pass
foo = myfunction(foo)

in questo modo
@myfunction
def foo():
    pass

questa
def foo():
    pass
foo = myfunction(x, y)(foo)

equivale
@myfunction(x, y) def foo():
    pass
"""

import functools

def mydecorators_prototipe(f):
    @functools.wraps(f)
    def my_wrpper(*args, **kwargs):
        """ Wrpapper della funzione da decorare """
        print('Eseguo delle azioni prima di chiamare', f.__name__)
        result = f(*args, **kwargs)
        print('Eseguo altre azioni dopo aver chiamato',f.__name__)
        return result
    return my_wrpper

@mydecorators_prototipe
def foo(a, b):
    """ Restituisci a + b"""
    return a + b

foo(1, 2)

print(foo.__name__)
print(foo.__doc__)

# generic costrutors
def my_decorator(func):
    def wrap_func(*args, **kargs):
        func(*args, **args)
    return wrap_func


def hello():
    print("hellloooo!!")

#Le funzioni sono variabili
greet = hello
print(greet())

def hello_f(func):
    func()

def greet_f():
    print('still here')

a = hello_f(greet_f)
print(a)

def ex_decorator(func):
    def wrap_func(*args, **kwargs):
        print('***************')
        func(*args, **kwargs)
        print('***************')
    return wrap_func

# @ex_decorator
# def hello_d():
#    print("helloooo Decorators")

# hello_d()

#@ex_decorator
#def bye_d():
#    print("See you later")

#bye_d()

# hello_d_ex_1 = ex_decorator(hello)
# print(hello_d_ex_1())


@ex_decorator
def greet(greeting, emoji =':)'):
    print(greeting, emoji)

print(greet("fuck You"))

print('-------------------------------------')
from time import perf_counter_ns, time
def performance(fn):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = fn(*args, **kwargs)
    t2 = time()
    print(f'took {t2-t1}')
    return result
  return wrapper

@performance
def long_time():
    for i in range(10000):
        i*5

long_time()

# altro esempio
# questo modulo serve per non perdere il riferimento alla funzione originale
# https://www.programmareinpython.it/video-corso-python-intermedio/12-i-decoratori/

from functools import wraps

def caps_lock(function_parameter):
    @wraps(function_parameter)
    def wrapper(*args, **kwargs):
        return function_parameter(*args, **kwargs).upper()
    return wrapper

@caps_lock
def echo(msg):
    return msg

print(echo("I decoratori sono favolosi"))

def timer(fn):
    def wrapper(*args, **kwargs):
      #import interno
      from time import perf_counter
      start = perf_counter()
      result = fn(*args, **kwargs)
      stop = perf_counter()
      print(f"the function was active {stop - start} seconds")

      return result

    return wrapper


@timer
def func_3():
   pass

@timer
def func_4(a, b):
    print(a * b)
    return a * b

func_3()

def function_decorator(fun_parameters):

    @wraps(fun_parameters) # con questo decoratore non ri perdono i metadata come il nome
    def wrapper():
        """wrapper significa incartare"""
        print(f"... Codice eseguito prima di {fun_parameters.__name__} ...")
        fun_parameters()
        print(f"... Codice eseguito dopo di {fun_parameters.__name__} ...")
    return wrapper

@function_decorator
def my_function_test():
    print("Hello !!")


my_function_test()

# <<< senza la funzione wrap perde i riferimeti alla funzione originale 
print(f"Name Function with decorator: {my_function_test.__name__}")

# decorator factory
def repeat_for(times):

    def deco(func):
        def inner(*args, **kwargs):
            for x in range(times):
                func()

        return inner
    
    return deco

@repeat_for(4)
def alpha():
    print('alpha')

alpha()


from time import perf_counter

def decorator_factory(loops_num):

    def decorating(fn):
        def inner(num):
            total_elapsed = 0
            for i in range(loops_num):
                start = perf_counter()
                result = fn(num)
                end = perf_counter()
                total_elapsed += end - start

            avg_run_time = total_elapsed/loops_num
            print('result is', result)
            print('num of loops is', loops_num)
            print('avg time elapsed', avg_run_time)
        
        return inner
    return decorating

@decorator_factory(500)
def calc_factorial2(num):
    if num < 0:
        raise ValueError('Please use a number not smaller than 0')
    product = 1
    for i in range(num):
        product = product * (i+1)
    return product
calc_factorial2(4)


import logging
from math import sqrt
from time import perf_counter
from typing import Any, Callable


def with_logging(func: Callable[..., Any]) -> Callable[..., Any]:

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logging.info(f"Calling {func.__name__}")
        value = func(*args, **kwargs)
        logging.info(f"Finished {func.__name__}")
        return value

    return wrapper


def benchmark(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(f"Execution of {func.__name__} took {run_time:.2f} seconds.")
        return value

    return wrapper


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    
    value =  range(2, int(sqrt(number) + 1))

    for element in range(2, int(sqrt(number) + 1)):
        if number % element == 0:
            return False
    

    return True


@with_logging
@benchmark
def count_prime_numbers(upper_bound: int) -> int:
    count = 0
    for number in range(upper_bound):
        if is_prime(number):
            count += 1
    return count

def main() -> None:
    logging.basicConfig(level=logging.INFO)
    count_prime_numbers(50000)

if __name__ == "__main__":
    main()

#--------------------------------------------------------------
# Class Decorataor
#--------------------------------------------------------------
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{type(self).__name__}({self.x!r}, {self.y!r})'
'''

import inspect

def with_repr(cls):
    args = list(inspect.signature(cls).parameters)
    argvals = ', '.join('{self.%s!r}' % arg for arg in args)
    code = 'def __repr__(self):\n'
    code+= f'   return f"{cls.__name__}({argvals})"\n'
    locs = {}
    exec(code, locs)
    cls.__repr__=locs['__repr__']
    return cls

# Example

@with_repr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

'''
In this example, a __repr__() method is generated from the calling signature of the __init__() method. 
The method is created as a text string and passed to exec() to create a function. 
That function is attached to the class.
'''
p = Point(2, 3)
print(p)

from functools import wraps
def logged(func):
    # Idea:Give me a function, I' ll put logging
    # around it

    print('Adding logging to', func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('You called', func.__name__)
        return func(*args, **kwargs)
    
    # importando wraps questa parte non serve più
    #wrapper.__name__ = func.__name__
    #wrapper.__doc__ = func.__doc__

    return wrapper