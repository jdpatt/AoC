"""Advent of Code 2018 Day 16"""
from copy import copy
from re import search


class Device:
    """Object representing the Device."""

    def __init__(self):
        super(Device, self).__init__()
        self.registers = [0, 0, 0, 0]

    def addr(self, reg_a, reg_b, reg_c):
        """stores into reg C the result of adding reg A and reg B"""
        self.registers[reg_c] = self.registers[reg_a] + self.registers[reg_b]

    def addi(self, reg_a, val_b, reg_c):
        """stores into reg C the result of adding reg A and value B"""
        self.registers[reg_c] = self.registers[reg_a] + val_b

    def mulr(self, reg_a, reg_b, reg_c):
        """stores into reg C the result of multiplying reg A and reg B"""
        self.registers[reg_c] = self.registers[reg_a] * self.registers[reg_b]

    def muli(self, reg_a, val_b, reg_c):
        """stores into reg C the result of multiplying reg A and value B"""
        self.registers[reg_c] = self.registers[reg_a] * val_b

    def banr(self, reg_a, reg_b, reg_c):
        """stores into reg C the result of bitwise AND of reg A and reg B"""
        self.registers[reg_c] = self.registers[reg_a] & self.registers[reg_b]

    def bani(self, reg_a, val_b, reg_c):
        """stores into reg C the result of bitwise AND of reg A and value B"""
        self.registers[reg_c] = self.registers[reg_a] & val_b

    def borr(self, reg_a, reg_b, reg_c):
        """stores into reg C the result of bitwise OR of reg A and reg B"""
        self.registers[reg_c] = self.registers[reg_a] | self.registers[reg_b]

    def bori(self, reg_a, val_b, reg_c):
        """stores into reg C the result of bitwise OR of reg A and value B"""
        self.registers[reg_c] = self.registers[reg_a] | val_b

    def setr(self, reg_a, _, reg_c):
        """copies the contents of reg A into reg C. B is ignored."""
        self.registers[reg_c] = self.registers[reg_a]

    def seti(self, val_a, _, reg_c):
        """copies the contents of reg A into reg C. B is ignored."""
        self.registers[reg_c] = val_a

    def gtir(self, val_a, reg_b, reg_c):
        """Sets reg C to 1 if value A is > than reg B. Otherwise, reg C is set to 0."""
        if val_a > self.registers[reg_b]:
            self.registers[reg_c] = 1
        else:
            self.registers[reg_c] = 0

    def gtri(self, reg_a, val_b, reg_c):
        """Sets reg C to 1 if reg A is > than value B. Otherwise, reg C is set to 0."""
        if self.registers[reg_a] > val_b:
            self.registers[reg_c] = 1
        else:
            self.registers[reg_c] = 0

    def gtrr(self, reg_a, reg_b, reg_c):
        """Sets reg C to 1 if reg A is > than reg B. Otherwise, reg C is set to 0."""
        if self.registers[reg_a] > self.registers[reg_b]:
            self.registers[reg_c] = 1
        else:
            self.registers[reg_c] = 0

    def eqir(self, val_a, reg_b, reg_c):
        """Sets reg C to 1 if value A is = to reg B. Otherwise, reg C is set to 0."""
        if val_a == self.registers[reg_b]:
            self.registers[reg_c] = 1
        else:
            self.registers[reg_c] = 0

    def eqri(self, reg_a, val_b, reg_c):
        """Sets reg C to 1 if reg A is = to value B. Otherwise, reg C is set to 0."""
        if self.registers[reg_a] == val_b:
            self.registers[reg_c] = 1
        else:
            self.registers[reg_c] = 0

    def eqrr(self, reg_a, reg_b, reg_c):
        """Sets reg C to 1 if reg A is = to reg B. Otherwise, reg C is set to 0."""
        if self.registers[reg_a] == self.registers[reg_b]:
            self.registers[reg_c] = 1
        else:
            self.registers[reg_c] = 0

    def __str__(self):
        print(f"Registers: {self.registers}")


def opcodes_test(registers, operation, results):
    """Test every opcode against the before, operation and results. Return the number of passing
    instructions.
    """
    dev = Device()
    passes = 0
    opcodes = {
        "addr": dev.addr,
        "addi": dev.addi,
        "mulr": dev.mulr,
        "muli": dev.muli,
        "banr": dev.banr,
        "bani": dev.bani,
        "borr": dev.borr,
        "bori": dev.bori,
        "setr": dev.setr,
        "seti": dev.seti,
        "gtir": dev.gtir,
        "gtri": dev.gtri,
        "gtrr": dev.gtrr,
        "eqir": dev.eqir,
        "eqri": dev.eqri,
        "eqrr": dev.eqrr,
    }
    for name, instruction in opcodes.items():
        dev.registers = copy(registers)
        instruction(operation[1], operation[2], operation[3])
        if dev.registers == results:
            passes += 1
    return passes


def transform_register_string(text):
    """Transform the string into a list with each integer element."""
    reg = search(r".+\[(.+)\]", text)
    if reg:
        return [int(x) for x in reg.group(1).split(",")]
    else:
        raise ValueError


def transform_operation(text):
    """Transform the string into a list with each integer element."""
    return [int(x) for x in text.split(" ")]


def main():
    """Main Puzzle Entry."""
    print("Part 1: How many samples behave like 3 or more opcodes?")
    samples = []
    with open("input16.txt") as puzzle:
        while True:
            try:
                before = transform_register_string(puzzle.readline())
                operation = transform_operation(puzzle.readline())
                after = transform_register_string(puzzle.readline())
                puzzle.readline()
                samples.append(opcodes_test(before, operation, after))
            except ValueError:
                break
    samples_with_3plus = [x for x in samples if x >= 3]
    print(len(samples_with_3plus))
    print("Part 2: Figure out the opcode numbers, run the program and return register 0.")


if __name__ == "__main__":
    main()


def test_opcode_test():
    """Test the example case."""
    assert opcodes_test([3, 2, 1, 1], [9, 2, 1, 2], [3, 2, 2, 1]) == 3


def test_transform_register_string():
    """Verify that we can transform the string into the correct list."""
    assert transform_register_string("Before: [1, 0, 2, 0]") == [1, 0, 2, 0]
    assert transform_register_string("After:  [1, 1, 2, 0]") == [1, 1, 2, 0]


def test_transform_operation():
    """Verify that we can transform the string into the correct list."""
    assert transform_operation("4 1 0 1") == [4, 1, 0, 1]
