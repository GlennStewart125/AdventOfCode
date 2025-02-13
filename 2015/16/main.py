from typing import TextIO

MFCSAM: {str: int} = {}


def main() -> None:
    fill_mfcsam()
    file: TextIO

    with open("input.txt", "r") as file:
        line: str
        for line in file:
            split: [str] = line.split(' ')
            is_correct_sue: bool = match_compounds(split)
            if is_correct_sue:
                print(split[1][:-1])
                break


def match_compounds(split: [str]) -> bool:
    component_count: int = 1
    try:
        while True:
            compound: str = split[2 * component_count][:-1]
            compound_amount: int = int(split[2 * component_count + 1][:-1])
            if not is_match(compound, compound_amount):
                return False
            component_count += 1
    except IndexError:
        return True


def is_match(compound: str, amount: int) -> bool:
    if compound == "cats" or compound == "trees":
        return amount > MFCSAM[compound]
    elif compound == "pomeranians" or compound == "goldfish":
        return amount < MFCSAM[compound]
    else:
        return amount == MFCSAM[compound]


def fill_mfcsam():
    MFCSAM["children"] = 3
    MFCSAM["cats"] = 7
    MFCSAM["samoyeds"] = 2
    MFCSAM["pomeranians"] = 3
    MFCSAM["akitas"] = 0
    MFCSAM["vizslas"] = 0
    MFCSAM["goldfish"] = 5
    MFCSAM["trees"] = 3
    MFCSAM["cars"] = 2
    MFCSAM["perfumes"] = 1


if __name__ == "__main__":
    main()
