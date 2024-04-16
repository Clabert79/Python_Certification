'''
https://www.delftstack.com/it/howto/python/xor-in-python/
https://realpython.com/python-bitwise-operators/
https://wiki.python.org/moin/BitwiseOperators

https://www.youtube.com/watch?v=i1wQOiljBvY&t=586s molto completo

'&' (ampersand) - bitwise conjunction;
'|'   (bar) - bitwise disjunction;
'~' (tilde) - bitwise negation;
'^' (caret) - bitwise exclusive or (xor).
'''

n1 = 23477
n2 = 31213

print(bin(n1)[2:])
print(bin(n2)[2:])

# AND
n3 = n1 & n2
print("---- AND -----")
print(bin(n3)[2:])

# OR
n4 = n1 | n2
print("---- OR -----")
print(bin(n4)[2:])

# XOR  1 XOR 0 = 1  // 0 XOR 1 = 1  se sono diversi è 1 <<

print("---- XOR -----")

print(bin(n1)[2:])
print(bin(n2)[2:])

n6 = n1 ^ n2
print(bin(n6)[2:])

a = bool(0) # False
b = bool(1) # True

print('a = ', a)
print('b = ', b)

print(a^b)

print("---- FLAGS -----")

# Read, Write, Execute, Change Policy
person1 = 0b1110
person2 = 0b1110
person3 = 0b1010

together1 = person1 & person2 & person3
print("---- AND -----")
print(bin(together1))

print("---- NEGATIVE -----")
print(bin(~n1))

n3 = 1
print(bin(n3))

bn1 = bin(~n3) # con questa trasformazione modifica l'intero finale da 1 a -2
nt = int(bn1, 2)
print(nt)

bn1 = bin(-n3) # con questa funziona corretamenet
nt = int(bn1, 2)
print(nt)

b1 = bin(~0b0110) # modifca il in negativo
print(b1) # -0b111
print(-0b111)

'''
n3 = int('-2')
print(n3)
'''
print("---- SHIFT -----")

number = 20 
print(bin(number))
number <<= 1
print(bin(number))
print(number)

number = 1
print(bin(number))
number <<= 1 # in pratica moltiplica per 2
print(bin(number))
print(number)

#---------------------------------------------------------------
a_byte = b'\xff'  # 255
# You can print it out directly like this
print(a_byte)

# You can only `ord()` a single byte
i = ord(a_byte)   # Get the integer value of the byte

print('Type: ',type(bin(i)), 'Binay: ' , bin(i)  )

bin = "{0:b}".format(i) # binary: 11111111
hex = "{0:x}".format(i) # hexadecimal: ff
dec = "{0:d}".format(i) # decimal: 255
oct = "{0:o}".format(i) # octal: 377

print(bin)
print(hex)
print(dec)
print(oct)

# https://www.rapidtables.com/convert/number/decimal-to-binary.html on line

b1 = 5 # -->>               0000000000000101
print(b1 << 1) # 10 -->>    0000000000001010
print(b1 << 2) # 20 -->>    0000000000010100
print(b1 >> 1) # 2 -->>     0000000000000010
print(b1 >> 2) # 1 -->>     0000000000000001

#bitwise complement  operator
# https://www.youtube.com/watch?v=__-OEo6CHQ8
print(~10) #11 --->         
           #                0000 1010 (10)
           #                1111 0101 after applying bitwise complement  
           #                       +1 add 1 to the complement  
           #                1111 0101 (-11)
           #                This is the same as -x - 1.
print(f'{0:08b}')
print(f'{~0:08b}')
print('----------')
print(f'{9:08b}')
print(f'{~9:08b}')
print(f'{~9}')
print('----------')
print(f'{10:08b}')
print(f'{~10:08b}')
print(f'{~10}')
print('----------')
print(f'{11:08b}')
print(f'{~11:08b}')
print(f'{~11}')


def print_bit(x):
    print(f'{x:08b}')
    return f'{x:08b}'

print('255 --> ', print_bit(255))
print('1 --> ', print_bit(1))

print('255 & 1 --> ', print_bit(255 & 1))
print('255 or 1 --> ', print_bit(255 or 1))

def is_third_bit_set(x):
    return (x & 4) == 4

print('-----------------------------')
print_bit(99)
print(is_third_bit_set(99))
print_bit(7)
print(is_third_bit_set(7))

from array import array
signed = array("b", [42, -42])
unsigned = array("B")

unsigned.frombytes(signed.tobytes())

print(unsigned)

print(39 << 3) # moltiplica il numero n volte <---------------------
 
var = 1 
while var < 10:
	print("#")
	var = var << 1 #(x 2)
	print(var)


print(312 >> 3) # divide il numero n volte

17 >> 1 #  --> 17 // 2
17 << 2 #  --> 17 * 4

print("----------------------------------------------------------------")
print("Operazioni sui Bit")
print("----------------------------------------------------------------")
i = 15
j = 22

print("i")
print_bit(i)

print("j")
print_bit(j)

print("AND")
log = i and j
print_bit(log)
print(log)

print("NOT 'i'")
logneg = not i
print_bit(logneg)
print(logneg)

print("~ 'i'")
bitneg = ~i
print_bit(bitneg)
print(bitneg) # -16 numero negativo -1

print("TEST CON '&' ")

i = 1
j = 2

print(i, " AND ", j)
log = i and j
print_bit(i)
print_bit(j)
print_bit(log)
print(log)

i = 2
j = 3

print(i, " AND ", j)
log = i and j
print_bit(i)
print_bit(j)
print_bit(log)
print(log)

i = 3
j = 4

print(i, " AND ", j)
log = i and j
print_bit(i)
print_bit(j)
print_bit(log)
print(log)

i = 3
j = 2

print(i, " AND ", j)
print_bit(i)
print_bit(j)
log = i & j
print_bit(log)
print(log)


i = 8
j = 8

print(i, " AND ", j)
print_bit(i)
print_bit(j)
log = i & j
print_bit(log)
print(log)

flag_register = 0x1234
print("flag register -->")
print_bit(flag_register)
the_mask = 8
print("mask --> ")
print_bit(the_mask)

# flag_register = flag_register | the_mask
print("| --> ")
flag_register |= the_mask
print_bit(flag_register)

flag_register = 0x1234

flag_register ^= the_mask
print("^= --> ")
print_bit(flag_register)
'''
hifting a value one bit to the left thus corresponds to multiplying it by two;
respectively, shifting one bit to the right is like dividing by two
'''

print(18 >> 1) # --> 9
#The right-shift operator used with the number one (>> 1) on an integer divides the integer's value by two.
print(18 << 1) # --> 36 (x2)
print(18 << 2) # --> 72 (x4)

bit1 = 64 >> 1 # --> 64 // 2 (2 to the power of 1)
print(bit1)

bit1 = 64 >> 2 # --> 64 // 4
print(bit1)

bit1 = 64 >> 4 # --> 64 // 16
print(bit1)

print("--------------------------")

bit2 = 3 << 2 # 3 * 4
print(bit2)

bit2 = 3 << 3 # 3 * 8
print(bit2)

var = 1
while var < 10:
    print("#")
    var = var << 1
    print("Var ", var)

'''
and → if both operands are true, the condition is true, e.g., (True and True) is True,
or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
not → returns false if the result is true, and returns true if the result is false, e.g., not True is False.

x = 15, which is 0000 1111 in binary,
y = 16, which is 0001 0000 in binary.

& does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary
| does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary
˜ does a bitwise not, e.g.,  ˜x = 240*, which is 1111 0000 in binary,
^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
>> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary
<< does a bitwise left shift, e.g., y << 3 = , which is 1000 0000 in binary,
'''

x = 0
y = 1
x = x ^ y
print("x = x ^ y ->", x)
y = x ^ y
print("y = x ^ y ->", y)
y = x ^ y
print("y = x ^ y ->", y)
print(x, y)