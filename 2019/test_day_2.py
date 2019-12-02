import pytest
from day_2 import IntCodeComputer


@pytest.fixture
def computer():
    return IntCodeComputer(
        [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], input1=9, input2=10
    )


def test_operand(computer):
    computer.run_opcode(0)
    assert computer.memory == [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_program(computer):
    computer.run_program()
    assert computer.memory == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
