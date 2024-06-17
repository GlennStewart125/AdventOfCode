from typing import TextIO
from itertools import permutations


def main() -> None:
    pairs: {(str, str): int} = {}
    people: set[str] = set()
    file: TextIO
    with open("input.txt", "r") as file:
        line: str
        
        for line in file:
            line_split: [str] = line.split(' ')
            positive_or_negative: int = 1 if line_split[2] == "gain" else -1
            people.add(line_split[0])
            pairs[line_split[0], line_split[-1].strip()[:-1]] = positive_or_negative * int(line_split[3])
            
    max_happiness: int = decideSeating(people, pairs)
    print(max_happiness)

    
def decideSeating(people: set[str], pairs: {(str, str): int}) -> int:
    seating: tuple[str, str, str, str]
    max_happiness: int = 0
    
    for seating in permutations(people):
        happiness: int = 0
        index: int
        
        for index, seat in enumerate(seating):
            left: int = (index - 1) % len(seating)
            right: int = (index + 1) % len(seating)
            happiness += pairs[(seating[index], seating[left])] + pairs[(seating[index], seating[right])]

        if happiness > max_happiness:
            max_happiness = happiness
            
    return max_happiness
        

if __name__ == "__main__":
    main()
