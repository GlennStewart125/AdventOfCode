from functools import reduce


def main() -> None:
    with open("input.txt", "r") as file:
        total_area: int = 0
        total_ribbon: int = 0
        lines: [str] = file.readlines()

        for present in lines:
            dimensions = [int(x) for x in present.split('x')]
            side1: int = dimensions[0] * dimensions[1]
            side2: int = dimensions[1] * dimensions[2]
            side3: int = dimensions[2] * dimensions[0]
            smallest_side: int = min(side1, side2, side3)
            present_area: int = 2 * side1 + 2 * side2 + 2 * side3 + smallest_side
            total_area += present_area

            dimensions.sort()
            present_ribbon: int = 2 * dimensions[0] + 2 * dimensions[1] + reduce(lambda x, y: x * y, dimensions)
            total_ribbon += present_ribbon

        print("area: {}".format(total_area))
        print("ribbon: {}".format(total_ribbon))


if __name__ == "__main__":
    main()
