from typing import TextIO


class Ingredient:

    def __init__(self, capacity: int, durability: int, flavour: int, texture: int, calories: int) -> None:
        self.capacity = capacity
        self.durability = durability
        self.flavour = flavour
        self.texture = texture
        self.calories = calories

    def getTotalCapacity(self, amount: int) -> int:
        return self.capacity * amount

    def getTotalDurability(self, amount: int) -> int:
        return self.durability * amount

    def getTotalFlavour(self, amount: int) -> int:
        return self.flavour * amount

    def getTotalTexture(self, amount: int) -> int:
        return self.texture * amount

    def getTotalCalories(self, amount: int) -> int:
        return self.calories * amount


def main() -> None:
    teaspoons: int = 100
    calories: int = 500
    ingredients: [Ingredient] = []

    file: TextIO
    with open("input.txt", "r") as file:
        line: str
        for line in file:
            split: [str] = line.split(' ')
            ingredients.append(Ingredient(int(split[2][:-1]), int(split[4][:-1]),
                                          int(split[6][:-1]), int(split[8][:-1]), int(split[10])))

    ingredient_permutations: [[int]] = generatePermutations(teaspoons, len(ingredients),
                                                            0, [], [])

    best_score: int
    best_score_with_calories: int
    best_score, best_score_with_calories = calculateScore(ingredient_permutations, ingredients, calories)
    print("without calories: {}, with calories: {}".format(best_score, best_score_with_calories))


def calculateScore(ingredient_permutations: [[int]], ingredients: [Ingredient], calories: int) -> (int, int):
    best_score: int = 0
    best_score_with_calories = 0

    for recipe in ingredient_permutations:
        total_capacity: int = 0
        total_durability: int = 0
        total_flavour: int = 0
        total_texture: int = 0
        total_calories: int = 0
        amount: int
        index: int

        for index, amount in enumerate(recipe):
            total_capacity += ingredients[index].getTotalCapacity(amount)
            total_durability += ingredients[index].getTotalDurability(amount)
            total_flavour += ingredients[index].getTotalFlavour(amount)
            total_texture += ingredients[index].getTotalTexture(amount)
            total_calories += ingredients[index].getTotalCalories(amount)

        totalScore: int = (max(0, total_capacity) * max(0, total_durability) *
                           max(0, total_flavour) * max(0, total_texture))
        if totalScore > best_score:
            best_score = totalScore
        if total_calories == calories and totalScore > best_score_with_calories:
            best_score_with_calories = totalScore

    return best_score, best_score_with_calories


def generatePermutations(teaspoons_left: int, ingredients_length: int, current_ingredient: int,
                         recipe: [int], permutations: [[int]]) -> [[int]]:
    if current_ingredient >= ingredients_length:
        if teaspoons_left == 0:
            permutations.append(recipe)
            return permutations
        else:
            return permutations

    for amount in range(0, teaspoons_left + 1):
        new_recipe: [int] = list(recipe)
        new_recipe.append(amount)
        generatePermutations(teaspoons_left - amount, ingredients_length, current_ingredient + 1, new_recipe,
                             permutations)

    return permutations


if __name__ == "__main__":
    main()
