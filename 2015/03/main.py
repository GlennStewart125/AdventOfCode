from typing import TextIO


class Santa:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
        self.visited: {[int, int]} = {(0, 0)}

    def move(self, direction: str) -> None:
        match direction:
            case '^':
                self.y += 1
            case '>':
                self.x += 1
            case 'v':
                self.y -= 1
            case '<':
                self.x -= 1


def main() -> None:
    file: TextIO
    with open("input.txt", "r") as file:
        onlySanta(file)
        file.seek(0)
        doubleTrouble(file)


def onlySanta(file: TextIO) -> None:
    santa: Santa = Santa(0, 0)
    while True:
        direction: str = file.read(1)
        if not direction:
            break

        santa.move(direction)
        if (santa.x, santa.y) not in santa.visited:
            santa.visited.add((santa.x, santa.y))

    print("only santa: {}".format((len(santa.visited))))


def doubleTrouble(file: TextIO) -> None:
    real_santa: Santa = Santa(0, 0)
    robot_santa: Santa = Santa(0, 0)
    move_real_santa: bool = True

    while True:
        direction: str = file.read(1)
        if not direction:
            break
        if move_real_santa:
            real_santa.move(direction)
            real_santa.visited.add((real_santa.x, real_santa.y))
        else:
            robot_santa.move(direction)
            robot_santa.visited.add((robot_santa.x, robot_santa.y))
        move_real_santa = not move_real_santa

    print("santa + robot: {}".format(len(real_santa.visited | robot_santa.visited)))


main()
