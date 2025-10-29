from collections import Counter

list_1 = ['x','y','z','x','x','x','y', 'x','z']

print(type(Counter(list_1)))
print(Counter(list_1))

my_str = "Welcome to Guru99 Tutorials!"
print(Counter(my_str))


_count = Counter()
_count.update('Welcome to Guru99 Tutorials!')
print('%s : %d' % ('u', _count['u']))
print('\n')
for char in 'Guru':
    print('%s : %d' % (char, _count[char]))


counter1 =  Counter({'x1':13, 'x': 4, 'y': 3, 'z': -2})

counter2 = Counter({'x1': -12, 'y': 5, 'z':4 })

#Addition
counter3 = counter1 + counter2 # only the values that are positive will be returned.

print("Addition")
print(counter3)

#Subtraction
counter4 = counter1 - counter2 # all -ve numbers are excluded.For example z will be z = -2-4=-6, since it is -ve value it is not shown in the output

print("Subtraction")
print(counter4)

# https://realpython.com/python-counter/ Deep dive

from collections import Counter
text = ('to be or not to be that is the question') 
counter = Counter(text.split()) 
print(counter)
for word in sorted(counter):
    print(f'{word:<12} {counter[word]}')