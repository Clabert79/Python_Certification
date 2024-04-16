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