# http://robyp.x10host.com/3/inspect.html##loaded
import inspect
import sys

from cat_foo import cat_foo_fun

def foo(a, b, c = 10, *vaargs, d=99, **kwargs):
    """ Esempio di docstring """
    e = [1, 2, 3]
    print(f)

    def moo():
        pass
    return moo

f = 100
moo = foo(1, 2)

print(foo.__name__)
print(foo.__qualname__)
print(moo.__name__)
print(foo.__defaults__)
print(foo.__kwdefaults__) # Argomenti keyword only di default

print(inspect.ismodule(cat_foo_fun))
print(inspect.isclass(cat_foo_fun))
print(inspect.isfunction(cat_foo_fun))

print(inspect.getdoc(cat_foo_fun))
print(inspect.isbuiltin(sum))
print(inspect.isbuiltin(sys))
#deve essere messo la funzione
print(inspect.getsource(cat_foo_fun))
