friends = ["Rolf", "Jhon", "Anna"]

for counter, friend in enumerate(friends):
    print(counter)
    print(friend)

list_friends =list(enumerate(friends))
dict_friends = dict(enumerate(friends))

print(list_friends)
print(dict_friends)

l1 = ["rosse", "verde", "giallo"]
s1 = "tramonto"

#creazione di un oggetto numerate
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("valore di ritorno ", type(obj1))

print(list(enumerate(l1)))
print(list(enumerate(s1, 0)))

list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]

for index,name in enumerate(list_names):
    print(f'{name} is found at index {index}')

indices_list = list(enumerate("Python"))

for index, item in enumerate("Python"):
    print(f" this is the index {index} an this is the {item}")


fruits = ['Apple', 'Pinapple', 'pear', 'grapes']
enumerated_fruits = enumerate(fruits)
enumerated_fruits_list = list(enumerated_fruits)

for index, val in enumerated_fruits_list:
    print(index, val)


def even_items(iterable):
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]

print(even_items(fruits))
