from itertools import product


def main() -> None:
    eggnog_amount: int = 150
    containers: [int] = []

    with open("input.txt", "r") as file:
        container: str
        for container in file:
            containers.append(int(container))

    valid_combinations: int
    min_combinations_count: int
    valid_combinations, min_combinations_count = getResults(containers, eggnog_amount)
    print(valid_combinations)
    print(min_combinations_count)


def getResults(containers: [int], eggnog_amount: int) -> (int, int):
    bools: [bool] = [True, False]

    combinations: [(int, [bool])] = [(i, list(c)) for i, c in enumerate(product(bools, repeat=len(containers)))]
    eggnog_amounts: [(int, int)] = [(index, sum([con * com for con, com in zip(containers, combination)]))
                                    for index, combination in combinations]
    valid_combinations: [(int, bool)] = [(index, True) for index, amount in eggnog_amounts if amount == eggnog_amount]

    valid_indices: [int] = [index for index, _ in valid_combinations]
    combinations_container_count: [int] = [sum(combinations[index][1]) for index in valid_indices]
    min_container_count: int = min(combinations_container_count)
    combinations_min_container_count: int = len([True for count in combinations_container_count
                                                 if count == min_container_count])

    return len(valid_combinations), combinations_min_container_count


if __name__ == "__main__":
    main()
