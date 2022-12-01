from collections import Counter


def count_carried_calories(lines: list[str]) -> Counter[int]:
    carried_calories: Counter[int] = Counter()
    elf_index = 1

    for line in lines:
        if line.strip() == "":
            elf_index += 1
            continue

        carried_calories[elf_index] += int(line.strip())

    return carried_calories
