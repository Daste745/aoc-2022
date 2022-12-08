from enum import Enum, auto
from sys import stdin


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


def is_visible(grid: list[list[int]], y: int, x: int, direction: Direction) -> bool:
    tree = grid[y][x]
    height = len(grid)
    width = len(grid[0])

    if direction == Direction.UP:
        for i in range(y - 1, -1, -1):
            # print(f"looking at {i=} {x=} {grid[i][x]=}")
            if grid[i][x] >= tree:
                return False

    elif direction == Direction.DOWN:
        for i in range(y + 1, height):
            if grid[i][x] >= tree:
                return False

    elif direction == Direction.LEFT:
        for i in range(x - 1, -1, -1):
            if grid[y][i] >= tree:
                return False

    elif direction == Direction.RIGHT:
        for i in range(x + 1, width):
            if grid[y][i] >= tree:
                return False

    return True


def main() -> None:
    grid = [[int(i) for i in line.strip()] for line in stdin.readlines()]
    # Count the border
    visible = len(grid) * 2 + (len(grid[0]) - 2) * 2

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if any(is_visible(grid, y, x, direction) for direction in Direction):
                visible += 1

    print(visible)


if __name__ == "__main__":
    main()
