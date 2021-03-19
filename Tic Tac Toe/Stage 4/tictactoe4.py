# write your code here
def printgrid(grid):
    dash = '-' * 9
    m = 0
    print(dash)
    while m < 7:
        print("| ", end = '')
        for i in range(m, m+3):
            print(grid[i], end = ' ')
        print("|")
        m += 3
    print(dash)

grid =  input("Enter cells: ")
printgrid(grid)
play = False
while not play:
    x_play = input("Enter the coordinates: ").split()
    if not x_play[0].isdigit() or not x_play[1].isdigit():
        print("You should enter numbers!")
    elif int(x_play[0]) not in range(1, 4) or int(x_play[1]) not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
    elif grid[3 * (int(x_play[0]) - 1) + int(x_play[1]) - 1] in ['X', 'O']:
        print("This cell is occupied! Choose another one!")
    else:
        location = 3 * (int(x_play[0]) - 1) + int(x_play[1]) - 1
        grid = grid[:location] + 'X' + grid[location + 1:]
        play = True
printgrid(grid)