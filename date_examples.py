# https://www.enricozini.org/blog/2007/pygnami/datetime/
# https://www.w3schools.com/python/python_datetime.asp

# pip install pytz <<<<<<<
import pytz
# pip install python-dateutil <<<<<<
from dateutil.parser import parse
import datetime
import datetime as dt
from time import time
import time

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
result_time = time.localtime(1672214933)
print("result:", result_time)
print("\nyear:", result_time.tm_year)
print("tm_hour:", result_time.tm_hour)

result_time = time.gmtime(1672214933)
print("result:", result_time)
print("\nyear:", result_time.tm_year)
print("tm_hour:", result_time.tm_hour)

time_tuple = (2022, 12, 28, 8, 44, 4, 4, 362, 0)
seconds = time.mktime(time_tuple)
print(seconds)

t = (2022, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)
print("Asctime:", result)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

t = datetime.time(1,2,3)
t1 = datetime.time(1,2,3)

print(t)
print('Ora: ' + str(t.hour))
print('Minuti: ' + str(t.minute))
print('Secondi: ' + str(t.second))

if t == t1:
	print("uguali")
else:
	print("diversi")

t = "pippo"
t1 = "pippo"

if t == t1:
	print("uguali")
else:
	print("diversi")

## differenze tra == e is

a = {1:2}
b = a
print(a is b)
print(a == b)

c = {1:2}

print(a is c) # false
print(a == c)

print(bool((1, 2) and 'python' and {1:'uno'}))

print(bool((1, 2) and '' and {1:'uno'}))

# a terminale funziona
# *sa1, b1, c1 = 'python'
#print(a1)  ['p', 'y', 't', 'h']
#print(b1) 'o'
#print(c1) 'n'

# *a, b, c = [1, 2, 3]
# print(a,b,c) ([1], 2, 3)
# *a, b, c, d = [1, 2, 3]
# print(a, b, c, d)([], 1, 2, 3)

print('yth' in 'python')
print((1, 2) in ['a', 'b', (1, 2)])

print('name' in {'age': 33, 'name': 'Beppe'}) # 'name' appartiene alle chiavi?
print( 'Beppe' in {'age': 33, 'name': 'Beppe'})# 'Beppe' appartiene alle chiavi?

for j in[('a','b'),'pyhton']:
	print(j)

ordinato = sorted([(1, 2, 3), 'pyhnn', {'quattro':4, 'cinque':5}], key=len, reverse = True)

print(ordinato)

for i in map(bin, [2, 3, 4]):
	print(i)

def product(x,y):
	return x * y

print(product(3,6))


today = datetime.date.today()
print(today)

print(datetime.date.min)

print(datetime.date.max)

d1 = datetime.date(2008, 3, 12)
print('d1:', d1)

d2 = d1.replace(year=2009)
print('d2:', d2)

# https://www.geeksforgeeks.org/comparing-dates-python/
d_time_3 = datetime.datetime(2018, 5, 3)
d_time_4 = datetime.datetime(2018, 6, 13)

print("d1 is greater than d2 : ", d_time_3 > d_time_4)
print("d1 is less than d2 : ", d_time_3 < d_time_4)
print("d1 is not equal to d2 : ", d_time_3 != d_time_3)

group_date = []

group_date.append(today)
group_date.append(d1)
group_date.append(d2)

group_date.sort()

for d in group_date:
    print(d)

print('----------------------------------')
print('         FORMATTAZIONE            ')
print('----------------------------------')

date_format = datetime.time(1, 10, 20, 13)
print(date_format)
print('hour:', date_format.hour)

print('Minutes:', date_format.minute)
print('Seconds:', date_format.second)
print('Microsecond:', date_format.microsecond)

today_f = datetime.date.today()
print(today)

print('ctime:', today_f.ctime())

print('Year:', today_f.year)
print('Month:', today_f.month)
print('Day :', today_f.day)

datetime_f = datetime.datetime(2018, 9, 15)

"""
%a: Returns the first three characters of the weekday, e.g. Wed.
%A: Returns the full name of the weekday, e.g. Wednesday.
%B: Returns the full name of the month, e.g. September.
%w: Returns the weekday as a number, from 0 to 6, with Sunday being 0.
%m: Returns the month as a number, from 01 to 12.
%p: Returns AM/PM for time.
%y: Returns the year in two-digit format, that is, without the century. For example, "18" instead of "2018".
%f: Returns microsecond from 000000 to 999999.
%Z: Returns the timezone.
%z: Returns UTC offset.
%j: Returns the number of the day in the year, from 001 to 366.
%W: Returns the week number of the year, from 00 to 53, with Monday being counted as the first day of the week.
%U: Returns the week number of the year,
"""

print(datetime_f.strftime("%b %d %Y %H:%M:%S"))

print(datetime_f.strftime("%d %m %Y %H:%M:%S"))

print(datetime_f.strftime('%b/%d/%Y'))

print('-----------------------------')
print('TIMEZONE')
print('-----------------------------')

dtime_time_zone = datetime.datetime.now(pytz.utc)

print(dtime_time_zone.tzinfo)

date_time_str = '2018-06-29 17:08:00'
date_time_obj = dt.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

dtime_time_zone = pytz.timezone('America/New_York')
timezone_date_time_obj = dtime_time_zone.localize(date_time_obj)

print(timezone_date_time_obj.tzinfo)

timezone_nw = pytz.timezone('America/New_York')
nw_datetime_obj = dt.datetime.now(timezone_nw)

timezone_london = pytz.timezone('Europe/London')
london_datetime_obj = nw_datetime_obj.astimezone(timezone_london)

print('America/New_York:', nw_datetime_obj)
print('Europe/London:', london_datetime_obj)

print('-----------------------------')
print('Convert Format String in Date')
print('-----------------------------')

datetime_format = parse('2018-06-29 22:21:41')
print(datetime_format)


date_array = [
    '2018-06-29 08:15:27.243860',
    'Jun 28 2018 7:40AM',
    'Jun 28 2018 at 7:40AM',
    'September 18, 2017, 22:19:55',
    'Sun, 05/12/1999, 12:30PM',
    'Mon, 21 March, 2015',
    '2018-03-12T10:12:45Z',
    '2018-06-29 17:08:00.586525+00:00',
    '2018-06-29 17:08:00.586525+05:00',
    'Tuesday , 6th September, 2017 at 4:30pm'
]

for date in date_array:
    print('Parsing: ' + date)
    dt = parse(date)
    print(dt.date())
    print(dt.time())
    print(dt.tzinfo)
    print('\n')




# pip install maya
'''
import maya

dt_maya_f = maya.parse('2020-04-18T17:45:25Z').datetime(to_timezone='America/New_York', naive=False)
print(dt_maya_f.date())
print(dt_maya_f.time())
print(dt_maya_f.tzinfo)

date_array_maya = [
    '2018-06-29 08:15:27.243860',
    'Jun 28 2018 7:40AM',
    'Jun 28 2018 at 7:40AM',
    'September 18, 2017, 22:19:55',
    'Sun, 05/12/1999, 12:30PM',
    'Mon, 21 March, 2015',
    '2018-03-12T10:12:45Z',
    '2018-06-29 17:08:00.586525+00:00',
    '2018-06-29 17:08:00.586525+05:00',
    'Tuesday , 6th September, 2017 at 4:30pm'
]

for date in date_array:
    print('Parsing Maya : ' + date + ' ...')
    dt = maya.parse(date).datetime()
    print(dt)
    print(dt.date())
    print(dt.time())
    print(dt.tzinfo)
'''


# https://stackabuse.com/converting-strings-to-datetime-in-python/

tx = datetime.time(4, 20, 1, 23)

print(tx)
print('Hour : ', tx.hour)
print('Minute : ', tx.minute)
print('Second : ', tx.second)
print('Microsecond : ', tx.microsecond)

print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)

# Date
today = datetime.date.today()
print(today)
print('ctime', today.ctime())
print('tuple', today.timetuple())
print('Ordinal', today.toordinal())

print('Year :', today.year)
print('Month:', today.month)
print('Day  :', today.day)

# date
from datetime import date
february_date = date(1999, 2, 3)

my_time = datetime.time(10, 9, 23) # ora, minuti, secondi
print(my_time)

my_date = datetime.date(1999, 2, 3)

if february_date is my_date:  # non viene intercettato
    print("IS")

if february_date == my_date: # viene intercettato
    print("==")

today_1 = datetime.date.today()

from datetime import date
today_2 = date.today()

if today_2 == today_1: # viene intercettato
    print("Today ==")
else:
    print(type(today_1), f"  today_1 {today_1} ")


current_minutes = datetime.datetime.now().minute

print(current_minutes)

# misurare le performance
# -----------------
#------------------

import time

def for_test(numbers):
    my_list = []
    for num in range(1, numbers +1):
        my_list.append(num)
    
    return my_list

def while_tetst(numbers):
    my_list = []
    counter = 1

    while counter <= numbers:
        my_list.append(counter)
        counter +=1

    return my_list

print('Start ....')
beginning = time.time()
for_test(1_500_000)
print('Finish')
ending = time.time()

print(ending - beginning)

print('Start ....')
beginning = time.time()
while_tetst(1_500_000)
print('finish')
ending = time.time()

print(ending - beginning)

import timeit

declaration_1 = '''
for_test(150000)
'''

setup_1 ='''
def for_test(numbers):
    my_list = []
    for num in range(1, numbers +1):
        my_list.append(num)
    
    return my_list
'''

lenght = timeit.timeit(declaration_1, setup_1, number= 10000)
print(lenght)

declaration_2 = '''
while_tetst(1_500_000)
'''

setup_2 = '''
def while_tetst(numbers):
    my_list = []
    counter = 1

    while counter <= numbers:
        my_list.append(counter)
        counter +=1

    return my_list
'''
lenght = timeit.timeit(declaration_2, setup_2, number= 10000)
print(lenght)
