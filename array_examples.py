# https://www.mygreatlearning.com/blog/python-array/

import time
import array as arr

array0 = arr.array('i', [20, 30, 40, 50, 20])

from array import *

# arrayName = array(typecode, [ Initializers ])
array1 = array('i', [20, 30, 40, 50]) # l'array in questo caso è formato solo da integer

for x in array1:
    print(type(x), " ", x)

for i in range(1000000):
    array0.append(i)

list0 = []
for i in range(1000000):
    list0.append(i)


st_array = time.process_time()
for x in array0:
    pass

et = time.process_time()

# get execution time
res = et - st_array
print('CPU Execution time Array: ', res, 'seconds')


list_array = time.process_time()
for x in list0:
    pass

et = time.process_time()

# get execution time
res = et - list_array
print('CPU Execution time List :', res, 'seconds')


arr_str = []
arr_str.append("Spark")
arr_str.append("BY")
arr_str.append("Example")

print("specifield string:", arr_str[0])

#--------------------------------------
# LOOP ARRAY
#--------------------------------------
for str in arr_str:
    print(str)

i = 0
while i < len(arr_str):
    print(arr_str[i])
    i += 1
