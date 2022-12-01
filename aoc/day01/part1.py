from sys import stdin

from aoc.day01.common import *


def main() -> None:
    most_carried_calories = count_carried_calories(stdin.readlines())
    _, amount = most_carried_calories.most_common(1)[0]
    print(amount)


if __name__ == "__main__":
    main()
