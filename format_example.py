# https://pyformat.info/

print(f"{5+5=}") #5+5=10

nswer = 42
print(f"{{answer}}") # prints "{42}"
# print(f"{ord('\"')}") # SyntaxError

# print(f"{ord('\n')}")     # SyntaxError
newline_ord = ord('\n')
print(f"{newline_ord}")   # prints "10"

n = 12345678990

from decimal import Decimal
print(f'{Decimal("10000000000000000000000000.0"):.3f}') # 10000000000000000000000000.000
print(f'{Decimal("10000000000000000000000000.0"):.3g}') # 1e+25
print(f'{Decimal("10000000000000000000000000.0"):.3E}') # 1.000E+22
print(f'{Decimal("10000000000000000000000000.0"):.3e}') # 1.000e+22

print(f'{Decimal("10000000000000000000000000.0"):.0f}') # 10000000000000000000000000

print(f'[{27:+10d}]') # [        27]
print(f'[{27:+010d}]') # [000000000027]

print(f'[{"Amanda":>10}]\n[{"Amanda":^10}]\n[{"Amanda":<10}]') 
'''
[    Amanda]
[  Amanda  ]
[Amanda    ]
'''

print(f"The value of n is {n:, }")

print(f"The value of n is {n:,}")

n = 1234.123

print(f"The value of n is {n:,.2f}")

print(' Padding ....')
s = 'ABC'
padding = 'X'
len = 8

x = s.rjust(4, '-')
print(x)

x = s.ljust(5, '0')
print(x)

x = s.zfill(len)
print(s,' fill ',x)

x = ('{:' + padding + '>' + str(len) + '}').format(s)
print(x)


x = f'{s:{padding}>{len}}'        # x = f'{s:X>8}'

print(x)

# number
print(30.11E9)              # 30110000000.0
print(30.11 * 10 ** 9)      # 30110000000.0

print("%d %s cost $%.2f" % (6, "bananas", 1.74)) #diversi tipi di formttazione

welcome_sentence = "Hello, my name is %s." % "Graham" # in una variabile

'''
Conversion types f and F convert to a string representation of a floating-point number,
while e and E produce a string representing E (scientific) notation:
'''
print("%f, %F" % (3.14159, 3.14))
print("%e, %E" % (1000.0, 1000.0))


'''
The g and G conversion types choose between floating-point or E notation output,
depending on the magnitude of the exponent and what value you specify for the
.<precision> component:
'''
print("%g" % 3.14)
print("%g" % 0.00000003)
print("%G" % 0.00000003)
print("%c" % 97) #conversione in carattere
print("%c" % 8721)
print("Get %d%% off on %s today only!" % (30, "bananas"))

#%[<flags>][<width>][.<precision>]<type>

#[<width>]
print("%5s" % "foo") # 5 sono i  caratteri minimi aggiungerà a sinistra quelli mancanti
print("%.2f" % 123.456789) # '123.46' arrotonda alla seconda cifra
print("%.2e" % 123.456789)
print("%.2g" % 123.456789)
print("%.4s" % "foobar") #sono troncati a 4
print("%8.3s" % "foobar") # --> '     foo'
print("%.*d" % (10, 123)) # --> '0000000123' il '.' fa aggiungere gli 0

#[<flags>]
'''

#   Display of base or decimal point for integer and floating-point values
0   Padding of values that are shorter than the specified field width
-   Justification of values that are shorter than the specified field width
+   Display of leading sign for numeric values
' ' (space) Display of leading sign for numeric values

'''
print("%+5d" % 3)

print("%d %s cost $%.2f" % (6, "bananas", 1.74))

# la stessa soluzione ma con un dizionario
data = {"quantity": 6, "item": "bananas", "price": 1.74}
template = "%(quantity)d %(item)s cost $%(price).2f"
print(template % data)

data = {"quantity": 6, "item": "bananas", "price": 1.74}
ad_1 = "%(quantity)d %(item)s cost $%(price).2f"
print(ad_1 % data)

ad_2 = "You' ll pay $%(price).2f for %(item)s, if you buy %(quantity)d"
print(ad_2 % data)


print('<<<--------->>>>')

greet = "Hi"

print(greet)

print(f"{greet:_^10}")
print(f"{greet:_<10}")
print(f"{greet:_>10}")

print(f"{3.4:10}")
print(f"{3829.45:2}")

print(f"{0.34356474:%}")

print(f"{1000000:,.2f}")
print(f"{1000000:_.2f}")

rating = float(0.234)
print(f"{rating:.3f}") # .<N>f serve a far stampare N numeri dopo la virgola