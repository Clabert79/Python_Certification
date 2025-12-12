from pickletools import string1
from tokenize import String

# https://realpython.com/python-getter-setter/
# https://realpython.com/python-property/


print("#0-----------------\n")

'''
property([fget=None, fset=None, fdel=None, doc=None])

fget	A function object that returns the value of the managed attribute
fset	A function object that allows you to set the value of the managed attribute
fdel	A function object that defines how the managed attribute handles deletion
doc	A string representing the property’s docstring
'''

class CircleP:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius
    
    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property"
    )

    radius_lambda = property(lambda self: self._radius)

circle = CircleP(42.0)
print(circle.radius)
print(circle.radius_lambda)

circle.radius = 100.0  
print(circle.radius)  

del circle.radius
try:
    print(circle.radius)  
except Exception as e:
    print(e)

# help(circle)

class CircleD:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property"""
        print("Get radius")
        return self._radius
    
    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")

print("#Decorator ------------->> ", dir(CircleD.radius))

class PointReadOnly:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    
#Write Only
import hashlib
import os
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @property
    def password(self):
        raise AttributeError("Password is write-only")
    
    @password.setter
    def password(self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(salt 
                                + plaintext.encode("utf-8")).hexdigest()


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        print("Getting x: ", self._x)
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        print("Getting y: ", self._y)
        return self._y

    def set_y(self, value):
        self._y = value


point = Point(12, 5)

point.get_x()
point.get_y()

point.set_x(42)
point.get_x()

print("Private -->>", point._x)
print("Private -->>",point._y)
class PointValidate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print("Validated")
        except:
            raise ValueError("x must be a float") from None
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"y" must be a number') from None

class propSquare:
    def __init__(self, start):
        self.value = start
    def getX(self):
        return self.value ** 2
    def setX(self, value):
        self.value = value;
    x = property(getX, setX)

P = propSquare(3)
Q = propSquare(32)
print(P.x)
print(Q.x)

#Esempio di implementazione di di una Property
class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)
    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

class Person:
    def getName(self):
        print("Getting name")
        return self.__name
    def setName(self, value):
        print("Setting name to " + value)
        self.__name = value
    name = Property(getName, setName)
    

class WriteCoordinateError(Exception):
    pass

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        raise WriteCoordinateError("x cordinate read only")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        raise WriteCoordinateError("y cordinate read only")
 
    def __str__(self):
        return f"({self._x}, {self._y})"
    
print("#Circle------------\n")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = float(value)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

circle = Circle(42)
print(circle.radius)
print(circle.diameter)

print("#1-----------------\n")
class Sensore():
    def __init__(self, temp = 0.0):
        self.temp = temp
        
    def toFahrenheit(self):
        return 32 + (self.temp * 1.8)

s = Sensore()
s.temp = 24.0
print(s.toFahrenheit())
print(s.__dict__)

print("#2-----------------\n")

class Sensore2():
    def __init__(self, temp = 0.0) -> None:
        self.__temp = temp
        
    def toFahrenheit(self):
        return 32 + (self.__temp * 1.8)
    
    def getTemp(self):
        return self.__temp
    
    def setTemp(self, t):
        if t < 0:
            t = 0
            print("temp non permessa")
        self.__temp = t

s2 = Sensore2()
s2.setTemp(30.0)
print(s2.toFahrenheit())
s2.setTemp(-10.0)
print(s2.getTemp())
print(s2.__dict__)

print('#3-------------------------\n')
class Sensore3():
    def __init__(self, temp = 0):
        self.__temp = temp

    def toFahrenheit(self):
        return 32 + (self.__temp * 1,8)
    
    def getTemp(self):
        print("get")
        return self.__temp

    def setTemp(self, t):
        print("set")
        if t < 0:
            t = 0
            print("temp non permesso")
        self.__temp = t    

    # metodo per settare le proprietà
    #temp = property(getTemp, setTemp)
    temp = property()
    temp = temp.getter(getTemp)
    temp = temp.setter(setTemp)  

s3 = Sensore3()
s3.temp = 30.0
print(s3.temp)
s3.setTemp(-10.0)
print(s3.getTemp())
print(s3.__dict__)

print("4----------------\n")
class Sensore4():
    def __init__(self, temp = 0.0):
        self.__temp = temp
    
    def toFahrenheit(self):
        return 32 + (self.__temp * 1.8)

    @property
    def temperatura(self):
        return self.__temp
    
    @temperatura.setter
    def temperatura(self, t):
        if t < 0:
            t = 0
            print("temp non permessa")
        self.__temp = t
    
s4 = Sensore4()
s4.temperatura = 12.0
print(s4.temperatura)

class person:
    def __init__(self, name="") -> None:
        self.__name = name

    def setname(self, name) -> None:
        print('setname() called')
        self.__name = name
    
    def getname(self) -> String:
        print('getname() called')
        return self.__name

    def delname(self) -> None:
        print('delname() called')
        del self.__name
    
    # Set property to use get_name, set_name
    # and del_name methods
    name = property(getname, setname, delname)

p1 = person("Pippo")
print(p1.name)
p1.name="Steve"
print(p1.name)

del p1.name

# --------------------------------------------------------------------------------------------------

import math

def empty_strings(user_object):
    for prop_name in user_object.__dict__.keys():

        print("prop_name --->> ", prop_name)

        prop_value = getattr(user_object, prop_name)
        print("prop_value --->> ", prop_value)

        if isinstance(prop_value, str):
            setattr(user_object, prop_name, '')

        if isinstance(prop_value, int):
            setattr(user_object, prop_name, 0)


class Circle:
    counter = 0 # variabile di classe
    def __init__(self, radius, name) -> None:
        if radius < 0:
            raise ValueError("radius must be non-negative")
        
        self.category = "shape" # è publica

        self._radius = radius
        self._area = None
        self.__name = name
        
        Circle.counter += 1

        self.scope_varible = "instance " + name
        Circle.scope_varible = "class"
        scope_variable = "local"      
        print(scope_variable)  

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError("radius must be non-negative")
        self._radius = val
        self._area = None

    @radius.deleter
    def radius(self):
        print("Deleting radius")
        del self._radius


    @property
    def area(self):
        if self._area is None:
            self._area =  math.pi * (self.radius ** 2)
        
        return self._area
    

    '''
    def get_radius(self):
        return self._radius
    
    def set_radius(self, new_radius):
        if new_radius < 0:
            raise ValueError("radius must be non-negative")

        self._radius = new_radius
    
    def del_radius(self):
        print("Deleting radius")
        del self._radius

    
    #fget = function to call to get the instance attribute value
    #fset = function to call to set the instance attribute value
    radius = property(fget=get_radius, 
                    fset=set_radius, 
                    fdel=del_radius,
                    doc="radius fo circle"
                    )
    
   
    radius = property(get_radius)
    radius = radius.setter(set_radius)
    radius = radius.deleter(del_radius)
    '''

    def __str__(self):
       return 'Recap: ' + self.__name + ', ' + str(self.radius)


circle = Circle(5, "Pippo")

print(circle)

print(circle.radius)

print(circle.__dict__)

circle.__dict__['_radius'] = 10

print(circle.radius)

print(circle.radius)



# circle.radius = -10

print(circle.__dict__)
print(circle._Circle__name)

if hasattr(circle, 'category'):
    print("Category is " + circle.category)

print(type(circle).__name__)

print(circle.scope_varible)
print(Circle.scope_varible)


empty_strings(circle)
print(circle)

del(circle.radius) # così cancella la proprietà

print("-----------------------------------------------")

class Person:
    def __init__(self, age) -> None:
        self._age = age  # Meglio usare _age come attributo privato

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def get_age(self):
        print("Getting the age ...")
        return self._age

    def set_age(self, age):
        if age < 0:
            print("He cannot have negative age")
        else:
            print("Setting age ...")
            self._age = age  # Corretto: usa il valore passato
    
    age = property(get_age, set_age)  # Posizionata correttamente
    
    def category(self):  # Nome corretto
        if self._age < 13:
            return "Kid"
        elif self._age >= 13 and self._age <= 19:
            return "Teen"
        elif self._age > 19 and self._age < 65:
            return "Adult"  # Corretto!
        else:
            return "Elderly"

person = Person(25)
print(person.category())  # Output: Adult
print(person.age)         # Output: Getting the age ... 25
person.age = 30           # Output: Setting age ...
print(person.age)         # Output: Getting the age ... 30


# Ovveriding
class Employee(Person):
    @property
    def name(self):
        return super().name.upper()

employee = Employee(35)
employee.name = "Steve"
print(employee.name)

print('--------------Attribute------------------')
class Catcher:
    def __getattr__(self, name):
        print("Getting the {} attribute".format(name))
    def __setattr__(self, name, value):
        print("Setting the {} attribute to {}".format(name, value))
        super().__setattr__(name, value)

C = Catcher()
C.job
C.pay = 100
print(C.pay)