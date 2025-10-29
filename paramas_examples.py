#paramas

def greet(name, messagge):
    print(f"{messagge}, {name}!")

greet("Alice", "Ciao")  # Output: Ciao, Alice!

greet(messagge="Hi", name="Bob")  # Output: Hi, Bob!

def greet(name, messagge="HI"):
    print(f"{messagge}, {name}!")

greet("Alice")         # Output: Ciao, Alice!  (Usa il valore predefinito)
greet("Bob", "Hey")

# *args → per una lista di valori posizionali
# **kwargs → per un dizionario di valori con nome

def sum_all_params(*numbers):
    return sum(numbers)

print(sum_all_params(1, 2, 3)) 
print(sum_all_params(1, 2, 3, 4, 5, 6, 7, 8)) 

def personal_description(**date_personal):
    for key, value in date_personal.items():
        print(f"{key}: {value}")

personal_description(name="Alice", age=30, city="Roma")

def func_01(a, b=2, *args, c=3, **kwargs):
    print(f"a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}")


def show_date(name, age):
    print(f"Nome: {name}, Età: {age}")


data = {"name": "Alice", "age": 30} #chiavi nome dei paramtri
show_date(**data)


def func_02(a=1, b=2, c=6):
    print(f"a={a}, b={b}, c={c}")

func_02(3, c=8)


def func_arg(a, b, c, d):
    print(f"a={a}, b={b}, c={c}, d={d}")


args = (10, 20)
args += (30, 40)

func_arg(*args)

args = {"a": 10, "b": 20, "c": 30}
args["d"] = 40

func_arg(**args)

func_arg(*(1, 2), **{'d':4, 'c':10})

func_arg(1, *(2, 3), **{'d':4})

func_arg(1, c=3, *(2,), **{'d':4})

func_arg(1, *(2,3),d=4)

func_arg(1, *(2, ), c=3, **{'d':4})