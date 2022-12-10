from __future__ import annotations

from sys import stdin


class CPU:
    _cycle: int
    _x: int
    _x_at_cycles: list[int]

    def __init__(self, start_value: int = 1) -> None:
        self._cycle = 0
        self._x = start_value
        self._x_at_cycles = [self._x]

    @property
    def x(self) -> int:
        return self._x

    @property
    def cycle(self) -> int:
        return self._cycle

    def noop(self) -> None:
        self._advance_cycle()

    def addx(self, amount: int) -> None:
        self._advance_cycle()
        self._x += amount
        self._advance_cycle()

    def _advance_cycle(self) -> None:
        self._cycle += 1
        self._x_at_cycles.append(self._x)

    def value_at_cycle(self, cycle: int) -> int:
        return self._x_at_cycles[cycle]


def main() -> None:
    cpu = CPU()

    for line in stdin.readlines():
        operation, *operands = line.strip().split()
        if operation == "noop":
            cpu.noop()
        elif operation == "addx":
            amount = int(operands[0])
            cpu.addx(amount)

    total = 0
    for i in range(20, cpu.cycle, 40):
        # i-1 because we use 0-indexed cycles
        value = cpu.value_at_cycle(i - 1)
        total += i * value
        print(i, value, i * value)
    print(total)


if __name__ == "__main__":
    main()
