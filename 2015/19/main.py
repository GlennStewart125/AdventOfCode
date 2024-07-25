"""
The answer to the second question was based on the insights given by the use "askalski" in the reddit thread:
https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju/
"""


def read(file_name: str) -> [str]:
    return [i.strip() for i in open(file_name, 'r')]


def main() -> None:
    lines: [str] = read("input.txt")
    medicine_molecule: str = lines[-1]
    replacements: [(str, str)] = []

    replacement: (str, str)
    for replacement in lines[:-2]:
        replacement_split: [str] = replacement.strip().split(' ')
        replacements.append((replacement_split[0], replacement_split[2]))

    distinct_molecules: set[str] = get_new_molecules(medicine_molecule, replacements)
    fewest_steps: int = get_fewest_steps_to_create_molecule_count(medicine_molecule)
    print("Distinct molecules count: {}".format(len(distinct_molecules)))
    print("fewest steps: {}".format(fewest_steps))


def get_new_molecules(starting_molecule: str, replacements: [(str, str)]) -> set[str]:
    distinct_molecules: set[str] = set()

    from_replacement: str
    to_replacement: str
    for from_replacement, to_replacement in replacements:
        index: int
        for index in range(len(starting_molecule)):
            x_len: int = len(from_replacement)
            if starting_molecule[index:index + x_len] == from_replacement:
                new_molecule: str = starting_molecule[:index] + to_replacement + starting_molecule[index + x_len:]
                distinct_molecules.add(new_molecule)

    return distinct_molecules


def get_fewest_steps_to_create_molecule_count(medicine_molecule: str):
    token: str
    count_token: int = sum(token.isupper() for token in medicine_molecule)
    count_parentheses: int = medicine_molecule.count("Rn") + medicine_molecule.count("Ar")
    count_comma: int = medicine_molecule.count("Y")
    return count_token - count_parentheses - (2 * count_comma) - 1


main()
