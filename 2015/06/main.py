from enum import Enum
from typing import TextIO


class Instruction(Enum):
    ON: int = 1
    OFF: int = 2
    TOGGLE: int = 3


def main() -> None:
    wrong_grid: [[bool]] = [[False for _ in range(0, 1000)] for _ in range(0, 1000)]
    elvish_grid: [[int]] = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]

    file: TextIO
    with open("input.txt", "r") as file:
        for line in file:
            x_start: int
            y_start: int
            x_end: int
            y_end: int
            split_string: [str] = line.split(' ')
            instruction: Instruction = get_instruction(split_string[1])
            x_start, y_start, x_end, y_end = get_coordinates(split_string)

            x_pos: int
            y_pos: int
            for x_pos in range(x_start, x_end + 1):
                for y_pos in range(y_start, y_end + 1):
                    perform_wrong_instruction(instruction, wrong_grid, x_pos, y_pos)
                    perform_elvish_instruction(instruction, elvish_grid, x_pos, y_pos)

        bool_list: [bool]
        wrong_lit_count: int = sum([sum(bool_list) for bool_list in wrong_grid])
        correct_elvish_count: int = sum([sum(bool_list) for bool_list in elvish_grid])
        print("wrong count: {}, correct elvish count: {}".format(
            wrong_lit_count, correct_elvish_count))


def get_coordinates(split_string: [str]) -> (int, int, int, int):
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


def perform_wrong_instruction(instruction: Instruction, grid: [[bool]], x: int, y: int) -> None:
    match instruction:
        case Instruction.ON:
            grid[x][y] = True
        case Instruction.OFF:
            grid[x][y] = False
        case Instruction.TOGGLE:
            grid[x][y] = not grid[x][y]


def perform_elvish_instruction(instruction: Instruction, grid: [[int]], x: int, y: int) -> None:
    match instruction:
        case Instruction.ON:
            grid[x][y] += 1
        case Instruction.OFF:
            grid[x][y] = max(0, grid[x][y] - 1)
        case Instruction.TOGGLE:
            grid[x][y] += 2


def get_instruction(instruction: str) -> Instruction:
    match instruction:
        case "on":
            return Instruction.ON
        case "off":
            return Instruction.OFF
        case _:
            return Instruction.TOGGLE


main()
