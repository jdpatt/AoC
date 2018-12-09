"""Advent of Code 2018 Day 7"""
from re import search

from common import get_puzzle_input


def find_starting_step(steps):
    """Find steps that don't have a predecessor."""
    tasks = set([step["step"] for step in steps])
    predecessors = set([step["predecessor"] for step in steps])
    return list(predecessors - tasks)


def convert_input_text(text):
    """Step O must be finished before step C can begin."""
    steps = []
    for line in text:
        regex = search(r"Step (.) must be finished before step (.) can begin.", line)
        steps.append({"predecessor": regex.group(1), "step": regex.group(2)})
    return steps


if __name__ == '__main__':
    puzzle = get_puzzle_input("input7.txt")
    steps = convert_input_text(puzzle)
    print(find_starting_step(steps))
