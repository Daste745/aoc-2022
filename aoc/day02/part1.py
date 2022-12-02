from sys import stdin

SCORING: dict[str, int] = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
BEATS: dict[str, str] = {
    "X": "C",
    "Y": "A",
    "Z": "B",
}
DRAWS: dict[str, str] = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}


def main() -> None:
    score = 0

    for line in stdin.readlines():
        player_1, player_2 = line.split()

        score += SCORING[player_2]

        if BEATS[player_2] == player_1:
            score += 6
        elif DRAWS[player_2] == player_1:
            score += 3

    print(score)


if __name__ == "__main__":
    main()
