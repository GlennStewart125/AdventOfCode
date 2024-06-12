from enum import Enum


class Instruction(Enum):
    ON = 1
    OFF = 2
    TOGGLE = 3


def main():
    wrong_grid: [[bool]] = [[False for _ in range(0, 1000)] for _ in range(0, 1000)]
    elvish_grid: [[int]] = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]

    with open("input.txt", "r") as file:
        for line in file:
            x_start: int
            y_start: int
            x_end: int
            y_end: int
            split_string: [str] = line.split(' ')
            instruction: Instruction = getInstruction(split_string[1])
            x_start, y_start, x_end, y_end = getCoordinates(split_string)

            for x in range(x_start, x_end + 1):
                for y in range(y_start, y_end + 1):
                    performWrongInstruction(instruction, wrong_grid, x, y)
                    performElvishInstruction(instruction, elvish_grid, x, y)

        wrong_lit_count: int = sum([sum(x) for x in wrong_grid])
        correct_elvish_count: int = sum([sum(x) for x in elvish_grid])
        print("wrong count: {}, correct elvish count: {}".format(
            wrong_lit_count, correct_elvish_count))


def getCoordinates(split_string: [str]):
    x_start: int = 0
    y_start: int = 0
    x_end: int = 0
    y_end: int = 0

    if len(split_string) == 4:
        x_start, y_start = map(int, split_string[1].split(','))
        x_end, y_end = map(int, split_string[3].split(','))
    elif len(split_string) == 5:
        x_start, y_start = map(int, split_string[2].split(','))
        x_end, y_end = map(int, split_string[4].split(','))

    return x_start, y_start, x_end, y_end


def performWrongInstruction(instruction: Instruction, grid: [[bool]], x: int, y: int):
    match instruction:
        case Instruction.ON:
            grid[x][y] = True
        case Instruction.OFF:
            grid[x][y] = False
        case Instruction.TOGGLE:
            grid[x][y] = not grid[x][y]


def performElvishInstruction(instruction: Instruction, grid: [[int]], x: int, y: int):
    match instruction:
        case Instruction.ON:
            grid[x][y] += 1
        case Instruction.OFF:
            grid[x][y] = max(0, grid[x][y] - 1)
        case Instruction.TOGGLE:
            grid[x][y] += 2


def getInstruction(instruction: str):
    match instruction:
        case "on":
            return Instruction.ON
        case "off":
            return Instruction.OFF
        case _:
            return Instruction.TOGGLE


if __name__ == "__main__":
    main()
