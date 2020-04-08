import random

WIN_CUBE = [a for a in range(1, 16)].append("x")


def random_cube(cube):
    for i in range(100):
        rand = random.choice(list(COMMANDS))
        COMMANDS[rand](cube)
    return cube


def create_cube():
    cube = [x for x in range(1, 16)]
    cube.append("x")
    cube = random_cube(cube)
    return cube


def canvas(cube):
    a = cube[0:4]
    b = cube[4:8]
    c = cube[8:12]
    d = cube[12:]
    print("{}\n{}\n{}\n{}\n".format(a, b, c, d))

# Up = -4, Down = +4, Left = -1, Right = +1


def up(cube):
    for point in range(4, len(cube)):
        if cube[point-4] == 'x':
            cube[point], cube[point-4] = cube[point-4], cube[point]
            return cube
        else:
            continue
    return cube


def down(cube):
    for point in range(0, len(cube)-4):
        if cube[point+4] == 'x':
            cube[point], cube[point+4] = cube[point+4], cube[point]
            return cube
        else:
            continue
    return cube


def left(cube):
    for point in range(0, len(cube)):
        if point != 0 and point != 4 and point != 8 and point != 12:
            if cube[point-1] == 'x':
                cube[point], cube[point-1] = cube[point-1], cube[point]
                return cube
            else:
                continue
    return cube


def right(cube):
    for point in range(0, len(cube)):
        if point != 3 and point != 7 and point != 11 and point != 15:
            if cube[point+1] == 'x':
                cube[point], cube[point+1] = cube[point+1], cube[point]
                return cube
            else:
                continue
    return cube


COMMANDS = {'w': up,
            's': down,
            'a': left,
            'd': right,
            }


def main():
    command = ''
    cube = create_cube()
    canvas(cube)
    while command != "Exit".lower():
        key_move = input("Enter you step: ").lower()
        command = key_move
        if command == "Exit".lower():
            return print('Game over. Bye!')
        try:
            COMMANDS[key_move](cube)
        except KeyError:
            print("Wrong Key!!!\nMove not accepted\nTry again")
        # if key_move == "w":
        #     cube = up(cube)
        # elif key_move == "s":
        #     cube = down(cube)
        # elif key_move == "a":
        #     cube = left(cube)
        # elif key_move == "d":
        #     cube = right(cube)
        canvas(cube)
        if cube == WIN_CUBE:
            return print('You win!')


if __name__ == "__main__":
    main()
