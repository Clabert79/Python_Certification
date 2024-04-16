# https://realpython.com/python-metaclasses/

# Possibili Use Case
# https://breadcrumbscollector.tech/when-to-use-metaclasses-in-python-5-interesting-use-cases/

for t in int, float, dict, list, tuple:
    print(type(t))

print(type(type))

class Foo:
    def show(self): # importante definire il paramtro dell'istanza
        print("hi")

x = Foo()

'''
x is an instance of class Foo.
Foo is an instance of the type metaclass.
type is also an instance of the type metaclass, so it is an instance of itself.
'''
print(type(x)) # <class '__main__.Foo'>
print(type(Foo)) # <class 'type'>

'''
You can also call type() with three arguments—type(<name>, <bases>, <dct>):
    - <name> specifies the class name. This becomes the __name__ attribute of the class.
    - <bases> specifies a tuple of the base classes from which the class inherits. 
    This becomes the __bases__ attribute of the class.
    
    - <dct> specifies a namespace dictionary containing definitions for the class body. 
    This becomes the __dict__ attribute of the class.

    Calling type() in this manner creates a new instance of the type metaclass. In other words, it dynamically creates a new class.
'''

FooMeta = type('Foo', (), {})
y = FooMeta()
print(y)
print(x)

Bar = type('Bar', (Foo,), dict(attr=100))

Test = type('Test', (Foo,), {"a1":5})
t = Test()
print(t.a1)
t.show()

# Creare una meta classe che unifica i comportamenti di tutte le classi che erediteranno

class Meta(type):
    def __new__(self, class_name, bases, attrs):
        a = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val

        print('class_name: ', class_name)
        print('bases: ', bases)
        print('New Attrs: ', a)

        return type(class_name, bases, a)

class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("Hi Dog")
    
d = Dog()
d.HELLO()