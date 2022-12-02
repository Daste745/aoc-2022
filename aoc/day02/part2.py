from sys import stdin

SCORING: dict[str, int] = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
BEATS: dict[str, str] = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}
DRAWS: dict[str, str] = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}
LOSES: dict[str, str] = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}


def main() -> None:
    score = 0

    for line in stdin.readlines():
        player_1, move = line.split()

        if move == "X":
            score += SCORING[LOSES[player_1]]
        elif move == "Y":
            score += SCORING[DRAWS[player_1]]
            score += 3
        elif move == "Z":
            score += SCORING[BEATS[player_1]]
            score += 6

    print(score)


if __name__ == "__main__":
    main()
