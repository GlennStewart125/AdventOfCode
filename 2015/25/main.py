def get_values(file_name: str) -> [str]:
    with open(file_name) as f:
        return f.readline().strip().split(' ')


def main() -> None:
    instruction: [str] = get_values("input.txt")
    row_limit: int = int(instruction[-3][:-1])
    column_limit: int = int(instruction[-1][:-1])
    first_code: int = 20151125
    multiplier: int = 252533
    divider: int = 33554393
    row: int = 1
    column: int = 1
    row_max: int = 1
    previous_value: int = 0
    value: int

    while True:
        if row == 1 and column == 1:
            value = first_code
            previous_value = value
        else:
            value = get_code(previous_value, multiplier, divider)
            previous_value = value

        if row == row_limit and column == column_limit:
            break

        if row == 1:
            row = row_max + 1
            row_max = row
            column = 1
        else:
            row -= 1
            column += 1

    print(value)


def get_code(previous_value: int, multiplier: int, divider: int) -> int:
    return int((previous_value * multiplier) % divider)


main()
