from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from functools import cached_property
from sys import stdin
from typing import Iterator


@dataclass()
class Directory:
    name: str
    children: list[Directory | File]
    parent: Directory | None

    def __hash__(self) -> int:
        return sum(map(ord, self.name))

    @cached_property
    def total_size(self) -> int:
        total = 0

        for child in self.children:
            if isinstance(child, Directory):
                total += child.total_size
            if isinstance(child, File):
                total += child.size

        return total

    def walk_directories(self) -> Iterator[Directory]:
        visited: set[Directory] = set()
        to_walk: deque[Directory] = deque([self])

        while len(to_walk) > 0:
            current = to_walk.popleft()
            if current in visited:
                continue
            visited.add(current)

            yield current

            for child in current.children:
                if not isinstance(child, Directory):
                    continue
                to_walk.append(child)


@dataclass
class File:
    name: str
    size: int


def print_directory_structure(start: Directory, indent: int = 0) -> None:
    """
    Print the directory structure similar to the one shown on the day 7 Advent of Code task page

    Example output:
    ```text
    - / (dir, totsize=48381165)
      - a (dir, totsize=94853)
        - e (dir, totsize=584)
        - i (file, size=584)
        - f (file, size=29116)
        - g (file, size=2557)
        - h.lst (file, size=62596)
      - b.txt (file, size=14848514)
      - c.dat (file, size=8504156)
      - d (dir, totsize=24933642)
        - j (file, size=4060174)
        - d.log (file, size=8033020)
        - d.ext (file, size=5626152)
        - k (file, size=7214296)
    ```
    """

    prefix = "  " * indent + "- "
    print(f"{prefix}{start.name} (dir, totsize={start.total_size})")

    for node in start.children:
        match node:
            case Directory(name):
                print_directory_structure(node, indent + 1)
            case File(name, size):
                print(f"  {prefix}{name} (file, {size=})")


def main() -> None:
    root_directory = Directory("/", children=[], parent=None)
    current_location = root_directory

    for line in stdin.readlines():
        if not line.startswith("$"):
            # Output from ls
            size_or_dir, name = line.strip().split(" ")
            if size_or_dir == "dir":
                current_location.children.append(
                    Directory(
                        name,
                        children=[],
                        parent=current_location,
                    )
                )
            else:
                size = int(size_or_dir)
                current_location.children.append(File(name, size))

            continue

        command, *arguments = line.replace("$ ", "").strip().split(" ")
        if command == "cd":
            argument = arguments[0]
            if argument == "/":
                current_location = root_directory
            if argument == "..":
                if parent := current_location.parent:
                    current_location = parent
            else:
                for child in current_location.children:
                    if not isinstance(child, Directory):
                        continue
                    if child.name != argument:
                        continue
                    current_location = child

        elif command == "ls":
            continue

    print_directory_structure(root_directory)

    size_sum = 0
    for dir in root_directory.walk_directories():
        if dir.total_size > 100_000:
            continue
        size_sum += dir.total_size

    print(size_sum)


if __name__ == "__main__":
    main()
