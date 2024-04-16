'''
https://realpython.com/python-sets/
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/17-Advanced%20Python%20Objects%20and%20Data%20Structures/03-Advanced%20Sets.ipynb
'''

# x = set(<iter>) 

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

print(x1.symmetric_difference(x2)) # inserice tutte le differenze 
print(x1.difference(x2)) # --->> {'foo', 'bar'}
print(x2.difference(x1)) # --->> {'qux', 'quux'}

print(x1.isdisjoint(x2)) # --->> False
x1.issubset(x2) # --->> False
print(x1 < x2)
print(x1.issuperset({'foo', 'bar'})) # -->> true

x1.update(['corge', 'garply'])
print(x1)

x_froz = frozenset(['foo', 'bar', 'baz'])
print(len(x_froz))
print("--------------------------------")
# first set
set_a1 =  {'foo', 'bar', 'baz', 'foo', 'qux'}

# second set
set_b1 =  {'foo', 'bar', 'baz', 'foo', 'qux', 'pix'}

set_diff = set_b1.difference(set_a1)

print("Diff -->", set_diff)
print("--------------------------------")
s0 = set()
print(type(s0))
s1 = set([1, 'ciao', 2, ('a','b')])
print(type(s1))
s2 = {1, 'py', ('a','b'), 3}
print(s2, "Type=", type(s2))
# set un oggetto mutabile
s0.add(4)
print(s0)
# ma gli oggetti all'interno no mutabili
# s0.add([1,2]) NO

s2.add('py') # non aggiunge duplicati
print(s2)
for item in s2:
	print(item)

print("Len: " + str(len(s2)))

#intersezione

print({'a', 'b', 'c', 'd'} & {'a', 'c', 'e'}) # 'a' ,'c'

#unione

print({'a', 'b', 'c', 'd'} | {'a', 'c', 'e'}) # 'a' ,'c', 'b', 'e', 'd'

#differenza
print({'a', 'b', 'c', 'd'} - {'a', 'c', 'e'}) # 'b' ,'d'

#differenza simmentrica
print({'a', 'b', 'c', 'd'} ^ {'a', 'c', 'e'}) # 'b' , 'e', 'd'

s3 = {1,2,3,4,5,6,6}
#convert to list
l1 = list(s3)
print(type(l1))
print(l1)

s3a = s3.copy()
print(1 in s3)
s3.clear()
print(1 in s3)
print(s3a)

my_set = {1,2,3,4,5,6}
your_set = {4,5,6,7,8,9,0}

print(my_set.difference(your_set))
my_set.discard(4)
print(my_set)
my_set.difference_update(your_set)
print(my_set)

tot_set = my_set.union(your_set)
print(tot_set)

print("-------------------------------")
print("SUBSET")
print("-------------------------------")

my_sub_set = {2,3,4}
print("my_sub_set", my_sub_set)
print("tot_set", tot_set)

print(my_sub_set.issubset(tot_set))
print(tot_set.issuperset(my_sub_set))

#Differenze con i dizionari
def ha_dupplicati_d(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False

def ha_dupplicati_s(t):
    return len(set(t)) < len(t)

X = set('spam')
Y = {'h', 'a', 'm'}

result = X & Y
print(result)

result =X | Y
print(result)

result = X - Y
print(result)

result = X ^ Y
print(result)

result = {n ** 2 for n in [1, 2, 3, 4]}
print(result)

result = list(set([1, 2, 1, 3, 1]))
print(result)

result = set('spam') - set('ham')
print(result)

result = set('spam') == set('asmp')
print(result)

print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])

L = [2, 2, 4, 3, 1, 4, 4, 7, 5, 6, 6, 6, 7]
L = list(set(L))
print(L)

engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}

print('bob' in engineers)
print(engineers & managers)
print(engineers | managers)
print(engineers - managers)
print(managers - engineers)
print(engineers > managers)
print({'bob', 'sue'} < engineers)
print((managers | engineers) > managers)
print(managers ^ engineers)
print((managers | engineers)-(managers ^ engineers))

#---------------------------------------
a = 3
b = a
a = a + 3
print('a:' + str(a))
print('b:' + str(b)) # b non cambia perchè è un oggetto immutabile


list_a = ['a','b','c']
list_b = list_a

list_a.append('D') # in questo caso è un oggetto mutabile e il comportamento è diverso

print('a:' + str(list_a))
print('b:' + str(list_b))

print(list_a == list_b) # verifca i valori
print(list_a is list_b) # verifca se sono lo stesso oggetto

list_c = ['a','b','c']
list_d = ['a','b','c']

print(list_c == list_d) # verifca i valori
print(list_c is list_d) # verifca se sono lo stesso oggetto in questo caso è false

list_d = list_c
print(list_c is list_d) # verifca se sono lo stesso oggetto in questo caso è vero

# convert List to set
a_list = [1, 2, 3, 3]
print(a_list)

converted_set = set(a_list)
print(converted_set)

print("--------------------------------")
#Cancellazione
set_del = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(set_del.pop())
print(set_del)

set_del.remove(2) # se non esiste l'elemnto restituisce un eccezione
print(set_del)

set_del.discard(8)
set_del.discard(8) # se non esiste l'elemento non restituisce errore
print(set_del)

set_del.clear()
print(set_del)

set_a = {1,3,5,7,9,11}
set_b = {2,4,6,8,10,11}

print('uninion',set_a.union(set_b))
print('intersection b',set_b.intersection(set_a))

print('difference a',set_a.difference(set_b))
print('difference b',set_b.difference(set_a))

print('difference a',set_a.symmetric_difference(set_b))
print('difference b',set_b.symmetric_difference(set_a))


names_1 = {'IBM', 'MSFT', 'AA'} 
names_2 = set(['IBM', 'MSFT', 'HPE','IBM', 'CAT'])

names_set = names_1 | names_2      # Union {'MSFT', 'CAT', 'HPE', 'AA', 'IBM'}
print(names_set)

names_set = names_1 & names_2      # Intersection {'IBM', 'MSFT'}”
print(names_set)

names_set = names_1 - names_2      # Difference { 'CAT', 'HPE' }
print(names_set)

names_set = names_2 - names_1      # Difference { 'AA' }
print(names_set)

names_set = names_1 ^ names_2      # Symmetric difference { 'CAT', 'HPE', 'AA' }”
print(names_set)

# names_set.remove('IBM') # rimuove ma genera errore se non esiste
# names_set.discard('SCOX')       # rimuove se esiste ma non genera errore se non lo trova

# l'oggetto set tiene un ordine in base a questa regola
# https://www.appsloveworld.com/coding/python3x/13/why-is-the-order-of-python-sets-not-deterministic-even-when-pythonhashseed0
set_c = {"B","a","A","z","c"}
print(set_c)

{1, 3, 5} == {3, 5, 1} # True
{1, 3, 5} != {3, 5, 1} # False

{1, 3, 5} < {3, 5, 1} # False

print({1, 3, 5} < {3, 5, 1, 0}) # Valuta la Lunghessaz in questo caso è True

'''
L’operatore <= ci dice se l’insieme alla sua sinistra è un sottoinsieme improprio di quello sulla destra, 
ovvero se tutti gli elementi dell’operando di sinistra sono anche elementi dell’operando di destra e i due insiemi possono anche essere uguali:
'''

{1, 3, 5} <= {3, 5, 1} #True
print({1, 3, 5, 4} <= {3, 5, 1, 4, 2, 5})

{1, 3, 5}.issubset({3, 5, 1}) # True
{1, 2}.issubset({3, 5, 1}) # False

{1, 3, 5}.issuperset({3, 5, 1}) #True
{1, 3, 5}.issuperset({3, 2}) # False

'''
La differenza simmetrica (o unione disgiunta) tra due insiemi è l’insieme che contiene quegli elementi di
entrambi gli insiemi che appartengono esclusivamente a uno o all’altro insieme.
'''

{1, 3, 5} ^ {2, 3, 4} # {1, 2, 4, 5}
{1, 3, 5, 7}.symmetric_difference([2, 2, 3, 3, 4, 4]) # {1, 2, 4, 5, 7}

'''
Due insiemi si dicono disgiunti quando non hanno elementi in comune.
'''
{1, 3, 5}.isdisjoint({2, 4, 6}) # True
{1, 3, 5}.isdisjoint({4, 6, 1}) # False