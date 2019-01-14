"""Advent of Code 2018 Day 19"""
from shared.common import get_puzzle_input
from shared.device import Device
from shared.transforms import transform_program


def main():
    """Main Puzzle Entry."""
    puzzle = get_puzzle_input("input/input19.txt")
    program = transform_program(puzzle[1:])
    print("Part 1: What is left in register 0 after the program ends.")
    dev = Device(instruction_register=int(puzzle[0][3:]))
    dev.run_program_with_flow_control(program)
    print(dev)
    print("Part 2: Register 0 started with the value 1. What is left after the program?")
    dev2 = Device(registers=[1, 0, 0, 0, 0, 0], instruction_register=int(puzzle[0][3:]))
    dev2.run_program_with_flow_control(program)
    print(dev2)


if __name__ == "__main__":
    main()
