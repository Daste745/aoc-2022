from collections import deque
from sys import stdin


def main() -> None:
    line = stdin.readline().strip()
    characters: deque[str] = deque(maxlen=14)

    for i, char in enumerate(line):
        if len(characters) == 14 and len(set(characters)) == 14:
            print("start-of-message at", i, characters)
            break

        characters.append(char)


if __name__ == "__main__":
    main()
