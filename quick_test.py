numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

print("List of ...")
for value in (x ** 2 for x in numbers if x % 2 != 0):
    print(value, end=' ')

squares_of_odds = (x ** 2 for x in numbers if x % 2 != 0)
print("Generator of ...")
for odd in (x ** 2 for x in squares_of_odds if x % 2 != 0):
    print(odd, end=' ')

from collections import Counter

text = ('to be or not to this is the question')
counter = Counter(text.split())

print(type(counter)," ---> ", counter)
for word in sorted(counter):
    print(f"{word}")