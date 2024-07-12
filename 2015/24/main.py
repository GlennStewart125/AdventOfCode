from itertools import combinations
from sys import maxsize
from functools import reduce
from operator import mul


def getValues(file_name: str) -> [int]:
    return [int(i.strip()) for i in open(file_name, 'r')]


def main() -> None:
    number_of_groups: int = 4
    weights: [int] = getValues("input.txt")
    target_weight: int = int(sum(weights) / number_of_groups)
    qe_best: int = maxsize
    group_size: int

    for group_size in range(len(weights)):
        qe_list: [int] = [reduce(mul, comb) for comb in combinations(weights, group_size)
                          if sum(comb) == target_weight]

        if qe_list:
            qe_min = min(qe_list)
            if qe_min < qe_best:
                qe_best = qe_min

    print(qe_best)


main()
