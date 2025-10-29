s = 'Python'
for i in range(len(s)):
     print(i, s[i])

for i in reversed(range(len(s))):
     print(i, s[i])

list_range = list(range(5))
print(list_range)

list_range = list(range(0))   # n <= 0, no numbers
print(list_range)

#range(start, stop) 
list(range(5, 10))  #[5, 6, 7, 8, 9]
list(range(5, 7))   #[5, 6]
list(range(5, 6))   #[5]
list(range(5, 5))   #start >= stop, no numbers  []
list(range(0, 5))   #[0, 1, 2, 3, 4]
list(range(0, 0))   #[]
list(range(0, -1))  #[]

#range(start, stop, step) 
list(range(0, 10, 2))   #[0, 2, 4, 6, 8]
list(range(0, 10, 6))   #[0, 6]
list(range(200, 800, 100))  #[200, 300, 400, 500, 600, 700]
list(range(10, 5, -1))  #[10, 9, 8, 7, 6] <<<<
list(range(10, 5, -2))  #[10, 8, 6]
list(range(6, 5, -2))   #[6]

list(range(5, 5, -2))  # equal to stop is omitted  []
list(range(4, 5, -2))  # beyond the stop is omitted []


data = [i for i in range(-1, 2)]

print(data)

for i in range(1, 11): # 1 a 10
     print('I --->> ', i)

# Unsando la funzione range c'è un grosso risparmio di memoria
import sys

sequence = [i for i in range(11111)]
print(sys.getsizeof(sequence)) # 95864

range_sequence = range(11111) 
print(sys.getsizeof(range_sequence)) # 48

list_test = ['a', 'c', 'd', 'e', 'z']

for i in range(len(list_test)):
     print(i, " --> ", list_test[i])

numbers = [3, 9, 7, 5]

for i in range (len(numbers)):
     numbers[i] *= 2

print(numbers)

word = "programming"
# Stampa coppie di lettere tranne la prima e l'ultima
for i in range(1, len(word) -2):
     print(word[i:i+2])