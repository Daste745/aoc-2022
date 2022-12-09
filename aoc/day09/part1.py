from __future__ import annotations

import dataclasses
from dataclasses import dataclass
from enum import Enum
from sys import stdin


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


@dataclass
class Position:
    y: int
    x: int

    def __hash__(self) -> int:
        return self.y | (self.x << 15)

    def is_touching(self, other: Position) -> bool:
        if abs(self.y - other.y) > 1:
            return False
        if abs(self.x - other.x) > 1:
            return False
        return True

    def move(self, direction: Direction) -> None:
        if direction == Direction.UP:
            self.y += 1
        elif direction == Direction.DOWN:
            self.y -= 1
        elif direction == Direction.LEFT:
            self.x -= 1
        elif direction == Direction.RIGHT:
            self.x += 1

    def follow(self, other: Position) -> None:
        if self.is_touching(other):
            return

        if self.y < other.y:
            self.y += 1
        elif self.y > other.y:
            self.y -= 1

        if self.x < other.x:
            self.x += 1
        elif self.x > other.x:
            self.x -= 1


def print_board(head: Position, tail: Position, size: int = 6) -> None:
    for y in range(size, -1, -1):
        for x in range(size):
            if head.y == y and head.x == x:
                print("H", end=" ")
            elif tail.y == y and tail.x == x:
                print("T", end=" ")
            elif y == 0 and x == 0:
                print("s", end=" ")
            else:
                print(".", end=" ")
        print()


def main() -> None:
    head = Position(0, 0)
    tail = Position(0, 0)
    visited: set[Position] = set([tail])

    for line in stdin.readlines():
        raw_direction, raw_amount = line.strip().split(" ")
        direction = Direction(raw_direction)
        amount = int(raw_amount)

        for _ in range(amount):
            head.move(direction)
            tail.follow(head)

            visited.add(dataclasses.replace(tail))

    print(f"{head=} {tail=}")
    # print_board(head, tail)
    print(len(visited))


if __name__ == "__main__":
    main()
