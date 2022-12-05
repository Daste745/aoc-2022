from collections import defaultdict
from sys import stdin


def main() -> None:
    stacks: defaultdict[int, list] = defaultdict(list)
    lines = iter(stdin.readlines())

    # Initial stacks
    for line in lines:
        if line == "\n":
            break
        # Assume they are sorted
        if line.strip().startswith("1"):
            continue

        stack_data = (
            line.replace("    ", "[.]")
            .strip()
            .replace(" ", "")
            .replace("[", "")
            .replace("]", "")
        )
        for i, container in enumerate(stack_data):
            if container == ".":
                continue
            stacks[i].append(container)

    for i in stacks.keys():
        stacks[i].reverse()

    # Moves
    for line in lines:
        clean_line = (
            line.strip().replace("move ", "").replace(" from", "").replace(" to", "")
        )
        amount, from_stack, to_stack = map(int, clean_line.split(" "))
        from_stack -= 1
        to_stack -= 1

        to_move = [stacks[from_stack].pop() for _ in range(amount)]
        to_move.reverse()
        stacks[to_stack] += to_move

    output: list[str] = []
    for i in sorted(stacks.keys()):
        if len(stacks[i]) == 0:
            output += " "
        else:
            output += stacks[i][-1]
    print("".join(output))


if __name__ == "__main__":
    main()
