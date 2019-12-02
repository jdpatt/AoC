"""Advent of Code 2019 Day 2"""
import operator
from shared.common import get_and_transform_input

OPCODES = {1: operator.add, 2: operator.mul, 99: None}  # Halt
STEP = 4


class IntCodeComputer:
    def __init__(self, memory, pointer=0, input1=12, input2=2):
        self.memory = memory
        self.pointer = pointer
        self.update_value(1, input1)
        self.update_value(2, input2)

    def get_value(self, position):
        """Return the value stored at this address."""
        return self.memory[position]

    def update_value(self, position, value):
        """Set the value at this address."""
        self.memory[position] = value

    def run_opcode(self, pointer: int):
        """Run the individual command updating the results in the memory."""
        input1 = self.get_value(self.memory[pointer + 1])
        input2 = self.get_value(self.memory[pointer + 2])
        output = self.memory[pointer + 3]
        self.memory[output] = OPCODES[self.memory[pointer]](input1, input2,)

    def run_program(self):
        """Run the intCode Program until completion."""
        while self.memory[self.pointer] != 99:
            self.run_opcode(self.pointer)
            self.pointer += STEP
        return self.results()

    def results(self):
        """Return the results after executing the program."""
        return self.memory[0]


if __name__ == "__main__":
    PROGRAM = [int(x) for x in get_and_transform_input("input2.txt")[0].split(",")]
    MEMORY = {index: item for index, item in enumerate(PROGRAM)}
    COMPUTER = IntCodeComputer(memory=MEMORY.copy())
    print(f"Part 1 after completion: {COMPUTER.run_program()}")

    print("Part 2")
    for noun in range(100):
        for verb in range(100):
            COMPUTER = IntCodeComputer(memory=MEMORY.copy(), input1=noun, input2=verb)
            if COMPUTER.run_program() == 19690720:
                print(f"Noun: {noun} Verb: {verb}")
                print(f"Part 2 Results {100 * noun + verb}")
                break
