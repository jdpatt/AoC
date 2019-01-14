"""Advent of Code 2018 Day 7"""
from collections import defaultdict
from re import search
from string import ascii_uppercase

from shared.common import get_puzzle_input


def convert_input_text(text):
    """Step O must be finished before step C can begin."""
    steps = defaultdict(list)
    predecessors = set()
    for line in text:
        regex = search(r"Step (.) must be finished before step (.) can begin.", line)
        # steps[step] = [list of predecessors]
        steps[regex.group(2)].append(regex.group(1))
        predecessors.add(regex.group(1))
    for key in predecessors - set(steps):
        steps[key] = []
    return steps


def letter_index(letter):
    return ascii_uppercase.index(letter) + 1


def find_parallel_duration(steps, workers=5, step_duration=60):  # GNJOCHKSWTFMXLYDZABIREPVUQ
    duration = 0
    agents = []
    while steps or agents:
        print(f"Current Duration: {duration}")
        for letter in sorted(steps):
            if len(steps[letter]) == 0 and len(agents) < workers:
                steps.pop(letter)
                agents.append({
                    "letter": letter,
                    "duration": duration - 1 + letter_index(letter) + step_duration
                })
                print(f"Worker {letter} added.")
        if agents:
            inprogress = []
            for worker in agents:
                if worker["duration"] <= duration:
                    print(f"Worker {worker['letter']} removed.")
                    steps = remove_predecessors(steps, worker["letter"])
                else:
                    inprogress.append(worker)
            agents = inprogress
        duration += 1
    return duration


def find_sequential_ordering(steps):
    final_order = []
    while steps:
        for letter in sorted(steps):
            if len(steps[letter]) == 0:
                final_order.append(letter)
                steps.pop(letter)
                steps = remove_predecessors(steps, letter)
                break
    return "".join(final_order)


def remove_predecessors(steps, letter):
    for _, value in steps.items():
        if letter in value:
            value.remove(letter)
    return steps


if __name__ == '__main__':
    PUZZLE = get_puzzle_input("input/input7.txt")
    STEPS = convert_input_text(PUZZLE)
    DURATION = find_parallel_duration(STEPS)
    ORDER = find_sequential_ordering(STEPS)
    print(f"Part 1 Final Order: {ORDER}")
    print(f"Part 2 Duration: {DURATION}")


def test_remove_predecessors():
    """Make sure that we can pop from the dictionary's value."""
    assert remove_predecessors({"A": ["B", "C"]}, "B") == {"A": ["C"]}
    assert remove_predecessors({"A": ["B", "C"]}, "D") == {"A": ["B", "C"]}


def test_find_sequential_ordering():
    """Compare the sort to the example."""
    example = {"C": [], "A": ["C"], "F": ["C"], "B": ["A"], "D": ["A"], "E": ["B", "D", "F"]}
    assert find_sequential_ordering(example) == "CABDFE"


def test_find_parallel_duration():
    """Compare the duration to the example."""
    pt2_example = {"C": [], "A": ["C"], "F": ["C"], "B": ["A"], "D": ["A"], "E": ["B", "D", "F"]}
    assert find_parallel_duration(pt2_example, 2, 0) == 15
