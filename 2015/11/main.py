puzzle_input: str = "vzbxkghb"


def main() -> None:
    new_password = findNewPassword(puzzle_input)
    print(new_password)
    new_password = findNewPassword(new_password)
    print(new_password)


def findNewPassword(input_str: str) -> str:
    new_password = increment(input_str)
    while not isValid(new_password):
        new_password = increment(new_password)

    return new_password


def isValid(password: str) -> bool:
    no_illegal_char = notContainsChar(password)
    contains_increasing = containsIncreasing(password)
    contains_two_pairs = containsPairs(password)

    return no_illegal_char and contains_increasing and contains_two_pairs


def notContainsChar(password: str) -> bool:
    no_illegal_char: bool = True
    if 'i' in password or 'o' in password or 'l' in password:
        no_illegal_char = False

    return no_illegal_char


def containsIncreasing(password: str) -> bool:
    contains_increasing: bool = False
    for index in range(0, len(password) - 2):
        currentChar: str = password[index]
        if (ord(password[index + 1]) == ord(currentChar) + 1 and
                ord(password[index + 2]) == ord(currentChar) + 2):
            contains_increasing = True

    return contains_increasing


def containsPairs(password: str) -> bool:
    pairs_count: int = 0
    previous_char: str = ""
    for char in password:
        if char == previous_char:
            pairs_count += 1
            previous_char = ""
        else:
            previous_char = char
    return pairs_count >= 2


def increment(password: str) -> str:
    reversed_password: str = password[::-1]
    index: int = 0
    reversed_new_password: str = ""

    for letter in reversed_password:
        new_value: int = ord(letter) + 1
        wrapped_around: bool = new_value % 122 == 1
        if wrapped_around:
            index += 1
            reversed_new_password += chr(97)
        else:
            reversed_new_password += chr(new_value)
            reversed_new_password += reversed_password[index + 1:]
            break

    return reversed_new_password[::-1]


if __name__ == "__main__":
    main()
