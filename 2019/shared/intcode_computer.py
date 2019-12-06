import pytest
from enum import Enum


class MODE(Enum):
    POSITION = 0
    IMMEDIATE = 1


class IntCodeComputer:
    def __init__(self, memory, pointer=0):
        self._opcodes = {
            1: self.add,
            2: self.mul,
            3: self.store,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            99: self.halt,
        }
        self.memory = memory
        self.pointer = pointer
        self.running = True
        self.input_val = 1

    @property
    def opcodes(self):
        return self._opcodes

    def decode_instruction(self, instruction):
        """Decode the current instruction"""
        instruction = str(instruction)
        opcode = instruction[-2:]
        argument_modes = []
        modes = instruction[:-2]
        for character in modes[::-1]:
            if character == "1":
                argument_modes.append(MODE.IMMEDIATE)
            else:
                argument_modes.append(MODE.POSITION)
        return int(opcode), argument_modes

    def run_opcode(self, opcode, arg_modes):
        """Run the individual command updating the results in the memory."""
        self.opcodes[opcode](arg_modes)

    def get_args(self, num_of_args=1):
        return self.memory[self.pointer + 1 : self.pointer + 1 + num_of_args]

    def get_input(self):
        return self.input_val

    def set_input(self, value):
        self.input_val = value

    # OPCODE INSTRUCTIONS ------------------------------------

    def add(self, arg_modes):
        a, b, output = self.get_args(3)
        a = self.read(a, get_mode(arg_modes, 0))
        b = self.read(b, get_mode(arg_modes, 1))
        self.write(output, a + b)
        self.pointer += 4

    def mul(self, arg_modes):
        a, b, output = self.get_args(3)
        a = self.read(a, get_mode(arg_modes, 0))
        b = self.read(b, get_mode(arg_modes, 1))
        self.write(output, a * b)
        self.pointer += 4

    def store(self, arg_modes):
        """Store a new value in memory at the given address."""
        address = self.get_args(1)[0]
        self.memory[address] = self.get_input()
        self.pointer += 2

    def output(self, arg_modes):
        """store a value from memory at the given address."""
        address = self.get_args(1)[0]
        address = self.read(address, get_mode(arg_modes, 0))
        print(address)
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
            self.write(output, 1)
        else:
            self.write(output, 0)
        self.pointer += 4

    def equals(self, arg_modes):
        first, second, output = self.get_args(3)
        first = self.read(first, get_mode(arg_modes, 0))
        second = self.read(second, get_mode(arg_modes, 1))
        if first == second:
            self.write(output, 1)
        else:
            self.write(output, 0)
        self.pointer += 4

    def halt(self, arg_modes):
        self.running = False

    # --------------------------------------------------------

    def run(self):
        """Run the intCode Program until completion."""
        while self.running:
            self.run_opcode(*self.decode_instruction(self.memory[self.pointer]))

    def read(self, address, mode=MODE.POSITION):
        if mode == MODE.POSITION:
            return self.memory[address]
        return address

    def write(self, address, value):
        self.memory[address] = value


def get_mode(arg_list, index, default=MODE.POSITION):
    try:
        return arg_list[index]
    except IndexError:
        return default


@pytest.fixture
def computer():
    comp = IntCodeComputer([1002, 4, 3, 4, 33])
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


def test_output(capsys, computer):
    computer.output([MODE.IMMEDIATE])
    captured = capsys.readouterr()
    assert "4" in captured.out


def test_halt(computer):
    computer.halt([])
    assert not computer.running


def test_simple_program(computer):
    computer.run()
    assert computer.memory == [1002, 4, 3, 4, 99]


def test_simple_program2(capsys, computer):
    computer.memory = [3, 0, 4, 0, 99]
    computer.run()
    captured = capsys.readouterr()
    assert "1" in captured.out


def test_compare_equal_pos_program(capsys, computer):
    computer.memory = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    computer.set_input(8)
    computer.run()
    captured = capsys.readouterr()
    assert "1" in captured.out


def test_compare_notequal_pos_program(capsys, computer):
    computer.memory = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    computer.set_input(2)
    computer.run()
    captured = capsys.readouterr()
    assert "0" in captured.out


def test_compare_equal_immediate_program(capsys, computer):
    computer.memory = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    computer.set_input(8)
    computer.run()
    captured = capsys.readouterr()
    assert "1" in captured.out


def test_compare_notequal_immediate_program(capsys, computer):
    computer.memory = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    computer.set_input(2)
    computer.run()
    captured = capsys.readouterr()
    assert "0" in captured.out


def test_compare_lessthan_pos_program(capsys, computer):
    computer.memory = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    computer.set_input(2)
    computer.run()
    captured = capsys.readouterr()
    assert "1" in captured.out


def test_compare_greaterthan_pos_program(capsys, computer):
    computer.memory = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    computer.set_input(9)
    computer.run()
    captured = capsys.readouterr()
    assert "0" in captured.out


def test_compare_lessthan_immediate_program(capsys, computer):
    computer.memory = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    computer.set_input(2)
    computer.run()
    captured = capsys.readouterr()
    assert "1" in captured.out


def test_compare_greaterthan_immediate_program(capsys, computer):
    computer.memory = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    computer.set_input(9)
    computer.run()
    captured = capsys.readouterr()
    assert "0" in captured.out


def test_jump_pos_program(capsys, computer):
    computer.memory = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    computer.set_input(0)
    computer.run()
    captured = capsys.readouterr()
    assert "0" in captured.out


def test_jump_immediate_program(capsys, computer):
    computer.memory = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    computer.set_input(0)
    computer.run()
    captured = capsys.readouterr()
    assert "0" in captured.out


def test_jump_pos_program2(capsys, computer):
    computer.memory = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    computer.set_input(1)
    computer.run()
    captured = capsys.readouterr()
    assert "1" in captured.out


def test_jump_immediate_program2(capsys, computer):
    computer.memory = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    computer.set_input(1)
    computer.run()
    captured = capsys.readouterr()
    assert "1" in captured.out
