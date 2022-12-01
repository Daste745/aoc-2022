from sys import stdin


from aoc.day01.common import *


def main() -> None:
    most_carried_calories = count_carried_calories(stdin.readlines())
    calorie_sum = 0
    for _, amount in most_carried_calories.most_common(3):
        calorie_sum += amount

    print(calorie_sum)


if __name__ == "__main__":
    main()
