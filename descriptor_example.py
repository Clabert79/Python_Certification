'''
l descrittore è come propertyviene implementato il tipo di Python . Un descrittore semplicemente attrezzi __get__, __set__ecc
e viene quindi aggiunta ad un'altra classe nella sua definizione

È necessario utilizzare una classe descrittore per incapsulare la logica che la alimenta.

__get__(self, obj, type=None) -> object
__set__(self, obj, value) -> None
__delete__(self, obj) -> None
__set_name__(self, owner, name)
'''

class my_descriptor:
    def __init__(self, initial_value):
        self.value = initial_value
    def __get__(self, instance, instance_type):
        print('In __get__()')
        return self.value
    def __set__(self, instance, value):
        print('In __set__()')
        self.value = value

    def __delete__(self, instance):
        print('In __del__()')
        del self.value

# Class descriptors
class verbose_attribute():
    def __get__(self, obj, type = None) -> object:
        print("accessing the attribute to GET value")
        return 42
    def __set__(self, obj, value) -> None:
        print("accessing the attribute to SET teh value")
        raise AttributeError("Cannot chamge the value")


class foo():
    attribute1 = verbose_attribute()

my_foo_obj = foo()
x = my_foo_obj.attribute1
print(x)
