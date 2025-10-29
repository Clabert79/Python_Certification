
def process_data(data):
    match data:
        case "banana":
            print("Monkeys like bananas!")
        case "apple":
            print("Apples are okay.")
        case _:
            print("I don't know that fruit.")
        

data1 = "apple"
data2 = "orange"

process_data(data1)
process_data(data2)

def process_data_simple(data):
    match data:
        case 1:
            print("Data is 1")
        case 2:
            print("Data is 2")
        case _:
            print("Data is not 1 or 2")

process_data_simple(5)

print("Finish")