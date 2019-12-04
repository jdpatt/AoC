"""Advent of Code 2018 Day 16"""
from copy import copy
from itertools import cycle

from shared.common import get_puzzle_input
from shared.device import Device
from shared.transforms import (
    transform_register_string,
    transform_program,
    transform_operation,
)


def find_ops_that_match_xplus(samples, matches):
    """Run the puzzle input and return ones who have `matches` or more matches."""
    results = [opcodes_test(Device(), x[0], x[1], x[2]) for x in samples]
    return [x for x in results if len(x) >= matches]


def get_sample_operations(file):
    """Read the puzzle input file and transform every four lines into one sample."""
    samples = []
    with open(file) as puzzle:
        while True:
            try:
                before = transform_register_string(puzzle.readline())
                operation = transform_operation(puzzle.readline())
                after = transform_register_string(puzzle.readline())
                puzzle.readline()
                samples.append([before, operation, after])
            except ValueError:
                break
    return samples


def opcodes_test(dev, registers, operation, results):
    """Test every opcode against the before, operation and results. Return the number of passing
    instructions.
    """
    passes = []
    for name, instruction in dev.opcode_names.items():
        dev.registers = copy(registers)
        instruction(operation[1], operation[2], operation[3])
        if dev.registers == results:
            passes.append(name)
    return passes


def solve_opcodes(samples):
    """Run through the sample input again and match opcodes with operations.

    If a operation only has one match we can assign it to an opcode and remove it from the
    selection of other samples.
    """
    unknown = [x for x in range(16)]
    known = []
    dev = Device()
    test_cases = cycle(samples)
    while unknown:
        case = next(test_cases)
        results = opcodes_test(dev, case[0], case[1], case[2])
        for element in known:
            if element in results:
                results.remove(element)
        if len(results) == 1:
            dev.opcodes[case[1][0]] = dev.opcode_names[results[0]]
            known.append(results[0])
            if case[1][0] in unknown:
                unknown.remove(case[1][0])
    return dev


def main():
    """Main Puzzle Entry."""
    puzzle = get_puzzle_input("input/input16.txt")
    samples = get_sample_operations("input/input16.txt")
    print("Part 1: How many samples behave like 3 or more opcodes?")
    print(len(find_ops_that_match_xplus(samples, 3)))

    print("Part 2: Find the opcode numbers, run the program and return register 0.")
    dev = solve_opcodes(samples)
    dev.run_program(transform_program(puzzle[3005:]))
    print(dev)


if __name__ == "__main__":
    main()


def test_opcode_test():
    """Test the example case."""
    assert opcodes_test(Device(), [3, 2, 1, 1], [9, 2, 1, 2], [3, 2, 2, 1]) == [
        "addi",
        "mulr",
        "seti",
    ]


def test_run_program():
    """Verify that a program runs correctly on the device."""
    dev = Device()
    dev.registers = [3, 2, 1, 1]
    dev.opcodes = {9: dev.addi}
    dev.run_program([[9, 2, 1, 2]])
    assert dev.registers == [3, 2, 2, 1]
