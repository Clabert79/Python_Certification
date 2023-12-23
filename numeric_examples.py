import math
import sys
from decimal import Decimal

# https://realpython.com/python-numbers/
'''
1234, −24, 0, 99999999999999                Integers (unlimited size)
1.23, 1., 3.14e-10, 4E210, 4.0e+210         Floating-point numbers
0o177, 0x9ff, 0b101010                      Octal, hex, and binary literals in 3.X
0177, 0o177, 0x9ff, 0b101010                Octal, octal, hex, and binary literals in 2.X
3+4j, 3.0+4.0j, 3J                          Complex number literals
set('spam'), {1, 2, 3, 4}                   Sets: 2.X and 3.X construction forms
Decimal('1.0'), Fraction(1, 3)              Decimal and fraction extension types
bool(X), True, False                        Boolean type and constants
'''


milion_a = 1000000
milion_b = 1_000_000
milion_c = 1e6
'''
You could replace the E by * 10 **
Note: E notation is short for exponential notation. 
You may have seen this notation used by calculators 
to represent numbers that are too big to fit on the screen.
'''
num = 200000000000000000.0 # --> 2e+17
num = 1e-4 # ---> 0.0001  -4, which is 1/10000
num = 2e400 # --> inf
type(num) # --> 'float'
print('<<---->>', 30.11E9 + 1) # -- print(30.11 * 10 ** 9)  # 30_110_000_001.0


n1 = 9
n2 = 2

r1 = n1 / n2
print('r1', r1, type(r1)) #float

r2 = n1 // n2
print('r2', r2, type(r2)) #int

r3 = n1 % n2
print('r3', r3,type(r2)) #int

def isAlmostEqual(a, b, delta = 1e5):
    return abs((a-b)/b) < delta # b diverso da 0


print(2**2**3) # si deve interpretare da destra a sinistra

print('-------- Floor ----------')
print(math.floor(-11.6))
print(math.floor(11.6))

print('-------- Int ------------')
print(int(-11.6))
print(int(11.6))

print('-------- round ----------')
print(round(-11.6, 3))
print(round(11.6, 3))

print('-------- implicit --------')

print(44 * 2.0/1.1 + 5)

print('-------- float ----------')
print(0.1 * 3)
print(0.1 * 3 == 0.3)
print(10.1 + 10.2 == 20.3)

a = 2.0e200 #2.0 * 10 ** 200
b = 2.0e900 #2.0 * 10 ** 900

print(b - b == 0)
print(a - a == 0)
print(a * b == b)
print(a * b - b == a * b - b)

# r = mbq**q
# es r = 0.34475 · 10**3 ---> r = 34.475 · 10**1
# i computer sono in base 2

# max number float
f = sum(2 ** (-i) for i in range(1, 53))

print((1 + f) * 2 ** 1023)
print(sys.float_info.max)

print(1 * 2 ** (-1022))
print(sys.float_info.min)

min_den =1/2**52 * sys.float_info.min
print(min_den)

#non esiste alcun numero macchina m tale che 0 < m < 1/2**52 * sys.float_info.min.
print(min_den / 2)

m = sys.float_info.max
a = a = 1.0 * 2 ** 100

print(m)
print( m + a)

print(0.1 * 3 == 0.3)
print(0.1 + 0.2 == 0.3)

print(Decimal('0.1') * Decimal('3') == Decimal('0.3'))
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))

c = 0.1 + 0.2
d = 0.3

print(c == d)
print(isAlmostEqual(c, d))

#caso reale
# minimo numero per il delta

print(isAlmostEqual(c, d, sys.float_info.epsilon))
print(isAlmostEqual(c, d, sys.float_info.epsilon /2))


test_b = 1==2

print(1==2 < 1)

from fractions import Fraction

x1 = Fraction(1, 3)
x2 = Fraction(1, 3)

print(x1 + x2)

print(Fraction('.25'))
print(Fraction('1.25'))
print(Fraction('.25') + Fraction('1.25'))

spams = 1
spams += 42
print(spams)


# floor arrontonda verso il più grande
print("math.floor(-23.11): ", math.floor(-23.11))
print("math.floor(300.16): ", math.floor(300.16))
print("math.floor(300.73): ", math.floor(300.73))


#arrontonda la più piccolo
print("math.ceil(-23.11) : ", math.ceil(-23.11))
print("math.ceil(300.16) : ", math.ceil(300.16))
print("math.ceil(300.72) : ", math.ceil(300.72))

int_a = 2
int_b = 9

float_a = 10.9
float_b = 100.89

res = int_a + int_b

print(type(res))

res = float_a + float_b

print(type(res))

res = float_a + float_b + int_a + int_b

print(type(res))

res = int_a + int_b

print(type(res))


#Fundamental Data Type
print(type(6))
print(type(2 - 4))
print(type(2 * 4))
print(type(2.00 / 5.00))
print(2.00 ** 5.00)

print((20 - 3) + 2 ** 2)

# ()
# **
# ] /
# + -

# Espressioni condizionali

x = 100

# verbose
if x > 0:
	y = math.log(x)
else:
	y = float('nan')

print(y)

#contratta

y = math.log(x) if x > 0 else float('nan')

print(y)


num_2 = 9

#1 metodo
print(num_2**(1/2))
print(num_2**(0.5))

print(pow(num_2, 1/2))
print(math.sqrt(9))
# alla terza
print(2 ** 3)

x =  5
x = float(x)
# write your code here
y = 3 * (x ** 3) - 2 * (x ** 2) + 3*x -1
print("y =", y)

x = float(input("Enter value for x: "))

# Write your code here.
y = 1 / (x + 1/(x + 1/(x + 1/x)))
print("y =", y)

income = float(input("Enter the annual income: "))

tax = 0.0
if income < 85_528:
    tax = tax if ((income * 0.18) - 556.02) < 0 else ((income * 0.18) - 556.02)
else:
    tax = 14_839.02
    if(income > 85_528):
        surplus = income - 85_528
        tax_surplus = surplus * 0.32
        tax = tax + tax_surplus

tax = round(tax, 0)
print("The tax is:", tax, "thalers")


x = 1
y = 1.0 

if x == y:
    print("Sono ==")

class Stack:
    def __init__(self):          # Initialize the stack
        self._items = [ ]

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __repr__(self):
        return f'<{type(self).__name__} at 0x{id(self):x}, size={len(self)}>'


class NumericStack(Stack):
    def push(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError('Expected Float')
        super().push(item)


#confronto per la tipologia di numeric da utilizare con le monete
from decimal import Decimal
sell_price = Decimal('1.01')
buy_price = Decimal('0.99')
items_sold = Decimal('1e18')
profit = (sell_price - buy_price) * items_sold
print(profit)
