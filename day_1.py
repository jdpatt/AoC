"""Advent of Code 2018 Day 1"""
import operator


def device_calibration():
    """Calculate the final frequency drift after falling in time."""
    ops = {"+": operator.add, "-": operator.sub}
    frequency = 0
    with open("input1.txt", "r") as text:
        for line in text:
            function = ops[line[:1]]
            change = int(line[1:])
            frequency = function(frequency, change)
        print(f"Final Frequency: {frequency}")


def find_repeating_frequency():
    """Find the first frequency that repeats."""
    ops = {"+": operator.add, "-": operator.sub}
    with open("input1.txt", "r") as input_txt:
        text = input_txt.readlines()

    frequency = 0
    results = set()
    while True:
        for line in text:
            function = ops[line[:1]]
            change = int(line[1:])
            frequency = function(frequency, change)
            if frequency not in results:
                results.add(frequency)
            else:
                print(f"First Repeated: {frequency}")
                return


if __name__ == "__main__":
    device_calibration()
    find_repeating_frequency()
