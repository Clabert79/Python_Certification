"""6.000.000 di lanci di un dado a 6 facce."""
import random
 # contatori delle frequenze

"""
https://elshad-karimov.medium.com/day-43-of-100daysofcode-in-python-the-art-of-randomness-and-simulations-b707c95a3af4

random.random(): Return the next random floating number between 0.0 and 1.0.

random.randint(a, b): Return a random integer N such that a <= N <= b

random.choice(sequence): Return a randomly selected element from a non-empty sequence.

random.shuffle(sequence): Shuffle the sequence in place.
"""

frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

for roll in range(6_000_000): # underscore come separatore
    face = random.randrange(1, 7)

# incremento del contatore appropriato
if face == 1:
    frequency1 += 1
elif face == 2:
    frequency2 += 1
elif face == 3:
    frequency3 += 1
elif face == 4:
    frequency4 += 1
elif face == 5:
    frequency5 += 1
elif face == 6:
    frequency6 += 1
print(f'Faccia{"Frequenza":>13}')
print(f'{1:>4}{frequency1:>13}')
print(f'{2:>4}{frequency2:>13}')
print(f'{3:>4}{frequency3:>13}')
print(f'{4:>4}{frequency4:>13}')
print(f'{5:>5}{frequency5:>13}')
print(f'{6:>5}{frequency6:>13}')

#https://blog.finxter.com/python-random-seed-a-deep-dive/
#inizializzo con lo stesso valore
random.seed(32)

for roll in range(10):
    print(random.randrange(1, 7), end=' // ')

for roll in range(10):
    print(random.randrange(1, 7), end=' // ') # diverso perchè continua la sequesnza

random.seed(32) # qui riparte

for roll in range(10):
    print(random.randrange(1, 7), end=' ')

x = "PNEUMONOULTRAMICROSCOPICSILICOVOLCANOCONIOSIS"
print("Output Without Setting A Seed: ")
for i in range(3):
    print(random.choice(x))

print("Output After Setting A Seed: ")
for i in range(3):
    random.seed(5)
    print(random.choice(x))

print("Randrange ...")
print(random.randrange(10))

for i in range(21):
    print(random.randrange(2, 20, 2),'-', end='')

print("")

print("Choices ...")

numbers = [n+1  for n in range(10)]
my_pick = random.choices(numbers, k=5)
print(my_pick)

numbers = [1,2,3,4]
my_pick = random.choices(numbers, weights=[1,2,3,4], k=20)

print(my_pick)