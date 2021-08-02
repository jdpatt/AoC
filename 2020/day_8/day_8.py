"""Day 8"""
import copy
from os import read
from pathlib import Path
from typing import Tuple


class BootCodeError(Exception):
    ...


def read_in_boot_code():
    """Each line consists of an operation and an argument."""
    with open(Path(__file__).parent.joinpath("input.txt")) as puzzle_input:
        instructions = list()
        for line in puzzle_input:
            operation, argument = line.split(" ")
            instructions.append(
                {"operation": operation, "argument": argument, "executed": False}
            )
        return instructions


def has_executed(instruction) -> bool:
    return instruction["executed"]


def run_program(instructions) -> Tuple[int, int]:
    accumulator = 0
    instruction_pointer = 0

    while True:
        try:
            instruction = instructions[instruction_pointer]
            if has_executed(instruction):
                return -1, accumulator
            if instruction["operation"] == "jmp":
                instruction_pointer += int(instruction["argument"])
            elif instruction["operation"] == "acc":
                accumulator += int(instruction["argument"])
                instruction_pointer += 1
            elif instruction["operation"] == "nop":
                instruction_pointer += 1
            else:
                raise BootCodeError("Unhandled Operation")
            instruction["executed"] = True
        except IndexError:
            print(f"Program Completed...\t{accumulator=}")  # 2060
            return 0, accumulator


if __name__ == "__main__":
    boot_code = read_in_boot_code()
    return_code, accumulator = run_program(copy.deepcopy(boot_code))
    print(f"Value prior to repeating instructions: {accumulator}")  # 1801
    for index, instruction in enumerate(boot_code):
        if instruction["operation"] == "acc":
            continue  # Skip running this loop.
        modified_boot_code = copy.deepcopy(boot_code)
        if instruction["operation"] == "jmp":
            modified_boot_code[index]["operation"] = "nop"
        elif instruction["operation"] == "nop":
            modified_boot_code[index]["operation"] = "jmp"
        print(f"Running program...{index}")
        return_code, accumulator = run_program(modified_boot_code)
        if return_code == 0:
            break
