# L'iterator è un oggetto con lo stato di iterazione

generator = (c * 4 for c in 'SPAM')
iterator_1 = iter(generator)

print(next(iterator_1))
print(next(iterator_1))

iterator_2 = iterator_1

print(next(iterator_2))

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

for x in mytuple:
  print(x)

for x in mystr:
  print(x)


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class Square:
    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.length:
            raise StopIteration
        
        self.current += 1
        return self.current ** 2
    

class Squares:
    def __init__(self, start, stop) -> None:
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2


# Iteratori Legacy

class iteratoreDispari(object):
    "Classe iterabile"

    def __init__(self, container):
        self.container = container
        self.n = -1

    def __next__(self):
        self.n += 2
        if self.n > self.container.maximum:
            raise StopIteration
        return self.n

    def __iter__(self):
        return self

class numeriDispari(object):
    "Classe itarabile"

    def __init__(self, maximum) -> None:
        self.maximum = maximum
    
    def __iter__(self):
        return iteratoreDispari(self)

num_dispari = numeriDispari(20)
for num in num_dispari:
    print("---> ", num)

it = iter(numeriDispari(7))
print(next(it))
print(next(it))

print(list(num_dispari))
print(set(n for n in num_dispari if n > 4))


fruits = ["apple", "orange", "grapes" ]
iter_fruits = iter(fruits)

print(iter_fruits.__next__())
print(next(iter_fruits))

class PowerOfTwo:
    def __init__(self) -> None:
        pass
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        result = 2**self.n
        self.n +=1
        return result

power_two = iter(PowerOfTwo())
print(next(power_two))
print(next(power_two))
print(next(power_two))
print(next(power_two))
print(next(power_two))

class FRange:
    def __init__(self, start, stop, step):

        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        xx = self.start
        while xx < self.stop:
            yield xx
            xx += self.step

nums = FRange(0.0, 1.0, 0.1)
for x in nums:
    print(x)


class stepper:
    def __getitem__(self, i):
        return self.data[i]

X1 = stepper()
X1.data = "Spam"    
print(X1[1])

for item in X1:
    print(item, end=',')    


print('p' in X1)
print([c for c in X1])
print(list(map(str.upper, X1)) )
print(tuple(X1), list(X1), ''.join(X1))

(a, b, c, d) = X1
print(a,c,d)