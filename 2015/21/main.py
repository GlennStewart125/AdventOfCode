import itertools
import sys


class Item:

    def __init__(self, name: str, cost: int, damage: int, armor: int):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor


weapons: [Item] = [Item("Dagger", 8, 4, 0),
                   Item("Shortsword", 10, 5, 0),
                   Item("Warhammer", 25, 6, 0),
                   Item("Longsword", 40, 7, 0),
                   Item("Greataxe", 74, 8, 0)
                   ]
armors: [Item] = [Item("Leather", 13, 0, 1),
                  Item("Chainmail", 31, 0, 2),
                  Item("Splintmail", 53, 0, 3),
                  Item("Bandedmail", 75, 0, 4),
                  Item("Platemail", 102, 0, 5),
                  ]
rings: [Item] = [Item("Damage +1", 25, 1, 0),
                 Item("Damage +2", 50, 2, 0),
                 Item("Damage +3", 100, 3, 0),
                 Item("Defense +1", 20, 0, 1),
                 Item("Defense +2", 40, 0, 2),
                 Item("Defense +3", 80, 0, 3),
                 ]


def getValues(file_name: str) -> [int]:
    return [int(i.strip().split(' ')[-1]) for i in open(file_name, 'r')]


def main() -> None:
    lines: [int] = getValues("input.txt")
    enemy_hp: int = lines[0]
    enemy_damage: int = lines[1]
    enemy_armor: int = lines[2]
    cost_victory_min: int = sys.maxsize
    cost_loss_max: int = 0

    combinations: [[Item]] = getOutfitCombinations()
    combination: [Item]
    for combination in combinations:
        player_armor: int
        player_damage: int
        cost: int

        player_damage, player_armor, cost = getOutfitStats(combination)
        victory: bool = fight(enemy_hp, enemy_damage, enemy_armor, player_damage, player_armor)

        if victory and cost < cost_victory_min:
            cost_victory_min = cost

        if not victory and cost > cost_loss_max:
            cost_loss_max = cost

    print(cost_victory_min)
    print(cost_loss_max)


def getOutfitCombinations() -> [[Item]]:
    all_combinations: [[Item]] = [[weapon, armor] for weapon in weapons for armor in armors]
    weapon: Item
    for weapon in weapons:
        all_combinations.append([weapon])

    ring_combinations: [[Item]] = [[x, y] for x, y in list(itertools.combinations(rings, 2))]
    ring: Item
    for ring in rings:
        ring_combinations.append([ring])

    all_combinations.extend([x + y for x in all_combinations for y in ring_combinations])

    return all_combinations


def getOutfitStats(outfit: [[Item]]) -> (int, int, int):
    damage: int = 0
    armor: int = 0
    cost: int = 0

    item: Item
    for item in outfit:
        damage += item.damage
        armor += item.armor
        cost += item.cost

    return damage, armor, cost


def fight(enemy_hp: int, enemy_damage: int, enemy_armor: int, player_damage: int, player_armor: int) -> bool:
    player_hp: int = 100

    while True:
        enemy_hp -= max(1, player_damage - enemy_armor)
        if enemy_hp <= 0:
            return True

        player_hp -= max(1, enemy_damage - player_armor)
        if player_hp <= 0:
            return False


main()
