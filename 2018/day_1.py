"""Advent of Code 2018 Day 1"""
from shared.common import get_puzzle_input


def device_calibration(frequencies):
    """Calculate the final frequency drift after falling in time."""
    return sum(frequency for frequency in frequencies)


def find_repeating_frequency(frequencies):
    """Find the first frequency that repeats."""
    seen_frequencies = set()
    current_freq = 0
    while True:
        for frequency in frequencies:
            current_freq += frequency
            if current_freq not in seen_frequencies:
                seen_frequencies.add(current_freq)
            else:
                return current_freq


if __name__ == "__main__":
    frequencies = [int(x) for x in get_puzzle_input("input/input1.txt")]
    print(f"Final Frequency: {device_calibration(frequencies)}")
    print(f"First Repeated: {find_repeating_frequency(frequencies)}")
