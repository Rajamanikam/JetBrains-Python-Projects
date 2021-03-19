def generate_cells():
    cells = "         "
    cells = [cells[cell:cell+3] for cell in range(0, 9, 3)]
    print_board(cells)
    return cells


def print_board(cells):
    print("---------")
    for row in cells:
        print(f"| {row[0]} {row[1]} {row[2]} |")
    print("---------")


def columns(cells):
    return [[row[index] for row in cells] for index in range(3)]


def diagonals(cells):
    return [[row[index] for index, row in enumerate(cells)], [row[index] for index, row in enumerate(reversed(cells))]]


def wins(x_or_o, cells):
    for row in cells:  # Checking rows
        if row.count(x_or_o) == 3:
            return True
    for column in columns(cells):  # Checking columns
        if column.count(x_or_o) == 3:
            return True
    for diagonal in diagonals(cells):  # Checking diagonals
        if diagonal.count(x_or_o) == 3:
            return True


def empty_cells(cells):
    # True if at least a cell is still empty
    return bool(sum(row.count(" ") for row in cells))


def xo_count(x_or_o, cells):
    return sum(row.count((x_or_o)) for row in cells)


def outcomes(cells):
    # Impossible outcomes:
    if abs(xo_count("X", cells) - xo_count("O", cells)) > 1:
        return "Impossible"
    if wins("X", cells) and wins("O", cells):
        return "Impossible"

    # Winning outcomes:
    if wins("X", cells):
        return "X wins"
    if wins("O", cells):
        return "O wins"

    # Game not finished and draw:
    if not wins("X", cells) and not wins("O", cells):
        return "Game not finished" if empty_cells(cells) else "Draw"


def playing(cells):
    while outcomes(cells) == "Game not finished":
        player_move(cells)
        print_board(cells)
    print(outcomes(cells))


def player_move(cells):
    x_or_o = determine_player(cells)
    print(f"Actual player: {x_or_o}")
    move_validity = None
    while not move_validity:
        coordinates = input("Enter the coordinates in the format 'Y X' where Y is the row and X is the column: ")
        move_validity = check_coordinates(coordinates, cells)
    coordinate_y = int(coordinates[0]) -1
    coordinate_x = int(coordinates[2]) - 1
    row = list(cells[coordinate_y]) # Row being modified
    row[coordinate_x] = x_or_o 
    cells[coordinate_y] = row


def determine_player(cells):
    return "O" if xo_count("X", cells) - xo_count("O", cells) > 0 else "X"


def check_coordinates(coordinates, cells):
    if len(coordinates) < 3:
        print("The coordinates should be in the format Y X with a space between the number.")
        return False
    if not coordinates[0].isnumeric() and not coordinates[2].isnumeric():
        print("You should enter numbers!")
        return False
    if int(coordinates[0]) not in range(1, 4) or int(coordinates[2]) not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        return False
    coordinate_y = int(coordinates[0]) -1
    coordinate_x = int(coordinates[2]) - 1
    if cells[coordinate_y][coordinate_x] != " ":
        print("This cell is occupied! Choose another one!")
        return False
    return True


def main():
    cells = generate_cells()
    playing(cells)


if __name__ == "__main__":
    main()