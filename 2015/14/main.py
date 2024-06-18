from typing import TextIO


class Reindeer:

    def __init__(self, name: str, speed: int, flight_time: int, rest_time: int) -> None:
        self.is_flying = True
        self.speed = speed
        self.flight_time = flight_time
        self.flight_time_left = flight_time
        self.rest_time = rest_time
        self.rest_time_left = rest_time
        self.distance_traveled = 0
        self.points = 0

    def fly(self) -> None:
        if self.is_flying:
            self.distance_traveled += self.speed
            self.flight_time_left -= 1

            if self.flight_time_left == 0:
                self.is_flying = False
                self.flight_time_left = self.flight_time

        else:
            self.rest_time_left -= 1

            if self.rest_time_left == 0:
                self.is_flying = True
                self.rest_time_left = self.rest_time


def main() -> None:
    reindeer: set[Reindeer] = set()
    seconds: int = 2503
    file: TextIO

    with open("input.txt", "r") as file:
        line: str
        for line in file:
            line_split: [str] = line.split(' ')
            reindeer.add(Reindeer(line_split[0], int(line_split[3]), int(line_split[6]),
                                  int(line_split[-2])))

    second: int
    rd: Reindeer
    for second in range(seconds):
        for rd in reindeer:
            rd.fly()
        award_reindeer: [Reindeer] = [ x for x in reindeer if x == max(reindeer, key=lambda y: y.distance_traveled)]
        for rd in award_reindeer:
            rd.points += 1

    maximum_distance_reindeer: Reindeer = max(reindeer, key=lambda x: x.distance_traveled)
    print("maximum distance: {}".format(str(maximum_distance_reindeer.distance_traveled)))
    maximum_points_reindeer: Reindeer = max(reindeer, key=lambda x: x.points)
    print("maximum points: {}".format(str(maximum_points_reindeer.points)))


if __name__ == "__main__":
    main()
