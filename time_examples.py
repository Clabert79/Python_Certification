# https://realpython.com/python-timer/
# https://pynative.com/python-get-execution-time-of-program/

# https://realpython.com/python-time-module/

from time import strftime, gmtime, ctime, time, struct_time
t = 1587253022
t_struct = gmtime(t)

print(strftime("%Y-%m-%d %H:%M:%Sz", t_struct))
print(strftime("Today is %A, %B %d, %Y", t_struct))

from time import strptime
from time import ctime
s = "04/18/2020 11:37:02 PM"

print(strptime(s, "%m/%d/%Y %I:%M:%S %p"))

print(ctime()) # timestamp depends on your geographical location.

t = time()
print(time())

print(ctime(t)) 

c_time = ctime(time())
print(type(c_time))

time_tuple = (2025, 2, 9, 7, 6, 55, 1, 57, 0)

time_obj = struct_time(time_tuple)

print(time_obj)

'''
Technical Detail: 
If you’re coming from another language, the terms struct and object might be in opposition 
to one another.
In Python, there is no data type called struct. Instead, everything is an object.
However, the name struct_time is derived from the C-based time library 
where the data type is actually a struct.
In fact, Python’s time module, which is implemented in C, 
uses this struct directly by including the header file times.h.
'''

print("Year ", time_obj.tm_year)
print("Month ", time_obj.tm_mon) 
print("Day M", time_obj.tm_mday)
print("Day Y", time_obj.tm_yday)

from time import sleep, perf_counter

start = perf_counter()
sleep(3)
end = perf_counter()

elapsed = end - start
print("elapsed", elapsed)

by_gmtime = gmtime(2_000_000)

print(type(by_gmtime), " --> " , by_gmtime)

curent = gmtime(time())
print("Current ", " --> ", curent.tm_year)    

now = time()

tommorow = now + 24 * 60 * 60
print("Tommorow ", ctime(tommorow))

tommorow - now #seconds

from calendar import timegm

now_epoch = time()

now_struct = gmtime(now_epoch)

from time import strftime

str_time = strftime("%Y-%m-%d %H:%M:%S", now_struct)
print(str_time) # 2025-03-14 15:01:42

s ="Monday, April 18, in the year 2025 CE"

fmt = "%A, %B %d, in the year %Y CE"
struct = strptime(s, fmt)

print(struct.tm_mon)

import datetime

dt = datetime.date(2025, 3, 21) #sono uguali

print(type(dt), dt)
import time

dt = datetime.date.fromtimestamp(time.time())

print(type(dt), dt) #sono uguali

dt = datetime.date.fromisoformat('2025-03-21')

print(type(dt), dt) #sono uguali

year = dt.year
month = dt.month
day = dt.day

dt = datetime.datetime.now()
print(type(dt), dt) # minuti e secondi
dt = datetime.datetime.today()
print(type(dt), dt)

from time import time, ctime
t01 = time()
print(ctime(t01))

time_tuple = (2025, 4, 29, 7, 6, 55, 1, 57, 0)
from time import struct_time
time_obj = struct_time(time_tuple)

print(type(time_obj), time_obj)

time_obj = struct_time(time_tuple)
day_of_year = time_obj.tm_yday
day_of_month = time_obj.tm_mday

print("---->", day_of_month)
print("---->", day_of_year)

dt = datetime.datetime.now()
tddelta = datetime.timedelta(days=10, hours=10, minutes=10)

add_dt = dt + tddelta

print(type(add_dt), " ", add_dt)

import pytz

dt_now_tmz_utc = datetime.datetime.now(tz=pytz.UTC)

dt_now_tmz_us = datetime.datetime.now(pytz.timezone('US/Eastern'))

print('UTC', dt_now_tmz_utc)
print("US", dt_now_tmz_us)