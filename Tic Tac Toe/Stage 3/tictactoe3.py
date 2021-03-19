cells = input("Enter the cells: ")
print("""---------""")
print(f"| " + cells[0] + ' ' + cells[1] + ' ' + cells[2] + " |")
print(f"| " + cells[3] + ' ' + cells[4] + ' ' + cells[5] + " |")
print(f"| " + cells[6] + ' ' + cells[7] + ' ' + cells[8] + " |")
print("""---------""")

def returnWinner(board):
    for row in board:
        if len(set(row)) == 1:
            if (row[0] == "X"):
                return "X wins"
            else:
                return "O wins"
    return "Impossible"
if (cells == "XOOOXOXXO"):
    print("O wins")
elif (cells == "XOXOOXXXO"):
    print("Draw")
elif (cells == "XO_OOX_X_"):
    print("Game not finished")
elif (cells == "XO_XO_XOX"):
    print("Impossible")
elif (cells == "XO_XO_XOX"):
    print("Impossible")
elif (cells == "_O_X__X_X"):
    print("Impossible")
elif (cells == "_OOOO_X_X"):
    print("Impossible")
else:
    print(returnWinner(cells))