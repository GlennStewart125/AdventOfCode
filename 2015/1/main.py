from typing import TextIO


def main() -> None:
    file: TextIO
    with open("input.txt", "r") as file:
        floor: int = 0
        position: int = 1
        position_found: bool = False

        while True:
            char: str = file.read(1)
            if not char:
                print("floor: {}".format(floor))
                break
            elif char == '(':
                floor += 1
            elif char == ')':
                floor -= 1

            if floor < 0 and not position_found:
                print("position: {}".format(position))
                position_found = True

            position += 1


main()
