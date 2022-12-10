from __future__ import annotations

from sys import stdin


class CPU:
    _screen: Screen
    _cycle: int
    _x: int
    _x_at_cycles: list[int]

    def __init__(self, start_value: int = 1) -> None:
        self._screen = Screen(columns=40, rows=6)
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
        self._screen.draw(self.cycle, self.x)
        self._advance_cycle()

    def addx(self, amount: int) -> None:
        self._screen.draw(self.cycle, self.x)
        self._advance_cycle()
        self._screen.draw(self.cycle, self.x)
        self._x += amount
        self._advance_cycle()

    def _advance_cycle(self) -> None:
        self._cycle += 1
        self._x_at_cycles.append(self._x)

    def value_at_cycle(self, cycle: int) -> int:
        return self._x_at_cycles[cycle]


class Screen:
    _columns: int
    _rows: int

    def __init__(self, columns: int, rows: int) -> None:
        self._columns = columns
        self._rows = rows

    def draw(self, cycle: int, sprite_pos: int) -> None:
        pos_in_row = (cycle + 1) % self._columns - 1

        if abs(sprite_pos - pos_in_row) <= 1:
            print("#", end="")
        else:
            print(".", end="")

        if (cycle + 1) % self._columns == 0:
            print()


def main() -> None:
    cpu = CPU()

    for line in stdin.readlines():
        operation, *operands = line.strip().split()
        if operation == "noop":
            cpu.noop()
        elif operation == "addx":
            amount = int(operands[0])
            cpu.addx(amount)


if __name__ == "__main__":
    main()
