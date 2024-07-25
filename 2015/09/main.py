import sys
import operator
from typing import TextIO

cities: {str: {str: int}} = {}


def main() -> None:
    read_cities()

    best_path: str
    best_dist: int

    best_path, best_dist = get_route(operator.lt)
    print(best_path + str(best_dist))
    best_path, best_dist = get_route(operator.gt)
    print(best_path + str(best_dist))


def read_cities() -> None:
    file: TextIO
    with open("input.txt", "r") as file:
        line: str
        for line in file:
            str_split: [str] = line.split(' ')
            if str_split[2] not in cities:
                cities[str_split[2]] = {str_split[0]: int(str_split[4])}
            else:
                cities[str_split[2]][str_split[0]] = int(str_split[4])
            if str_split[0] not in cities:
                cities[str_split[0]] = {str_split[2]: int(str_split[4])}
            else:
                cities[str_split[0]][str_split[2]] = int(str_split[4])


def get_route(op: operator) -> tuple[str, int]:
    best_route: str = ""
    city: str
    best_distance: int = sys.maxsize if op == operator.lt else 0

    for city in cities.keys():
        route: str
        distance: int

        route, distance = calculate_route(city, set(), "", op)
        if op(distance, best_distance):
            best_route = route
            best_distance = distance

    return best_route, best_distance


def calculate_route(name: str, visited: set[str], path: str, op: operator) -> tuple[str, int]:
    connected_city_name: str
    distance: int
    min_path: str = ""
    last_city: bool = True
    path += "{} ".format(name)
    visited.add(name)
    min_distance: int = sys.maxsize if op == operator.lt else 0

    for connected_city_name, distance in cities[name].items():
        if connected_city_name in visited:
            continue
        last_city = False
        path: str
        recursion_distance: int

        path, recursion_distance = calculate_route(connected_city_name, visited.copy(), path, op)
        if op(distance + recursion_distance, min_distance):
            min_distance = distance + recursion_distance
            min_path = path
            path = "{} ".format(name)

    if last_city:
        return path, 0
    else:
        return min_path, min_distance


main()
