"""Advent of Code 2019 Day 9"""
from shared.common import get_input
from shared.intcode_computer import IntCodeComputer

if __name__ == "__main__":
    BOOST_PROGRAM = [int(x) for x in get_input("input9.txt").split(",")]
    computer = IntCodeComputer(BOOST_PROGRAM.copy())
    computer.push(1)
    computer.run()
    print(f"BOOST KeyCode: {computer.output_results()}")
    del computer

    computer = IntCodeComputer(BOOST_PROGRAM.copy())
    computer.push(2)
    computer.run()
    print(f"Coordinates of the Distress Signal: {computer.output_results()}")


def test_program_1():
    computer = IntCodeComputer(
        [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    )
    computer.run()
    assert computer.output_results() == [
        109,
        1,
        204,
        -1,
        1001,
        100,
        1,
        100,
        1008,
        100,
        16,
        101,
        1006,
        101,
        0,
        99,
    ]


def test_program_2():
    computer = IntCodeComputer([1102, 34915192, 34915192, 7, 4, 7, 99, 0])
    computer.push(1)
    computer.run()
    assert computer.output_results() == [1219070632396864]


def test_program_3():
    computer = IntCodeComputer([104, 1125899906842624, 99])
    computer.push(1)
    computer.run()
    assert computer.output_results() == [1125899906842624]
