from sys import stdin


def priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord("a") + 1
    elif item.isupper():
        return ord(item) - ord("A") + 27
    return 0


def main() -> None:
    priority_sum = 0

    for line in stdin.readlines():
        clean_line = line.strip()
        half = int(len(clean_line) / 2)
        comp1, comp2 = set(clean_line[:half]), set(clean_line[half:])
        common = comp1 & comp2

        for item in common:
            priority_sum += priority(item)

    print(priority_sum)


if __name__ == "__main__":
    main()
