from sys import stdin


def range_from_str(range_str: str) -> range:
    start, stop = map(int, range_str.split("-"))
    return range(start, stop + 1)


def main() -> None:
    overlaps = 0

    for line in stdin.readlines():
        pairs = line.strip().split(",")
        ranges = map(set, map(range_from_str, pairs))
        range_1, range_2 = ranges

        if (range_1 - range_2) == set() or (range_2 - range_1) == set():
            overlaps += 1

    print(overlaps)


if __name__ == "__main__":
    main()
