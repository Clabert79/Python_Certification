class Life:
    def __init__(self, name='unknown'):
        print('Hello ' + name)
        self.name = name

    def live(self):
        print(self.name + ' is living !!')

    def __del__(self):
        print('Goodbye ' + self.name)

brian = Life('Brian')
brian.live()
brian = 'pippo'
print(brian)


class MyClass():
    def __new__(cls, message):
        instance = super().__new__(cls)
        return instance
    def __init__(self, message) -> None:
        self.message = message
        print(self.message)

mc = MyClass("Pluto")

class Commuter1:
    def __init__(self, val) -> None:
        self.val = val
    def __add__(self, other):
        print('add',  self.val, other)
        return self.val + other
    def __radd__(self, other):
        print('radd', self.val, other) 
        return other + self.val

print('Inint ...')
y = Commuter1(99)
x = Commuter1(88)
print('------>')

w = x + 1
z = 1 + y

u = y + x
u_1 = Commuter1(99) + Commuter1(88)
 

print('w', w)
print('z', z)
print('u', u)
print('u_1', u_1)

print('**********************************')

class Number:
    def __init__(self, val) -> None:
        self.val = val
    def __iadd__(self, other):
        print('iadd', self.val, other)
        self.val += other
        return self


n = Number(5)
n += 1
n += 1
print(n.val)

m = Number([1])
m += [2]

print(m.val)