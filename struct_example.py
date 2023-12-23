import struct

'''
https://www.pythonpool.com/struct-pack/

c  -> character
s  -> char[]
i  -> integer
f  -> float
?  -> boolean
q  -> long long integer
'''

packed_data = struct.pack('i 4s f ?', 10, b'Code', 2022, 0)
print(packed_data)

unpacked_data = struct.unpack('i 4s f ?', packed_data)

print(unpacked_data)

