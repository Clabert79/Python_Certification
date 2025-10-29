'''
TRIANGOLO '*'
'''
num_rows = 5

for i in range(1, num_rows + 1):
    #space
    for j in range(num_rows - i):
        print(" ", end="")

    #asterisk     
    for j in range(i):
        print("*", end=" ")
    print()

# **********************************************************************************************************************************