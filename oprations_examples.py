import numpy as np

x = 4
y = 2
z = 7
x_m = np.array([[1, 2], [3, 4]])
y_m = np.array([[5, 6], [7, 8]])

# https://www.youtube.com/watch?v=aaFmMs8esCw

print(f'{z} divided  {y} equals {z / y}')
print(f'{z} divided to the floor {y} equals {z // y}')
print(f'{z} modulo of {y} equals {z % y}')
print(f'{z} to the power of {y} equals {z ** y}')
print(f'{z} to the power of 3 equals {z ** 3}')
print(f'{z} the square root of {x} is {4 ** 0.5}')
print(f'the matrix multiplication of {x_m} @ {y_m} is {x_m @ y_m}')

print(bool(0)) #False

result = (5**2 == 25)
print(result)

num1 = 6 // 3
print(type(num1)) # int
num2 = 6 // 3.
print(type(num2))
num3 = 6. // 3
print(type(num3))
num4 = 6. // 3.
print(type(num4))

# Ternary Operators
# https://book.pythontips.com/en/latest/ternary_operators.html

# value_if_true if condition else value_if_false

is_nice = True
state = "nice" if is_nice else "not nice"
print(state)

# (if_test_is_false, if_test_is_true)[test]

nice = True
personality = ("mean", "nice")[nice]
print("The cat is ", personality)

condition = True
print(2 if condition else 1/0)

def my_function(real_name, optional_display_name=None):
    optional_display_name = optional_display_name or real_name
    print(optional_display_name)

my_function("John")

my_function("Mike", "anonymous123")
