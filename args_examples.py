def absolute_sum(*args):
    result = 0
    for arg in args:
        result += abs(arg)
    
    return result

print(absolute_sum(1, 3, 4, -5))

numbers = [1 ,5, 9]
print(sum(x for x in numbers))

def number_attributes(**kwargs):
    count = 0
    for args in kwargs.items():
        count += 1
    return count

print(number_attributes(A=1,B=4,C=5))

def list_attributes(**kwargs):
    return list(kwargs.values())

print(type(list_attributes(a=1, b=7, c=9)))


def myFun_1(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun_1(first='Geeks', mid='for', last='Geeks')

def myFun(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)

print("------------------------------------------------------")
def describe_person(name, **kwargs):
    characteristics = f"Characteristics of {name}:"
    
    for argument_name, argument_value in kwargs.items():
        characteristics += f"{argument_name}: {argument_value}"

    print(characteristics)    

describe_person("Thomas", eye_color = "blu", hair_color = "blonde")


def product(first, *values, scale = 1):
    result = first * scale
    for val in values:
        result = result * val

    return result

result = product(1, 2, 3, 4, scale = 8)
# result = product(1, 2, 3, 4, 8) It' the SAME
print(" ---> ", result)


#un metodo per fare il check dei paramtri
def make_table(data, **parms):

    fgcolor = parms.pop('fgcolor', 'black')
    bgcolor = parms.pop('bgcolor', 'white')
    width = parms.pop('width', None)

    fgcolor = parms.pop('border', 1)
    bgcolor = parms.pop('borderstyle', 'grooved')
    width = parms.pop('cellpadding', 10)

    print("Parms == ", parms)
    # No more options se è '0' non scatta
    if parms:
        raise TypeError(f'Unsupported configuration options {list(parms)}')
name = 'pipppo'

make_table(name, fgcolor='black',bgcolor='white', border=1,
                  borderstyle='grooved', cellpadding=10,
                  width=400)
