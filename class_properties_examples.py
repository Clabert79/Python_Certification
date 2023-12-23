from pickletools import string1
from tokenize import String


# https://realpython.com/python-getter-setter/

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
        self.age = age

    def get_age(self):
        print("Getting the age ...")
        return self.age;

    def set_age(self, age):
        if age < 0:
            print("He cannot have negative age")
        else:
            print("Setting age ...")
            self.age = age
    
    def cataegory(self):
        if self.age < 13:
            return "Kid"
        elif self.age >= 13 and self.age <= 19:
            return "Teen"
        elif self.age > 19 and self.age < 65:
            return "Teen"
        else:
            return "Elderly"
    age = property(get_age, set_age)


person = Person(25)
