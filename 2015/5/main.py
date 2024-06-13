vowels: {str} = {'a', 'e', 'i', 'o', 'u'}
naughty_strings: {str} = {
    'ab',
    'cd',
    'pq',
    'xy'
}


def main() -> None:
    with open("input.txt", "r") as file:
        nice_strings: int = 0
        better_nice_strings: int = 0
        for string in file:
            if isPartOneNice(string):
                nice_strings += 1
            if isBetterNice(string):
                better_nice_strings += 1

        print("nice string count: {}".format(nice_strings))
        print("better nice string count: {}".format(better_nice_strings))


def isPartOneNice(string: str) -> bool:
    prev_char: str = ''
    vowel_count: int = 0
    has_double: bool = False

    for char in string:
        if char in vowels:
            vowel_count += 1
        if prev_char + char in naughty_strings:
            return False
        if prev_char == char:
            has_double = True
        prev_char = char

    if has_double and vowel_count >= 3:
        return True

    return False


def isBetterNice(string: str) -> bool:
    all_pairs: {(str, str): int} = {}
    char_two_behind: str = ''
    char_one_behind: str = ''
    has_repeat_with_space: bool = False
    has_pair: bool = False

    for index, char in enumerate(string):
        if char_one_behind == '':
            char_one_behind = char
            continue

        if char_two_behind == char:
            has_repeat_with_space = True

        existing_pair_index: int = all_pairs.get((char_one_behind, char))
        if existing_pair_index and index - existing_pair_index > 1:
            has_pair = True

        if not existing_pair_index:
            all_pairs[char_one_behind, char] = index
        char_two_behind = char_one_behind
        char_one_behind = char

        if has_repeat_with_space and has_pair:
            return True
    return False


if __name__ == "__main__":
    main()
