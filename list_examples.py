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

