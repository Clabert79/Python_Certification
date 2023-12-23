'''
import time
'''

a_bytes = bytes(3)
b_array = bytearray(3)
print(a_bytes)
print(b_array)
print(a_bytes == b_array) # sono uguali al confronto

try:
    a_bytes[0] = 1
except Exception as e:
    print(e)

b_array[0] = 1
print(b_array)

print('----------------------------------------------------')

import time
n = 100_000_000
start = time.time()
b = bytes(b'x' * n)
stop = time.time()
print('bytes()', stop - start)
start = time.time()
b = bytearray(b'x' * n)
stop = time.time()
print('bytearray()', stop - start)
