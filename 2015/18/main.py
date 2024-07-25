from typing import TextIO


def main() -> None:
    steps: int = 100
    state: [[bool]] = []
    with_corners: bool = True
    file: TextIO

    with open("input.txt", "r") as file:
        file_row: str
        for file_row in file:
            light: str
            light_row: [bool] = []
            for light in file_row.strip():
                if light == '.':
                    light_row.append(False)
                else:
                    light_row.append(True)
            state.append(light_row)

    if with_corners:
        set_corners(state)
    for step in range(steps):
        state = perform_step(state, with_corners)

    on_count: int = sum([sum(row) for row in state])
    print(str(on_count))


def perform_step(state_current: [[bool]], with_corners: bool) -> [[bool]]:
    state_new: [[bool]] = []
    y: int
    row: [bool]

    for y, row in enumerate(state_current):
        row_new: [bool] = []
        x: int
        light: bool
        for x, light_bool in enumerate(row):
            row_new.append(get_new_light_value(state_current, x, y, light_bool))
        state_new.append(row_new)

    if with_corners:
        set_corners(state_new)
    return state_new


def set_corners(state: [[bool]]) -> None:
    state[0][0] = True
    state[0][-1] = True
    state[-1][0] = True
    state[-1][-1] = True


def get_new_light_value(state: [[bool]], x: int, y: int, light_bool: bool) -> bool:
    surrounding_range: [int] = [-1, 0, 1]
    count: int = 0
    y_neighbour: int
    x_neighbour: int

    for y_neighbour in surrounding_range:
        for x_neighbour in surrounding_range:
            if y_neighbour == 0 and x_neighbour == 0:
                continue
            elif y_neighbour + y < 0 or y_neighbour + y >= len(state):
                continue
            elif x_neighbour + x < 0 or x_neighbour + x >= len(state):
                continue
            else:
                count += state[y_neighbour + y][x_neighbour + x]

    if light_bool and count == 2 or count == 3:
        return True
    elif not light_bool and count == 3:
        return True
    else:
        return False


main()
