print(walrus := True)
print(type(walrus))

# No Walrus Operator

inputs = list()

while True:
    current = input("Write something: ")
    if current == "quit":
        break
    inputs.append(current)

# Walrus Operator
inputs = list()

while (current := input("Write something: ")) != "quit":
    inputs.append(current)

a = "piiiiippooooo"
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")


value = input("Enter a number: ")
if value.isnumeric():
    print(f"The number is {value}")
#walrus
if (value := input("Enter a number: ")).isnumeric():
    print(f"The number is {value}")
# --------------------------------------------------------------


while True:
    data = input("Inserisci qualcosa (o scrivi 'stop' per terminare): ")
    if data == "stop":
        break
    print(f"Hai scritto: {data}")
#walrus
while (data := input("Inserisci qualcosa (o scrivi 'stop' per terminare): ")) != "stop":
    print(f"Hai scritto: {data}")
# --------------------------------------------------------------

numbers = [10, 15, 21, 33, 40]
filtered = []
for n in numbers:
    if n % 3 == 0:
        filtered.append(n)
print(filtered)
#walrus
filtered = [n for n in numbers if(remaider := n % 3) == 0]
print(filtered)
# --------------------------------------------------------------

with open("file.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())
#walrus
with open("file.txt", "r") as f:
    while (line := f.readline().strip()):
        print(line)
# --------------------------------------------------------------

counts = {}
items = ['a', 'b', 'a', 'c', 'b', 'a']

for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
print(counts)
#walrus
for item in items:
    counts[item] = (current := counts.get(item, 0)) + 1
print(counts)
# --------------------------------------------------------------

data = [("Alice", 85), ("Bob", 42), ("Charlie", 95)]
threshold = 50

total = 0
for name, score in data:
    if score > threshold:
        total += score
print(total)
#walrus
total = sum(score for name, score in data if(valid := score > threshold))
print(total)
'''
Other Examples:

discount = 0.0
if (mo := re.search(r'(\d+)% discount', advertisement)):
    discount = float(mo.group(1)) / 100.0

# Loop over fixed length blocks
while (block := f.read(256)) != '':
    process(block)

[clean_name.title() for name in names
 if (clean_name := normalize('NFC', name)) in allowed_names]
'''
