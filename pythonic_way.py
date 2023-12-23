# per stampare delle label con paramtri da pytho 3.6
name = 'Claudio'
age = 43
print(f"Hi, I am {name} and I am {age + 1} years old")


route = {'id': 271, 'title': 'Fast App'}
query = {'id': 1, 'render_fast': True}
post = {'email': 'j@mail.com', 'name': 'Jeff'}

'''
NO Pythonic !!!

m1 = {}

for k in query:
    m1[k] = query[k]

 for k in post:
    m1[k] = post[k]

for k in route:
    m1[k] = route[k]
'''

m1 = { **route, **query, **post}    # se c'è una chiave uguale l'ultima in oridine vince
                                    # in questo caso id vale '1' che è quello di quey che arriva dopo
print(m1)

high_measurements = [23, 27, 28, 45, 50]

'''
NO Pythonic !!!
high_count = 0
for m in hight:
    high_count += 1

'''
# in pythonic way la sum si fa in questo modo
high_count = sum(1 for _ in high_measurements)
print(high_count)


def generator_fibonacci():
    current, nxt = 0, 1

    while True:
        current, nxt = nxt, nxt + current
        yield current

import itertools

for part in itertools.islice(generator_fibonacci(), 3):
    print(part)
