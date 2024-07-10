from typing import TextIO


def main() -> None:
    length_difference1: int = 0
    length_difference2: int = 0
    file: TextIO

    with open("input.txt", "r") as file:
        line: str

        for line in file:
            length_difference1 += len(line[:-1]) - len(eval(line))
            length_difference2 += 2 + line[:-1].count('"') + line[:-1].count('\\')

    print(length_difference1)
    print(length_difference2)


main()
