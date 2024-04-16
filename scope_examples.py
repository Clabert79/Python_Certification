# https://realpython.com/python-namespaces-scope/
# LEGB rule (local, enclosing, global, and built-in scopes)
'''
When you use an unqualified name insidea function,
Python searchesuptofour scopes—the local (L) scope, then the local scopes of any enclosing (E) defs and lambdas, then the global (G) scope, and then the built-in (B) scope—and stops at the first place the name is found.
If the name is not found during this search, Python reports an error.
'''

print("--------------------------------------------------------------------------------")


def show_truth_string():
    my_var_str = "Surprise STR Inside"
    my_list_var.append("Inside func")
    print("Inside Func", my_var_str)
    print(my_list_var)

my_var_str = "Surprise STR Outside"
my_list_var = ["Outside func 1"]
print(my_list_var)
show_truth_string() #Stampa la variabile interna
print("Outside STR Func", my_var_str) # Stampa Esterna
my_list_var.append("Outside func 2")
print(my_list_var) # viene modifica la list all'interno della funzione 

print("--------------------------------------------------------------------------------")
x = 88
def func_no_mutable():
    # global x
    # x = y + 1
    return x

x = func_no_mutable()
print(x)

x_map = {'a':1, 'b':2}

def func_mutable():
    global x_map
    x_map = {'c':3, 'd':4}

    # global x_map
    print(x_map)


func_mutable()
print(x_map)

print('----------------------------------------------------')
print('Local ....')

# https://www.programiz.com/python-programming/global-local-nonlocal-variables
def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print("inner: ", x)

    inner()
    print('outer:', x)

outer()


def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1

    return nested

f_1 = tester(0)
f_1('Spam')
f_1('Ham')
f_1('Eggs')

def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1

    nested.state = start
    return nested

f_2 = tester(0)
f_2('spam')
f_2('ham')
print(f_2.state)


state = [1,2,4,5]

def tester(start):
    state = [1,2,4,5]
    def nested(label):
        print(label, state[0])

    state[0] += 1
    state = [start]
    return nested

tester(5)


X1 = 'Spam1'
def func():
    X1 = 'NI!'
    print(X1)

func()
print(X1)

def f(a, b, c):
    a = 1 # a is a single scalar value, so no pointing involved
    c = b # point the local"c"pointer to point to"b"
    c[0] = 2 # change the 2nd value in the list pointed to by"c"to 2


a=10
b=[11, 12, 13]
c=[13, 14, 15]

print( 'a', a)
print( 'b', b)
print( 'c', c)

f(a, b, c)

print( 'a', a)
print( 'b', b)
print( 'c', c)

print('Finish Local ....')


print('----------------------------------------------------')

# ----------------------------------
#           ASSIGN
#-----------------------------------

string = 'Spam'
a, b, c = string[0], string[1], string[2:]
print( a, b, c)

a, b, c = list(string[:2]) + [string[2:]]
print( a, b, c)
a, b = string[:2]
c = string[2:]
print( a, b, c)

(a, b), c = string[:2], string[2:]
print( a, b, c)

(a, c )= string[:2], string[2:]

print( a, c)

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
    print( a, b, c)

for ((a, b), c) in [((7, 8), 9), ((10, 11), 12)]:
    print( a, b, c)

red, green, blue = range(3)
print(green, blue)

L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)

# only pyhton 3.n
seq = [5, 6, 7, 8]
# a, *b = seq
# print(a, b)

while seq:
    f_seq, *seq = seq
    print(f_seq, seq)

a, *b = 'spam'
print(a, b)

a, *b, c = 'spam'
print(a, b, c)

a, *b, c = range(10)
print(a, b, c)

# con l'*' la procedura prende tutti i numeri che sono all'interno
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

# ripete lo stesso comportamento in python 2.
for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    a, b, c = all[0], all[1:3], all[3]
    print(a, b, c)

a = b = 0
b = b + 1
print(a, b) # 'a' è immutabile e rimane a 0

a = b = []
b.append(42)
print(a, b) # la lista non immutabile e prendono entrambe il valore di 42

Y = 20
X = 5
X = X + Y
print(X, Y)
X += Y #  equivalente a quello precedente
print(X, Y)
X *= Y
print(X, Y)
X %= Y
print(X, Y)
X &= Y
print(X, Y)
X ^= Y
print(X, Y)
X <<= Y
print(X, Y)
X -= Y
print(X, Y)
X /= Y
print(X, Y)
X **= Y
print(X, Y)
# X |= Y
# X >>= Y
# X // = Y

print(X, Y)
# ----------------------------------
#           SCOPE
#-----------------------------------

x_a = "global"

def foo_x():
   # x_a = x_a + " pippo" se faccio qualcosa si accorge che la variabile è fuori scope se ometto questa riga legge quella fuori
    print("X insiede ", x_a)

foo_x()
print("X outside ", x_a)

# Create a Local Variable
def foo_y():
    y = "local"
    print(y)

foo_y()

# Using Global and Local variables in the same code
x_b = "Global"

def foo_x_a():
    global x_b
    y_a = "Local"
    x_b = x_b * 2 # riesce a leggerla
    print(x_b)
    print(y_a)

foo_x_a()


x_c = 5

def foo_x_b():
    x_c = 10
    print("local x: ", x_c)


foo_x_b()

print("X Global ", x_c)

print("No Local")

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "Non local"

    inner()
    print("outer: ", x)

outer()

print('-'*40)

a_1 = 1

def nester():
    print(a_1)
    class C:
        print(a_1)
        def method1(self):
            print('method1 ...')
            print(a_1)

        def method2(self):
            print('method2 ...')
            a_1 = 3
            print(a_1)

    I = C()
    I.method1()
    I.method2()

print(a_1)
nester()
print('-'*40)


total = 1

def add_to_total(n):
    global total # mantiene il valore estrno
    total = total + n

add_to_total(5)

print("Total " , total)

def show_truth():
    mysterious_var.append('New surprise') #lista e cerca nelle variabili globali
    print(mysterious_var)

mysterious_var = ['Surprise ??"']

show_truth()
print(mysterious_var)


X_f = 99

def f1():
    X_f = 88

    def f2():
        print(X_f)
    return f2

f1() # non la chiama

action = f1()
action() # viene chiamata

print("---------------------------------------")

'''
The output here is 'Spam',
because the function references a global variable
in the enclosing module (because it is not assigned in the function,
it is considered global).
'''
X_1 = 'Spam--1'
def func_1():
    print(X_1)
func_1()

print("---------------------------------------")
'''
The output here is 'Spam' again
because assigning the variable inside the function makes it a local
and effectively hides the global of the same name.
The print state- ment finds the variable unchanged in the global (module) scope.
'''

X_2 = 'Spam2'
def func_2():
    X_2 = 'NI!'

func_2()
print(X_2)
print("---------------------------------------")

X_3 = 'Spam3'
def func_3():
    X_3 = 'NI!'
    print(X_3) # Print local vaeiable

func_3()
print(X_3)

print("---------------------------------------")
'''
This time it just prints 'NI' because the global declaration
forces the variable as- signed inside
the function to refer to the variable in the enclosing global scope.
'''

X_4 = 'Spam4'
def func_4():
    global X_4
    X_4 = 'NI!'

func_4()
print(X_4 )
print("---------------------------------------")
'''
The output in this case is again 'NI' on one line and 'Spam' on another,
because the print statement in the nested function finds the name in the enclosing func- tion’s local scope,
and the print at the end finds the variable in the global scope.
'''

X_5 = 'Spam5'
def func_5():
    X_5 = 'NI'
    def nested():
        print(X_5)

    nested()

func_5()
print(X_5)

print("---------------------------------------")

'''
This example prints 'Spam', because the nonlocal statement
(available in Python 3.X but not 2.X)
means that the assignment to X inside
the nested function changes X in the enclosing function’s local scope.
Without this statement, this assignment would classify X as local to the nested function,
making it a different variable; the code would then print 'NI' instead.
'''

X_6 = 'Global'
def func_6():
    X_6 = 'NI'
    def nested():
        nonlocal X_6
        X_6 = 'Spam6'

    nested()
    print(X_6)

func_6()
print(X_6) # Non viene modificato


# ---------------------------------------------

def my_function_scope_1():
    var = 2
    print("Do I know that variable?", var)

var = 1,
my_function_scope_1()
print(var)


my_list_3 = [1, 2, 3, 7]
my_list_1 = [0, 1, 2, 3, 4]

def my_function_scope_2(my_list_1):
    print("Print List ##1:", my_list_1)
    print("Print List #2: >>>>> ", my_list_3) # si va a prendere la lista fuori dalla funzione (molto pericoloso)
    del my_list_1[0]  # canella l'elemento in tutte le liste
    my_list_3.append(17) # affiunge l'elemeto in tutte le liste

    print("Print #3:", my_list_1)
    print("Print #4: >>>>>>", my_list_3)

my_function_scope_2(my_list_1)

print("Print #5: >>>>>>>>>>>", my_list_3)


def outer():
    
    def inner():
        print(message)
    
    message = 'hello'
    inner()
    message = 'world'
    inner()

    return inner

print('-->> Before outer')
outer()
print('---->> After outer')
inner_returned = outer()
print('------->>')
inner_returned()
message = "fuck"
inner_returned()

print(outer.__code__.co_cellvars)
print(inner_returned.__closure__[0].cell_contents)


age_1 = 27

def increase_age():
    age_1 = 30

increase_age()

print("Age 1: ", age_1) # 27 non viene modificato l'intero

def func_test_scope(x):
    if x > 0:
        y = 42 # se è positivo viene valorizzato e visto fuori dalla condizione

    return x + y

print(func_test_scope(10))


def countdown(start):
    n = start

    def dispay():
        print('Y-minus --> ', n) # all'interno della stessa funzione anche se annidata si vedono

    while n > 0:
        dispay()
        n -= 1

countdown(20)


# “names is determined once at function definition !!!!”
# così NON FUNZIONA

def countdown_local(start):
    n = start
    def display():
        print('T-minus', n)


    def decrement():
        # n -= 1  # Fails: UnboundLocalError  <<<<<
        # così Finziona
        nonlocal n
        n -= 1        # Modifies the outer n

    while n > 0:
        display()
        decrement()

countdown_local(30)

pipp = ["2","3","4"]
pluto = "pluto"
def modify_global():
    # se non viene dichiarato internamente prende quella globale se è una variabile "immutabile"
    print("STR inside the function " + pluto) 
    
    # print("before inside ---> ", pipp) una referenza all'oggetto non riesce a trovarla e si rompe
    
    pipp = [1,2,3]
    print("after ", pipp)


modify_global()

print(pipp)

def append_global(pipp):
    pipp.append("z") #aggiunge a quella globale
    print("inside append ", pipp)

append_global(pipp)

print("-----> ", pipp)

# -----------------
num = 7

print(f'ID {id(num)} Num 1 --->', num)

def cube(num):
    print(f'ID {id(num)} Num Inside func --->', num)
    num = num ** num
    return num

cube(num)
print(f'ID {id(num)} Num 2 --->', num)