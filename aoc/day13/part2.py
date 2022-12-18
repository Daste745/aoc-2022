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
                # print(f"{s}a ran out")
                return True, True
            elif i >= len(b):
                # print(f"{s}b ran out")
                return False, True

            elem_a = a[i]
            elem_b = b[i]
            # print(f"{s}compare {elem_a} vs {elem_b}")

            if isinstance(elem_a, int) and isinstance(elem_b, list):
                # print(f"{s}{elem_a=} is int, converting to [{elem_a}]")
                elem_a = [elem_a]
            elif isinstance(elem_a, list) and isinstance(elem_b, int):
                # print(f"{s}{elem_b=} is int, converting to [{elem_b}]")
                elem_b = [elem_b]

            if isinstance(elem_a, int) and isinstance(elem_b, int):
                if elem_a < elem_b:
                    # print(f"{s}left smaller")
                    return True, True
                elif elem_a > elem_b:
                    # print(f"{s}right smaller")
                    return False, True

            elif isinstance(elem_a, list) and isinstance(elem_b, list):
                # print(f"{s}recursing with {elem_a} {elem_b}")
                valid, decision = check(elem_a, elem_b, depth + 1)
                if decision:
                    return valid, True

            i += 1

    valid, _ = check(packet_a, packet_b)
    return valid


def main() -> None:
    lines = iter(stdin.readlines())
    packets: list[RecList[int]] = [[[2]], [[6]]]
    result = 1

    for line in lines:
        if line.strip() == "":
            continue
        packets.append(parse_packet(line.strip()))

    for i in range(len(packets)):
        for j in range(len(packets) - 1):
            if is_packet_pair_valid(packets[i], packets[j]):
                packets[i], packets[j] = packets[j], packets[i]

    for i, packet in enumerate(packets, start=1):
        if packet == [[2]] or packet == [[6]]:
            result *= i

    print(result)


if __name__ == "__main__":
    main()
