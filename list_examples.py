
m = [[1,2,3], [4,5,6], [7,8,9]]
col2 = [row[1] for row in m]
print(col2)

sum_col2 = [row[1] + 1 for row in m]
print(sum_col2)

diag = [m[i][i] for i in [0,1,2]]
double = [c * 2 for c in 'spam']
print(double)

numbers = [2, 3, 5, 7, 11, 13, 17, 19]
numbers[::2] = [100, 100, 100, 100]
print("ID 1 --> ", id(numbers))
print(numbers)
numbers[:] = [] #cancella gli elementi
print("ID 2 --> ", id(numbers))

numbers = []
print("ID 3 --> ", id(numbers)) # cambia l'oggetto a cui è referenziato

numbers = list(range(0, 10))
del numbers[-1]
del numbers[0:2] #cancella una porzione
del numbers[::2] # cancellazione alternata
del numbers[:] # tutti

print(numbers)

del numbers # cancella la variabile
try:
    print(numbers)
except NameError:
    print("NameError occurred. Some variable isn't defined.")

numbers = [2, 3, 5, 7, 11, 13, 17, 19]
numbers *= 2 #dupplica gli lementi di una lista
print(numbers)
numbers = [3, 7, 1, 4, 2, 8, 5, 6, 3, 7, 1, 4, 2, 8, 5, 6]

num_indiex = numbers.index(5, 7) # cerca il valore "5" a partire da dall'indice 7

print(num_indiex)
num_index_end = numbers.index(5, 7, len(numbers)) # l'ultimo paramtro è la fine della ricerca
print(num_index_end)

print(numbers.index(7, 0, 4)) #valore "7" da 0 a 4

is_found = 10 not in numbers
print(type(is_found), is_found)

is_found = 7  in numbers
print(type(is_found), is_found)

color_names = ['arancione', 'giallo', 'verde']
color_names.insert(0, "rosso")

#aggiungono elemnti alla fine della lista
color_names.append('blu')
color_names.extend(['indaco', 'viola'])
color_names.extend((4, 5, 6)) # notate le parentesi aggiuntive
print(color_names)

copied_list = color_names.copy() # copia superficiale
copied_list = color_names[:] # sono equivalenti delle copie senza riferimento in mempria


#Rimuovere
color_names.remove('verde')

try:
    color_names.remove("azzuro")
except ValueError as er:
    print("Error Details: ", er)

color_names.clear()
color_names[:] = []

print("Copia Dopo le varie rimozioni ", copied_list) # la copia non viene toccata

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3,1, 4, 3, 3, 3, 2, 3, 3, 2, 2]
for i in range(1, 6):
    print(f'{i} compare {responses.count(i)} volte in responses') # conta le occorenze

color_names = ['rosso', 'arancione', 'giallo', 'verde', 'blu']

print("Before -->> ", id(color_names))
color_names.reverse()
print("After -->> ", id(color_names)) #non viene modificato il puntamento 

nums = [1, 2, 3]
vals = nums
print("Vals", vals)
print("Nums", nums)

del vals[:] # cancella tutte e 2 perchè stesso riferimento

print("Vals", vals)
print("Nums", nums)

# Confronta qual'è il numero più grande per il confronto
# Se sono uguali conftonta la lunghezza il più lungo è il maggiore

c = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 6]

if c > b:
    print('C ', c, " >> " , 'B ', b)
else:
    print('C ', c, " << " , 'B ', b)

characters = []
characters += 'Birthday'

print(characters) # crea una lista di caratteri

print("-------------------------------------------------------")
print("SLICE")
print("-------------------------------------------------------")

numbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(numbers)

numbers_a = numbers[2:6]
print("numbers[2:6] --> ", numbers_a)

numbers_b = numbers[:6]
print("numbers[:6] --> ", numbers_b)

numbers_c = numbers[6:]
print("numbers[6:] --> ", numbers_c)

numbers_d = numbers[6:len(numbers)]
print("numbers[6:len(numbers)] --> ", numbers_d)

numbers_e = numbers[:] # si copia la squenza intera

numbers_f = numbers[::2] # passo 2
print("numbers[::2] --> ", numbers_f)

# Inverte l'ordine della lista
numbers_g_1 = numbers[::-1]
# equivalente

numbers_g_2 = numbers[-1:-9:-1]

print(numbers_g_1, " --- ", numbers_g_2)

# https://towardsdatascience.com/whats-the-difference-between-is-and-in-python-dc26406c85ad
# reference equality
if(numbers_g_2 is numbers_g_1):
    print("numbers_g_2 is numbers_g_1")

# value equality
if(numbers_g_2 == numbers_g_1):
    print("numbers_g_2 == numbers_g_1")

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
 
ascending_numbers = sorted(numbers) # la funzione sorted crea una nuova lista

print("Before Sort() ", numbers)
numbers.sort();
print("After Sort() ", numbers)

numbers *= 2 # Raddoppia la list

print("After numbers *= 2 ", numbers)

pos = numbers.index(5, 7) # cerca il '5' a partire dalla posizione 7

print(" numbers.index(5, 7) ", pos)

letters = ['a','b','c','d','e']

print("letters.index('c') ", letters.index('c'))

#.............................................................................
# Shuffle List Deep Dive (https://www.geeksforgeeks.org/python-ways-to-shuffle-a-list/)

import random

shuffle_numbers  = sorted(ascending_numbers, key=lambda x :random.random()) 

#.............................................................................

response = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2] 

for i in range(1, 6):
    print(f'{i} compare {response.count(i)} occurent in resposnses')

# invertire l'ordine
color_names =  ['rosso', 'arancione', 'giallo', 'verde', 'blu']
color_names.reverse()
print(color_names)

#copiare
copied_list = color_names.copy()

list_01 = [item ** 3 for item in range(0,6)]
print(list_01)

list_02 = ["aaaaaa","bbbbbbb", "cccccccc", "dddddddd", "eeeeeeee", "ffffffff"]

# [start:stop:step] 
# --> Start: da che indice parte
# --> Stop: fino a che indice 
# --> Step: passo

print(list_02[1:4]) # ['bbbbbbb', 'cccccccc', 'dddddddd']
print(list_02[0::2]) #['aaaaaa', 'cccccccc', 'eeeeeeee']
print(list_02[1:4:2]) # ['bbbbbbb', 'dddddddd']


list_03 = ["a", "b", "c", "d" ,"3"]

print(list_03[1:3]) # "b , c" Prende il secondo elemento e il terzo

print(list_03[0:4]) # a, b, c, d parte dal primo

list_04 = [1,2,3,4,5,6,7,8,9]
print(list_04[::2]) # con il passo di 2


grades = [("Nora", 95), ("Gino", 64), ("Loretto", 86)]
for index, (student, grade) in enumerate(grades):
    print(index, student, grade)

'''
0 Nora 95
1 Gino 64
2 Loretto 86
'''

#ZIP
months = ["junuary", "February", "March", "April","May"]

first_product =[530, 545, 670, 940, 1002]
second_product = [250, 210, 295, 345, 297]
third_product = [715, 652, 850, 837, 789]

print("Zip ....")
for month, prod1, prod2, prod3 in zip(months, first_product, second_product, third_product):
    print(f"{month} {prod1} {prod2} {prod3}") 
    total = prod1 + prod2 + prod3
    print(f"Total Revenue in: {month}")
    print(total)
print("Zip ....")

print(list(zip(months, first_product, second_product, third_product)))

'''
Il numero di righe dipende da quanti elementi ci sono nelle liste(tuple)
I Parametri in base a quante liste ci sono 

[('junuary', 530, 250, 715), 
('February', 545, 210, 652), 
('March', 670, 295, 850), 
('April', 940, 345, 837), 
('May', 1002, 297, 789)]
'''