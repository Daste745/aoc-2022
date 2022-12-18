import json
from itertools import islice
from sys import stdin
from typing import Iterator, TypeVar, cast

T = TypeVar("T")
RecList = list[T | "RecList[T]"]


def chunk_by(iterator: Iterator[T], n: int) -> Iterator[list[T]]:
    while chunk := list(islice(iterator, n)):
        yield chunk


def parse_packet(input: str) -> RecList[int]:
    return cast(RecList[int], json.loads(input))


def is_packet_pair_valid(packet_a: RecList[int], packet_b: RecList[int]) -> bool:
    def check(a: RecList[int], b: RecList[int], depth: int = 0) -> tuple[bool, bool]:
        s = "  " * depth
        i = 0
        while True:
            if i >= len(a) and i >= len(b):
                return False, False
            elif i >= len(a):
                print(f"{s}a ran out")
                return True, True
            elif i >= len(b):
                print(f"{s}b ran out")
                return False, True

            elem_a = a[i]
            elem_b = b[i]
            print(f"{s}compare {elem_a} vs {elem_b}")

            if isinstance(elem_a, int) and isinstance(elem_b, list):
                print(f"{s}{elem_a=} is int, converting to [{elem_a}]")
                elem_a = [elem_a]
            elif isinstance(elem_a, list) and isinstance(elem_b, int):
                print(f"{s}{elem_b=} is int, converting to [{elem_b}]")
                elem_b = [elem_b]

            if isinstance(elem_a, int) and isinstance(elem_b, int):
                if elem_a < elem_b:
                    print(f"{s}left smaller")
                    return True, True
                elif elem_a > elem_b:
                    print(f"{s}right smaller")
                    return False, True

            elif isinstance(elem_a, list) and isinstance(elem_b, list):
                print(f"{s}recursing with {elem_a} {elem_b}")
                valid, decision = check(elem_a, elem_b, depth + 1)
                if decision:
                    return valid, True

            i += 1

    valid, _ = check(packet_a, packet_b)
    return valid


def main() -> None:
    lines = iter(stdin.readlines())
    index_sum = 0

    for i, chunk in enumerate(chunk_by(lines, 3), start=1):
        packet_1 = parse_packet(chunk[0].strip())
        packet_2 = parse_packet(chunk[1].strip())

        print(f"== pair {i}")
        print(f"compare {packet_1} vs {packet_2}")
        print(is_packet_pair_valid(packet_1, packet_2))
        print()

        if is_packet_pair_valid(packet_1, packet_2):
            index_sum += i

    print(index_sum)


if __name__ == "__main__":
    main()
