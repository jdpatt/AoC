"""Advent of Code 2019 Day 2"""
from shared.common import get_and_transform_input
from shared.intcode_computer import IntCodeComputer


if __name__ == "__main__":
    PROGRAM = [int(x) for x in get_and_transform_input("input2.txt")[0].split(",")]
    MEMORY = {index: item for index, item in enumerate(PROGRAM)}
    COMPUTER = IntCodeComputer(memory=MEMORY.copy())
    COMPUTER.store(1, 12)
    COMPUTER.store(2, 2)
    print(f"Part 1 after completion: {COMPUTER.run()}")

    print("Part 2")
    for noun in range(100):
        for verb in range(100):
            COMPUTER = IntCodeComputer(memory=MEMORY.copy())
            COMPUTER.store(1, noun)
            COMPUTER.store(2, verb)
            if COMPUTER.run() == 19690720:
                print(f"Noun: {noun} Verb: {verb}")
                print(f"Part 2 Results {100 * noun + verb}")
                break
