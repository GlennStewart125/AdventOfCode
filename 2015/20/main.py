def main() -> None:
    presents_target: int = 36000000
    multiplier_part1: int = 10
    multiplier_part2: int = 11
    max_house_number_part1: int = int(presents_target / multiplier_part1)
    max_house_number_part2: int = int(presents_target / multiplier_part2)
    house_presents_part1: [int] = getHousePresents(max_house_number_part1, multiplier_part1, max_house_number_part1)
    house_presents_part2: [int] = getHousePresents(max_house_number_part2, multiplier_part2, 50)

    printHouseNumber(house_presents_part1, presents_target)
    printHouseNumber(house_presents_part2, presents_target)


def getHousePresents(max_house_number: int, multiplier: int, house_limit: int) -> [int]:
    house_presents: [int] = [0] * max_house_number

    for elf in range(1, max_house_number):
        elf_range: int = min(house_limit * elf, max_house_number)
        for house_number in range(elf, elf_range, elf):
            house_presents[house_number] += elf * multiplier

    return house_presents


def printHouseNumber(house_presents: [int], presents_target: int) -> None:
    for house_number, house_presents in enumerate(house_presents):
        if house_presents >= presents_target:
            print(house_number)
            break


main()
