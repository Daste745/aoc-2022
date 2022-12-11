from __future__ import annotations

import math
from collections import Counter
from dataclasses import dataclass
from functools import reduce
from itertools import islice
from operator import mul
from sys import stdin
from typing import Iterator


def chunk_by(iterator: Iterator, n: int) -> Iterator[list]:
    while chunk := list(islice(iterator, n)):
        yield chunk


@dataclass
class Monkey:
    items: list
    operator: str
    operand: str
    test: int
    test_true: int
    test_false: int
    inspections: int = 0

    def turn(self, monkeys: list[Monkey], test_lcm: int) -> None:
        for i in range(len(self.items)):
            operand = self.items[i] if self.operand == "old" else int(self.operand)
            if self.operator == "+":
                self.items[i] += operand
            elif self.operator == "*":
                self.items[i] *= operand

            self.items[i] %= test_lcm

            if self.items[i] % self.test == 0:
                target = monkeys[self.test_true]
            else:
                target = monkeys[self.test_false]

            target.items.append(self.items[i])
            self.inspections += 1

        self.items.clear()


def main() -> None:
    lines = iter(stdin.readlines())
    monkeys: list[Monkey] = []

    for data in chunk_by(lines, 7):
        starting_items = map(int, data[1].split(":")[1].strip().split(", "))
        operation = data[2].replace("Operation: new = old", "").strip()
        operator, operand = operation.split(" ")
        test_divisible_by = int(data[3].replace("Test: divisible by", "").strip())
        test_true = int(data[4].replace("If true: throw to monkey", "").strip())
        test_false = int(data[5].replace("If false: throw to monkey", "").strip())

        monkeys.append(
            Monkey(
                items=list(starting_items),
                operator=operator,
                operand=operand,
                test=test_divisible_by,
                test_true=test_true,
                test_false=test_false,
            )
        )

    test_lcm = math.lcm(*[monkey.test for monkey in monkeys])
    for _ in range(10000):
        for monkey in monkeys:
            monkey.turn(monkeys, test_lcm)

    top_inspections = Counter(
        {i: monkey.inspections for i, monkey in enumerate(monkeys)}
    )
    print(top_inspections)
    print(reduce(mul, map(lambda pair: pair[1], top_inspections.most_common(2))))


if __name__ == "__main__":
    main()
