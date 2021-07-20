"""Advent of Code 2019 Day 5"""

from shared.common import get_input
from shared.intcode_computer import IntCodeComputer

if __name__ == "__main__":
    PUZZLE = [int(x) for x in get_input("input5.txt").split(",")]
    SHIP_ID = 1
    computer = IntCodeComputer(PUZZLE.copy())
    computer.push(SHIP_ID)
    computer.run()
    print(
        f"Thermal Environment Supervision Terminal Diagnostics: {computer.output_results()}"
    )
    del computer

    # Part 2
    SHIP_ID = 5
    computer = IntCodeComputer(PUZZLE.copy())
    computer.push(SHIP_ID)
    computer.run()
    print(f"Thermal Radiator Controller Diagnostics: {computer.output_results()}")
