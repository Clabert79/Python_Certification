#https://docs.python.org/3/howto/sorting.html
numbers = [5, 2, 3, 1, 4]
sort_numbers = sorted(numbers)
print(numbers) #in questo caso NON viene modificato l'ordine
numbers.sort()  #in questo caso viene modificato l'ordine
print(numbers)

sort_numbers_from_dict = sorted({5: 'D', 3: 'B', 1: 'B', 2: 'E', 4: 'A'}) # sorted accetta qualsiasi tipo di struttura dati ma restiuisce una lista
print(type(sort_numbers_from_dict), sort_numbers_from_dict)

split_statment = sorted("This is a test string from Andrew".split(), key=str.lower)
print(split_statment)

words = ["python", "esempio", "ordinamento", "avanzato"]
sorted_words = []
for word in words:
    sorted_charater = sorted(word)
    sorted_word = ' '.join(sorted_charater)
    sorted_words.append(sorted_word)

print(sorted_words)

data = {'z': 23, 'x': 7, 'y': 42}

for _ in sorted(data): # NON  è ordinato quindi con sorted NON viene oridnato l'originale 
    print("--> ", _) # vengono stampate le chiavi in maniera oridinata  -->  x -->  y -->  z

data_sorted = sorted(data) # Vine restituita una lista delle chiavi rodinate

for _ in sorted(data):
    print(data[_], end=' ')

test_string ="geeekforgeeks"

print("The original string :" + str(test_string))

res = ''.join(sorted(test_string, reverse=True))

print("String after reverse sorting : " + str(res))

import functools 
test_string = "geekforgeeks"

# using sorted() + reduce() + lambda

res = functools.reduce(lambda x, y: x + y,
                       sorted(test_string,
                              reverse=True))

print("String after reverse sorting : " + str(res))


# https://www.geeksforgeeks.org/python-sorted-function/
L = ["ccccccc","bb", "dddd","a"]
print("Normal sort: ", sorted(L))
print("Sort with len ", sorted(L, key=len))

def func_order(x):
    return x % 7
L = [15, 3, 11, 7]

print("Normal sort :", sorted(L)) 
print("Sorted with key:", sorted(L, key=func_order)) 

tuples = [("A", 5), ("C", 7), ("Z", 2), ("V", 4), ("T", 10)] 

def get_last_element(x):
    return x[-1]

for char, num in sorted(tuples, key=get_last_element):
    print(char, num)

