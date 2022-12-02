from collections import Counter
from sys import stdin


def count_carried_calories(lines: list[str]) -> Counter[int]:
    carried_calories: Counter[int] = Counter()
    elf_index = 1

    for line in lines:
        if line.strip() == "":
            elf_index += 1
            continue

        carried_calories[elf_index] += int(line.strip())

    return carried_calories


def main() -> None:
    most_carried_calories = count_carried_calories(stdin.readlines())
    calorie_sum = 0
    for _, amount in most_carried_calories.most_common(3):
        calorie_sum += amount

    print(calorie_sum)


if __name__ == "__main__":
    main()
