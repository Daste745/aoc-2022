from functools import reduce
from itertools import islice
from sys import stdin
from typing import Iterator


def chunk_by(iterator: Iterator, n: int) -> Iterator[list]:
    while chunk := list(islice(iterator, n)):
        yield chunk


def priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord("a") + 1
    elif item.isupper():
        return ord(item) - ord("A") + 27
    return 0


def main() -> None:
    priority_sum = 0

    for group in chunk_by(iter(stdin.readlines()), 3):
        common: set[str] = reduce(
            lambda prev, current: prev & current,
            [set(item.strip()) for item in group],
        )
        for item in common:
            priority_sum += priority(item)

    print(priority_sum)


if __name__ == "__main__":
    main()
