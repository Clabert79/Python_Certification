# Serializzazione (Ppickling)

import pickle

name_file = "my_dict.pkl"
my_dict = {"name": "Mario", "age": 35}

# Salvataggio dei dati
with open(name_file,'wb') as file:
    pickle.dump(my_dict, file)

#De-serializzazione (Unpickling)

with open(name_file,'rb') as file:
    my_dict_load = pickle.load(file)

print('Type: ', type(my_dict_load), 'Value: ', my_dict_load)

import os
if os.path.exists(name_file):
    print(f"this file {name_file} exist. Now remove ...")
    os.remove(name_file)
else:
    print(f"this file {name_file} does not exist")

import shelve

shelf = shelve.open('proof')
shelf['name'] = 'Pippo' 
shelf['age'] = 30 
shelf.close()

shelf = shelve.open('proof') 

print(shelf['name'])

shelf.close()