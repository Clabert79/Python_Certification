class Garage:
    def __init__(self) -> None:
        self.cars = []
    
    def __len__(self):
        return len(self.cars)

garage_ford = Garage()
garage_ford.cars.append("Fiesta")
garage_ford.cars.append("Focus")

print(len(garage_ford))


class Vehicle:

    vehicle_count = 0

    def __init__(self, body_type, make) -> None:
        self.vehicle_body = body_type
        self.vehicle_make = make
    
#classmethod
data = '''
<account>
    <owner>Guido</owner>
    <amount>1000.0</amount>
</account>
'''

class Account:
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance
    @classmethod
    def from_xml(cls, data):
        from xml.etree.ElementTree import XML
        doc = XML(data)
        return cls(doc.findtext('owner'),float(doc.findtext('amount')))


#Example use
a = Account.from_xml(data)

# Second example
import time
class Date:
    datefmt = '{year}-{month:02d}-{day:02d}'

    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return self.datefmt.format(year=self.year,
                                   month=self.month,
                                   day=self.day)
    @classmethod
    def from_timestamp(cls, ts):
        tm = time.localtime(ts)
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)
    
    @classmethod
    def today(cls):
        return cls.from_timestamp(time.time())

class MDYDate(Date):
    datefmt = '{month}/{day}/{year}'

class DMYDate(Date):
    datefmt = '{day}/{month}/{year}'

a = Date(1967, 4, 9)
print(a) 

b = MDYDate(1967, 4, 9)
print(b)

c = DMYDate(1967, 4, 9)
print(c)

a = MDYDate.today()
print(a) 


#fACTORY PATTERN
from datetime import date
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    # a class method to create a 
    # Person object by birth year

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year -year)
    
    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

    def display(self):
        print("Name : ", self.name, "Age : ", self.age)

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('james', 1996)

person1.display()
person2.display()
print(Person.isAdult(22))
import string

print('Example Class ...')

class Account:
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self._balance = balance
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected str')
        
        if not all(c in string.ascii_lowercase for c in value):
            raise ValueError('Must be uppercase ASCII')
        if len(value) > 10:
            raise ValueError('Must be 10 characters or less')
        
        self._owner = value

class Date:
    _cache = { }

    @staticmethod
    def __new__(cls, year, month, day):
        self = Date._cache.get((year,month,day))

        if not self:
            self = super().__new__(cls)
            self.year = year
            self.month = month
            self.day = day
            Date._cache[year,month,day]

        return self
    
    def __init__(self, year, month, day):
        pass

# Example
d = Date(2012, 12, 21)
e = Date(2012, 12, 21)
assert d is e              # Same object