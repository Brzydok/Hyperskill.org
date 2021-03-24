cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def matrix():
    p = 9 * "-"
    print(p)
    print("|", cells[0], cells[1], cells[2], "|")
    print("|", cells[3], cells[4], cells[5], "|")
    print("|", cells[6], cells[7], cells[8], "|")
    print(p)


def new_move_x():
    while True:

        n = input("Enter the coordinates: ").split()

        if (n[0].isnumeric() and n[1].isnumeric()) != True:
            print("You should enter numbers!")
            continue

        elif int(n[0]) > 3 or int(n[1]) > 3:
            print("Coordinates should be from 1 to 3!")
            continue

        elif int(n[0]) < 1 or int(n[1]) < 1:
            print("Coordinates should be from 1 to 3!")
            continue

        elif int(n[0]) == 1:
            if int(n[1]) == 1:
                if cells[0] == "X" or cells[0] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[0] = "X"
            elif int(n[1]) == 2:
                if cells[1] == "X" or cells[1] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[1] = "X"
            elif int(n[1]) == 3:
                if cells[2] == "X" or cells[2] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[2] = "X"
        elif int(n[0]) == 2:
            if int(n[1]) == 1:
                if cells[3] == "X" or cells[3] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[3] = "X"
            elif int(n[1]) == 2:
                if cells[4] == "X" or cells[4] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[4] = "X"
            elif int(n[1]) == 3:
                if cells[5] == "X" or cells[5] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[5] = "X"
        elif int(n[0]) == 3:
            if int(n[1]) == 1:
                if cells[6] == "X" or cells[6] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[6] = "X"
            elif int(n[1]) == 2:
                if cells[7] == "X" or cells[7] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[7] = "X"
            elif int(n[1]) == 3:
                if cells[8] == "X" or cells[8] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[8] = "X"
        break


def new_move_o():
    while True:

        n = input("Enter the coordinates: ").split()

        if (n[0].isnumeric() and n[1].isnumeric()) != True:
            print("You should enter numbers!")
            continue

        elif int(n[0]) > 3 or int(n[1]) > 3:
            print("Coordinates should be from 1 to 3!")
            continue

        elif int(n[0]) < 1 or int(n[1]) < 1:
            print("Coordinates should be from 1 to 3!")
            continue

        elif int(n[0]) == 1:
            if int(n[1]) == 1:
                if cells[0] == "X" or cells[0] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[0] = "O"
            elif int(n[1]) == 2:
                if cells[1] == "X" or cells[1] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[1] = "O"
            elif int(n[1]) == 3:
                if cells[2] == "X" or cells[2] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[2] = "O"
        elif int(n[0]) == 2:
            if int(n[1]) == 1:
                if cells[3] == "X" or cells[3] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[3] = "O"
            elif int(n[1]) == 2:
                if cells[4] == "X" or cells[4] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[4] = "O"
            elif int(n[1]) == 3:
                if cells[5] == "X" or cells[5] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[5] = "O"
        elif int(n[0]) == 3:
            if int(n[1]) == 1:
                if cells[6] == "X" or cells[6] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[6] = "O"
            elif int(n[1]) == 2:
                if cells[7] == "X" or cells[7] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[7] = "O"
            elif int(n[1]) == 3:
                if cells[8] == "X" or cells[8] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cells[8] = "O"
        break

def result():
    x_counter = cells.count("X")
    o_counter = cells.count("O")
    _counter = cells.count("_")
    gs = [x for x in cells]
    winner = [[gs[0], gs[1], gs[2]],  # 0
              [gs[3], gs[4], gs[5]],  # 1
              [gs[6], gs[7], gs[8]],  # 2
              [gs[0], gs[4], gs[8]],  # 3
              [gs[6], gs[4], gs[2]],  # 4
              [gs[0], gs[3], gs[6]],  # 5
              [gs[1], gs[4], gs[7]],  # 6
              [gs[2], gs[5], gs[8]]]  # 7

    if x_counter > o_counter + 1 or o_counter > x_counter + 1:
        print("Impossible")
    elif ["X", "X", "X"] in winner and ["O", "O", "O"] in winner:
        print("Impossible")
    elif ["X", "X", "X"] in winner:
        print("X wins")
    elif ["O", "O", "O"] in winner:
        print("O wins")
    else:
        print("Draw")

matrix()
new_move_x()
matrix()
new_move_o()
matrix()
new_move_x()
matrix()
new_move_o()
matrix()
new_move_x()
matrix()
result()
new_move_o()
matrix()
result()
new_move_x()
matrix()
result()
new_move_o()
matrix()
result()
new_move_x()
matrix()
result()
