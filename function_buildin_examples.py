# https://realpython.com/python-enumerate/

# MAP

'''
Applica una funzione su tutta una lista di oggetti e crea un oggetto map iterabile
'''

names = ["Andrea", "Luigi", "Marco"]

print(map(len, names))

#trasormo in una lista
print(list(map(len, names)))

#esempio con una funzione custom
def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]

squared = map(square, numbers)

print(squared)
print(list(squared))
