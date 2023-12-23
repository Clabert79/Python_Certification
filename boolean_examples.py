# https://stackoverflow.com/questions/31354429/why-is-true-is-false-false-false-in-python#:~:text=Python%20interprets%20multiple%20(in)equalities,is%20is%20equivalent%20to%20%3D%3D%20.

x = 1, 0, -1, [0], 1 
y = 0, 1 > 0 or []

print(x)
print(y)

print(x and y)
print(1, 0, -1, [0], 1 and 0, 1 > 0 or [])

if 1:
    print('1 is True')
else:
    print('NO')

if 0 :
    print('NO')
else:
    print('0 is False')


if -1:
    print('-1 is True')
else:
    print('NO')

if 3:
    print("> 0 is True")
else:
    print("NO")

none = None
if(none):
    print("NO")
elif none is False : # in questo caso invece restiuesce False ---> if not none:
    print("'NONE' is False")
else:
    print("None is not True and is not False")

false_boolean = False
if not false_boolean:
    print("FALSEEE !!!")

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
'''
They reference the same object.
'''
x = [0]
y = [x, 1]
print(x is y[0])

'''
x has been assigned to a different object.
'''

x = [0]
print(x is y[0]) #False
print(x == y[0]) #True

#https://realpython.com/courses/python-is-identity-vs-equality/#:~:text=The%20%3D%3D%20operator%20compares%20the,you're%20comparing%20to%20None%20.

# == is for value equality
# is is for reference equality. 

a = [1, 2, 3]
b = a
c = a[:]

print(a == a) # True
print(a == c) # True

print(a is b) # True
print(a is c) # False

#https://towardsdatascience.com/whats-the-difference-between-is-and-in-python-dc26406c85ad

a = 10
print(a <= 10 and 1 < a) # True
print(a <= 10 & 1 < a) # False viene valutato così a <= (10 & 1) < a or a <= 0 < a
# fix
print((a <= 10) & (1 < a))

print('------------------------------------------------')
print('0 = ', bool(0))
print('1 = ', bool(1))
print('-1 = ', bool(-1))
print('None = ',bool(None))

print('------------------------------------------------')
print('5 == 5 not', not(5==5)) #false

'''
The negation of a conjunction is the disjunction of the negations.
The negation of a disjunction is the conjunction of the negations.
'''
p = 1
q = 1
print(not (p and q) == (not p) or (not q))
print(not (p or q) == (not p) and (not q))

i = 1
j = not not i # i è iniziamente true poi viene trasformata in false dal primo not e poi riconvertita in true dal primo not.
print(j)


a = 1
b = 0
c = a & b
print("c", c)
d = a | b
print("d", d)

e = a ^ b
print("e", e)

print("c+ d + e", c+ d + e)

