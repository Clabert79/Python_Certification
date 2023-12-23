import enum
from enum import Enum
from enum import IntEnum


Pasta = IntEnum('Pasta', ('spaghetti', 'lasagne', 'penne'))
print(Pasta.__name__)
print(Pasta.spaghetti)
print(Pasta.lasagne)

if Pasta.lasagne == Pasta.spaghetti:
    print("uguale")
else:
    print("no uguale")

print(Pasta.spaghetti + Pasta.lasagne)

#possono essere usati ovunque al posto di un intero
print(('a', 'b', 'c')[Pasta.spaghetti])



print('*************************************************')
pasta_2 = Enum('pasta_2', 'spaghetti lasagne tagliatelle')
print(pasta_2.spaghetti)
print(pasta_2.tagliatelle)
print(pasta_2.lasagne)

for member in Pasta:
    print(member.name, member.value, sep="-->")
# i membri non possono essere modificati


class Days(enum.Enum):
    Sun = 1
    Mon = 1
    Tue = 3

print ("The enum member as a string is : ",end="")
print (Days.Mon)

print ("he enum member as a repr is : ",end="")
print (repr(Days.Sun))

print ("The type of enum member is : ",end ="")
print (type(Days.Mon))

print ("The name of enum member is : ",end ="")
print (Days.Tue.name)
