puzzle_input: str = "3113322113"
times: int = 50


def main() -> None:
    result: str = puzzle_input

    for _ in range(0, times):
        result = look_and_say(result)

    print(len(result))


def look_and_say(input_string: str) -> str:
    result: str = ""
    previous_char: str = ""
    previous_count: int = 0
    char: str

    for char in input_string:
        if previous_char == "":
            previous_char = char
            previous_count = 1
        elif previous_char == char:
            previous_count += 1
        else:
            result += str(previous_count) + previous_char
            previous_count = 1
            previous_char = char

    result += str(previous_count) + previous_char
    return result


main()
