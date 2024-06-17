from typing import TextIO, Any
import json
from itertools import repeat


def main() -> None:
    file: TextIO = open("input.json")
    json_output: Any = json.load(file)
    total_count_with_red: int = countNumbers(json_output, True)
    total_count_no_red: int = countNumbers(json_output, False)
    print(total_count_with_red)
    print(total_count_no_red)
    file.close()


def countNumbers(data: Any, count_red: bool) -> int:
    if type(data) is type(dict()):
        if not count_red and "red" in data.values():
            return 0
        else:
            return sum(map(countNumbers, data.values(), repeat(count_red)))
    if type(data) is type(list()):
        return sum(map(countNumbers, data, repeat(count_red)))
    if type(data) is type(1):
        return data
    return 0


if __name__ == "__main__":
    main()
