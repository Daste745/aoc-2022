from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from functools import cached_property
from sys import stdin
from typing import Iterator

DISK_SIZE = 70_000_000
UNUSED_TARGET = 30_000_000


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

    to_delete = root_directory
    free_space = DISK_SIZE - root_directory.total_size
    for dir in root_directory.walk_directories():
        if (
            free_space + dir.total_size >= UNUSED_TARGET
        ) and dir.total_size < to_delete.total_size:
            to_delete = dir

    print(to_delete.name, to_delete.total_size)


if __name__ == "__main__":
    main()
