from __future__ import annotations

import dataclasses
from dataclasses import dataclass
from enum import Enum
from sys import stdin
from typing import Iterable


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
        return (self.y << 16) ^ self.x

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


def print_visited(visited: Iterable[Position]) -> None:
    min_height = min(visited, key=lambda pos: pos.y).y
    max_height = max(visited, key=lambda pos: pos.y).y
    min_width = min(visited, key=lambda pos: pos.x).x
    max_width = max(visited, key=lambda pos: pos.x).x

    for y in range(max_height, min_height - 1, -1):
        for x in range(min_width, max_width + 1):
            if y == 0 and x == 0:
                print("s", end="")
                continue

            for visit in visited:
                if visit.y == y and visit.x == x:
                    print("#", end="")
                    break
            else:
                print(".", end="")

        print()


def main() -> None:
    head = Position(0, 0)
    knots = [Position(0, 0) for _ in range(9)]
    visited: set[Position] = set([knots[-1]])

    for line in stdin.readlines():
        raw_direction, raw_amount = line.strip().split(" ")
        direction = Direction(raw_direction)
        amount = int(raw_amount)

        # print(f"Moving {direction} {amount} times")
        for step in range(amount):
            head.move(direction)
            previous = head
            # print(f"Step {step}")
            for i, knot in enumerate(knots, start=1):
                # print(
                #     f"({i}) {knot} is following {previous} ({knot.is_touching(previous)})"
                # )
                knot.follow(previous)
                # print(f"  -> {knot}")
                previous = knot

            # Save only the last knot's position
            visited.add(dataclasses.replace(knots[-1]))
        # print()

    # print(f"{head=} {knots[-1]=}")
    # print_board(head, tail)
    # print_visited(visited)
    # print([(pos.y, pos.x) for pos in visited])
    print(len(visited))


if __name__ == "__main__":
    main()
