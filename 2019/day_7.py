"""Advent of Code 2019 Day 7"""
import queue
import threading
from itertools import permutations
from time import sleep

import pytest
from shared.common import get_input
from shared.intcode_computer import IntCodeComputer


class Amplifier:
    def __init__(self, program, inputs=None):
        self.computer = IntCodeComputer(program)
        if inputs:
            self.computer.input_register = inputs

    def run(self):
        self.computer.run()

    def is_running(self):
        return self.computer.running

    def set_input(self, obj):
        self.computer.input_register = obj

    def set_output(self, obj):
        self.computer.output_register = obj


def run_amplification(software, combo):  # 34852
    amps = [Amplifier(software.copy()) for _ in range(0, 5)]
    output = 0
    for index in range(0, 5):
        amps[index].computer.push(combo[index])
        amps[index].computer.push(output)
        amps[index].run()
        output = amps[index].computer.pop()
    return output


def link_amplifiers(amp1, amp2):
    register = queue.Queue()
    amp1.computer.output_register = register
    amp2.computer.input_register = register


def run_amplification_with_feedback(software, combo):
    amps = [Amplifier(software.copy()) for _ in range(5)]
    link_amplifiers(amps[4], amps[0])
    link_amplifiers(amps[0], amps[1])
    link_amplifiers(amps[1], amps[2])
    link_amplifiers(amps[2], amps[3])
    link_amplifiers(amps[3], amps[4])

    for index, amp in enumerate(amps):
        amp.computer.push(combo[index])

    amps[0].computer.push(0)

    threads = list()
    for amp in amps:
        x = threading.Thread(target=amp.run)
        threads.append(x)
        x.start()
    for index in range(5):
        threads[index].join()
    return amps[4].computer.pop()


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
