# https://docs.python.org/3/library/typing.html
# https://docs.python.org/3.11/library/typing.html
# https://www.youtube.com/watch?v=QORvB-_mbZ0&t=374s <<<<<
# search: https://www.youtube.com/results?search_query=hint+types+python+deep+dive
# da vedere https://www.youtube.com/watch?v=3A0y-ksmGgI <<<
#https://mrslima.medium.com/python-typing-88923684500b


from typing import List
import sys


x: str = 1

def something(numb: float) -> int:
    return 2021 + numb

def nothing(numb: float) -> None:
    2021 + numb

l_1 : List[List[int]] = [[1, 2], 3, 4]

from typing import Dict

d_1: Dict[str, str] = {"State": "Capital"}

def foo(output: bool=False): #opzionale
    return output

from typing import Callable

def foo() -> Callable[[int, int], int]:
    func: Callable[[int, int], int] = lambda x, y: x + y
    return func

def compare(a, b):

    print("A", a)
    print("B", b)

    print("ID A: ", id(a),"ID B:", id(b))

    if a is b:
        print("a is b -> same object")

    if a == b:
        print('a == b -> same value')

    if type(a) is type(b):
        print('type(a) is type(b) -> same type')

a = [1, 2, 3]
b = [1, 2, 3]
#compare(a, b)

a = 3
b = 1
#compare(a, b)

a = 37       # Creates an object with value 37
b = a        # Increases reference count on 37
c = []
c.append(b)  # Increases reference count on 37”

#compare(a, b)
compare(b, c[0]) # se vado a prendere il valore interno ha lo stess ID
print("Ref Count: ",sys.getrefcount(b))
del a
compare(b, c[0]) #anche se 'a' è stata cancellata il riferimeto alla memoria non cambia
print("Ref Count: ",sys.getrefcount(b))

del c
print("Ref Count: ",sys.getrefcount(b))
del b
print("Ref Count: ",sys.getrefcount(37))

#https://www.csestack.org/python-getrefcount-reference-count-memory-management/ <<<<

print('------------------------------------------------------------------------------')
print('TYPY HINT')
print('------------------------------------------------------------------------------')

# https://www.infoworld.com/article/3630372/get-started-with-python-type-hints.html

name: str
age: int

name = "Your name?"
age = int("100")

# alternatively, and more simply:

name: str = "Your name?"
age: int = int("10")

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    else:
        retun n * factorial(n -1)

