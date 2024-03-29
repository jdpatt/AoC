import queue
import time
from enum import Enum

import pytest


class MODE(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class IntCodeComputer:
    def __init__(self, program=None, pointer=0):
        self._opcodes = {
            1: self.add,
            2: self.mul,
            3: self.store,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.adjust_relative_base,
            99: self.halt,
        }
        self.memory = [0] * 1048576  # Arbitrary Memory Size
        if program:
            self.put_program_in_memory(program, 0)
        self.pointer = pointer
        self.relative_base = 0
        self.running = True
        self.input_register = queue.Queue()
        self.output_register = queue.Queue()

    def put_program_in_memory(self, program, offset=0):
        for index, instruction in enumerate(program):
            self.memory[offset + index] = instruction

    def decode_instruction(self, instruction):
        """Decode the current instruction"""
        instruction = str(instruction)
        opcode = instruction[-2:]
        argument_modes = []
        modes = instruction[:-2]
        for character in modes[::-1]:
            if character == "1":
                argument_modes.append(MODE.IMMEDIATE)
            elif character == "2":
                argument_modes.append(MODE.RELATIVE)
            else:
                argument_modes.append(MODE.POSITION)
        return int(opcode), argument_modes

    def run_opcode(self, opcode, arg_modes):
        """Run the individual command updating the results in the memory."""
        self._opcodes[opcode](arg_modes)

    def get_args(self, num_of_args=1):
        return self.memory[self.pointer + 1 : self.pointer + 1 + num_of_args]

    def get_input(self):
        return self.input_register.get(block=True)

    # OPCODE INSTRUCTIONS ------------------------------------

    def add(self, arg_modes):
        a, b, output = self.get_args(3)
        a = self.read(a, get_mode(arg_modes, 0))
        b = self.read(b, get_mode(arg_modes, 1))
        self.write(output, a + b, get_mode(arg_modes, 2))
        self.pointer += 4

    def mul(self, arg_modes):
        a, b, output = self.get_args(3)
        a = self.read(a, get_mode(arg_modes, 0))
        b = self.read(b, get_mode(arg_modes, 1))
        self.write(output, a * b, get_mode(arg_modes, 2))
        self.pointer += 4

    def store(self, arg_modes):
        """Store a new value in memory at the given address."""
        address = self.get_args(1)[0]
        self.write(address, self.get_input(), get_mode(arg_modes, 0))
        self.pointer += 2

    def output(self, arg_modes):
        """store a value from memory at the given address."""
        address = self.get_args(1)[0]
        value = self.read(address, get_mode(arg_modes, 0))
        self.output_register.put_nowait(value)
        self.pointer += 2

    def jump_if_true(self, arg_modes):
        first, second = self.get_args(2)
        first = self.read(first, get_mode(arg_modes, 0))
        second = self.read(second, get_mode(arg_modes, 1))
        if first:
            self.pointer = second
        else:
            self.pointer += 3

    def jump_if_false(self, arg_modes):
        first, second = self.get_args(2)
        first = self.read(first, get_mode(arg_modes, 0))
        second = self.read(second, get_mode(arg_modes, 1))
        if not first:
            self.pointer = second
        else:
            self.pointer += 3

    def less_than(self, arg_modes):
        first, second, output = self.get_args(3)
        first = self.read(first, get_mode(arg_modes, 0))
        second = self.read(second, get_mode(arg_modes, 1))
        if first < second:
            self.write(output, 1, get_mode(arg_modes, 2))
        else:
            self.write(output, 0, get_mode(arg_modes, 2))
        self.pointer += 4

    def equals(self, arg_modes):
        first, second, output = self.get_args(3)
        first = self.read(first, get_mode(arg_modes, 0))
        second = self.read(second, get_mode(arg_modes, 1))
        if first == second:
            self.write(output, 1, get_mode(arg_modes, 2))
        else:
            self.write(output, 0, get_mode(arg_modes, 2))
        self.pointer += 4

    def halt(self, arg_modes):
        self.running = False

    def adjust_relative_base(self, arg_modes):
        address = self.get_args(1)[0]
        value = self.read(address, get_mode(arg_modes, 0))
        self.relative_base += value
        self.pointer += 2

    # --------------------------------------------------------

    def run(self, program=None):
        """Run the intCode Program until completion."""
        if program:
            self.memory = program
        while self.running:
            self.run_opcode(*self.decode_instruction(self.memory[self.pointer]))

    def read(self, address, mode=MODE.POSITION):
        if mode == MODE.POSITION:
            return self.memory[address]
        elif mode == MODE.RELATIVE:
            return self.memory[address + self.relative_base]
        return address

    def write(self, address, value, mode=MODE.POSITION):
        if mode == MODE.POSITION:
            self.memory[address] = value
        elif mode == MODE.RELATIVE:
            self.memory[address + self.relative_base] = value

    def push(self, item):
        self.input_register.put_nowait(item)

    def pop(self):
        return self.output_register.get_nowait()

    def output_results(self):
        results = []
        while not self.output_register.empty():
            try:
                results.append(self.output_register.get(block=False))
            except queue.Empty:
                continue
            self.output_register.task_done()
        return results


def get_mode(arg_list, index, default=MODE.POSITION):
    try:
        return arg_list[index]
    except IndexError:
        return default


@pytest.fixture
def computer():
    comp = IntCodeComputer([1002, 4, 3, 4, 33])
    comp.input_register.put(1)
    return comp


def test_decode_instruction(computer):
    assert computer.decode_instruction("1102") == (2, [MODE.IMMEDIATE, MODE.IMMEDIATE])
    assert computer.decode_instruction("1002") == (2, [MODE.POSITION, MODE.IMMEDIATE])
    assert computer.decode_instruction("2") == (2, [])


def test_get_args(computer):
    assert list(computer.get_args()) == [4]
    assert list(computer.get_args(2)) == [4, 3]
    assert list(computer.get_args(3)) == [4, 3, 4]


def test_add(computer):
    computer.add([MODE.IMMEDIATE, MODE.POSITION])
    assert computer.memory == [1002, 4, 3, 4, 8]


def test_mul(computer):
    computer.mul([MODE.POSITION, MODE.IMMEDIATE])
    assert computer.memory == [1002, 4, 3, 4, 99]


def test_store(computer):
    computer.store([])
    assert computer.memory == [1002, 4, 3, 4, 1]


def test_output(computer):
    computer.output([MODE.IMMEDIATE])
    assert 4 in list(computer.output_register.queue)


def test_halt(computer):
    computer.halt([])
    assert not computer.running


def test_adjust_relative_base(computer):
    computer.memory = [109, 19, 99]
    computer.relative_base = 2000
    computer.run()
    assert computer.relative_base == 2019


def test_simple_program(computer):
    computer.run()
    assert computer.memory == [1002, 4, 3, 4, 99]


def test_simple_program2(computer):
    computer.memory = [3, 0, 4, 0, 99]
    computer.run()
    assert 1 in list(computer.output_register.queue)


def test_compare_equal_pos_program(computer):
    computer.memory = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    computer.input_register.queue.clear()
    computer.input_register.put(8)
    computer.run()
    assert 1 in list(computer.output_register.queue)


def test_compare_notequal_pos_program(computer):
    computer.memory = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    computer.input_register.queue.clear()
    computer.input_register.put(2)
    computer.run()
    assert 0 in list(computer.output_register.queue)


def test_compare_equal_immediate_program(computer):
    computer.memory = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    computer.input_register.queue.clear()
    computer.input_register.put(8)
    computer.run()
    assert 1 in list(computer.output_register.queue)


def test_compare_notequal_immediate_program(computer):
    computer.memory = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    computer.input_register.queue.clear()
    computer.input_register.put(2)
    computer.run()
    assert 0 in list(computer.output_register.queue)


def test_compare_lessthan_pos_program(computer):
    computer.memory = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    computer.input_register.queue.clear()
    computer.input_register.put(2)
    computer.run()
    assert 1 in list(computer.output_register.queue)


def test_compare_greaterthan_pos_program(computer):
    computer.memory = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    computer.input_register.queue.clear()
    computer.input_register.put(9)
    computer.run()
    assert 0 in list(computer.output_register.queue)


def test_compare_lessthan_immediate_program(computer):
    computer.memory = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    computer.input_register.queue.clear()
    computer.input_register.put(2)
    computer.run()
    assert 1 in list(computer.output_register.queue)


def test_compare_greaterthan_immediate_program(computer):
    computer.memory = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    computer.input_register.queue.clear()
    computer.input_register.put(9)
    computer.run()
    assert 0 in list(computer.output_register.queue)


def test_jump_pos_program(computer):
    computer.memory = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    computer.input_register.queue.clear()
    computer.input_register.put(0)
    computer.run()
    assert 0 in list(computer.output_register.queue)


def test_jump_immediate_program(computer):
    computer.memory = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    computer.input_register.queue.clear()
    computer.input_register.put(0)
    computer.run()
    assert 0 in list(computer.output_register.queue)


def test_jump_pos_program2(computer):
    computer.memory = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    computer.input_register.put(1)
    computer.run()
    assert 1 in list(computer.output_register.queue)


def test_jump_immediate_program2(computer):
    computer.memory = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    computer.input_register.put(1)
    computer.run()
    assert 1 in list(computer.output_register.queue)


def test_multiple_input(computer):
    computer.input_register.queue.clear()
    computer.input_register.put(1)
    computer.input_register.put(9)
    computer.pointer = 1
    computer.store([])
    computer.pointer = 2
    computer.store([])
    assert computer.memory == [1002, 9, 3, 1, 33]
