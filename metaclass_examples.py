'''
• se un oggetto obj non è istanza di type, ovvero isinstance(obj, type) restituisce False,
allora obj non è una classe;

• se un oggetto obj è una istanza di type, ovvero se isinstance(obj, type) restituisce True,
allora obj è una classe;

• se un oggetto obj è una classe e risulta essere sottoclasse di type, ovvero
issubclass(obj, type) restituisce True, allora obj è una metaclasse e questo significa che le istanze di obj sono,
a loro volta, delle classi.

metodi magici

class type:
@classmethod
def __call__(cls, *args, **kwargs):
inst = cls.__new__(cls, *args, **kwargs)
if isinstance(inst, cls): inst.__init__(*args, **kwargs)
return inst

'''

# pag 647
'''

class FooMeta(type):
    def __call__(meta, name, bases, namespace):
        print('FooMeta.__call__()')

class InstanceOfFooMeta(type, metaclass=FooMeta):
   pass

class Foo(metaclass=InstanceOfFooMeta):
    pass

FooMeta.__call__()
'''

# https://realpython.com/python-metaclasses/


Foo = type('Foo', (), {})

x = Foo()

print(type(x))

Bar = type('Bar', (Foo,), dict(attr=100))

x_b = Bar()

print(x_b.attr)
print(x_b.__class__)
print(x_b.__class__.__bases__)

#-------------------------------------------------------------

Fooo = type(
        'Fooo',
        (),
        {
            'attr': 100,
            'attr_val': lambda x : x.attr
        },

)


'''
è l'equivalente di questa definizione
class Foo:
    attr = 100
    def attr_val(self):
        return self.attr

'''


x_c = Fooo()
print(x_c.attr)
print(x_c.attr_val())


def new(cls):
    x = object.__new__(cls)
    x.attr = 101 # si puo' insierire qualsiasi nome di metotodo
    return x

Foo.__new__ = new

f = Foo()
print(f.attr)

g = Foo()
print(g.attr)

#-------------------------------------------------------------
# definire un propria metaclasse
#-------------------------------------------------------------

class Meta(type):
    def __new__(cls, name, bases,dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 102
        return x

class BarMeta(metaclass=Meta):
    pass

class Qux(metaclass=Meta):
    pass

print(BarMeta.attr, Qux.attr)


class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        a = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
        print(a)

        return type(class_name, bases, a)

class Dog(metaclass=Meta):
    x = 5
    y = 6

    def hello():
        print("Hi")

d = Dog()
print(d.X) # deve essere Maiuscola