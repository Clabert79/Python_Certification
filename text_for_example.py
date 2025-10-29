
board = [["-"]*3]*3
print(board)

board[1][0] = "X"

# Print board to screen
for row in board:
    print(f"{row[0]} {row[1]} {row[2]}")

board_1 = [["-"]*3 for _ in range(3)] # ha creato 3 righe diverse

board_1[1][0] = "X"

for row in board_1:
    print(f"{row[0]} {row[1]} {row[2]}")

pippo = 4.1
pippo = "4.1"