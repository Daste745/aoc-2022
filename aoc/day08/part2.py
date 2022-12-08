from enum import Enum, auto
from functools import reduce
from sys import stdin


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


def count_visible(grid: list[list[int]], y: int, x: int, direction: Direction) -> int:
    tree = grid[y][x]
    height = len(grid)
    width = len(grid[0])
    count = 0

    if direction == Direction.UP:
        for i in range(y - 1, -1, -1):
            count += 1
            if grid[i][x] >= tree:
                return count

    elif direction == Direction.DOWN:
        for i in range(y + 1, height):
            count += 1
            if grid[i][x] >= tree:
                return count

    elif direction == Direction.LEFT:
        for i in range(x - 1, -1, -1):
            count += 1
            if grid[y][i] >= tree:
                return count

    elif direction == Direction.RIGHT:
        for i in range(x + 1, width):
            count += 1
            if grid[y][i] >= tree:
                return count

    return count


def scenic_score(grid: list[list[int]], y: int, x: int) -> int:
    return reduce(
        lambda a, b: a * b,
        (count_visible(grid, y, x, direction) for direction in Direction),
    )


def main() -> None:
    grid = [[int(i) for i in line.strip()] for line in stdin.readlines()]

    max_scenic_score = max(
        scenic_score(grid, y, x)
        for x in range(1, len(grid[0]) - 1)
        for y in range(1, len(grid) - 1)
    )
    print(max_scenic_score)


if __name__ == "__main__":
    main()
