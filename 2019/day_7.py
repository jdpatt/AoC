"""Advent of Code 2019 Day 7"""
from itertools import permutations
from shared.common import get_input
from shared.intcode_computer import IntCodeComputer

import pytest


class Amplifier:
    def __init__(self, program, inputs=None):
        self.computer = IntCodeComputer(program)
        if inputs:
            self.computer.input_register = inputs

    def run(self):
        self.computer.run()

    def is_running(self):
        return self.computer.running

    def output(self):
        return self.computer.output_register

    def inputs(self, values):
        self.computer.input_register = values


def run_amplification(software, combo):  # 34852
    amps = [Amplifier(software.copy()) for _ in range(0, 5)]
    output = 0
    for index in range(0, 5):
        amps[index].inputs([combo[index], output])
        amps[index].run()
        output = amps[index].output()[0]
    return amps[4].output()


def run_amplification_with_feedback(software, combo):
    amps = [Amplifier(software.copy()) for _ in range(0, 5)]
    output = 0
    while amps[4].is_running():
        for index in range(0, 5):
            amps[index].inputs([combo[index], output])
            amps[index].run()
            output = amps[index].output()[0]
    return amps[4].output()


if __name__ == "__main__":
    AMPLIFIER_SOFTWARE = [int(x) for x in get_input("input7.txt").split(",")]
    PHASE_SETTINGS = permutations(range(0, 5))
    max_output = max(
        run_amplification(AMPLIFIER_SOFTWARE, combo) for combo in PHASE_SETTINGS
    )
    print(f"Part 1: Max Output Possible: {max_output}")

    NEW_PHASE_SETTINGS = permutations(range(5, 10))
    max_output = max(
        run_amplification_with_feedback(AMPLIFIER_SOFTWARE, combo)
        for combo in NEW_PHASE_SETTINGS
    )
    print(f"Part 2: Max Output Possible with Feedback: {max_output}")


def test_feedback_loop():
    assert max(
        [
            run_amplification_with_feedback(
                [
                    3,
                    26,
                    1001,
                    26,
                    -4,
                    26,
                    3,
                    27,
                    1002,
                    27,
                    2,
                    27,
                    1,
                    27,
                    26,
                    27,
                    4,
                    27,
                    1001,
                    28,
                    -1,
                    28,
                    1005,
                    28,
                    6,
                    99,
                    0,
                    0,
                    5,
                ],
                combo,
            )
            for combo in permutations(range(0, 5))
        ]
        == 139629729
    )
