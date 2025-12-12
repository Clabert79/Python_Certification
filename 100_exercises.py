a = 1
_a = 2
_a2 = 3
# 2a = 4 not valid

print(a + _a + _a2)

a = "1"
b = 2
#print(a + b) error type error
print(a + str(b))

a = "1"
b = 2
print(int(a) + b)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[1])

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[3:6]) #Slice from index 3 to 6

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[:3]) #Slice from index 0 to 3
