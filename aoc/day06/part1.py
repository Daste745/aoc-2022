from collections import deque
from sys import stdin


def main() -> None:
    line = stdin.readline().strip()
    characters: deque[str] = deque(maxlen=4)

    for i, char in enumerate(line):
        if len(characters) == 4 and len(set(characters)) == 4:
            print("start-of-packet at", i, characters)
            break

        characters.append(char)


if __name__ == "__main__":
    main()
