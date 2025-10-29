'''
https://peps.python.org/pep-0636/
https://benhoyt.com/writings/python-pattern-matching/

'''

command = input("What are you doing next? ")

print(command.split())

match command.split():
    case ["quit"]:
        print("Goodbye!")

    case [action]:
        print(f"Action: {action}")  

    case [action, obj]:
        print(f"Action: {action}, Object: {obj}")
    