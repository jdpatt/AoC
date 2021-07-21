"""Puzzle Day 1"""
import itertools
import math
from pathlib import Path
from typing import List


def find_combo_that_sum_to_value(iterable: List[int], value: int, length: int = 2):
    """Given an iterable find a combination that sums to `value`.

    Args:
        iterable: The object to use to generate the combinations.
        value: The sum we are trying to find.
        length: The length of the combination.
    """
    for combo in itertools.combinations(iterable, length):
        if sum(combo) == value:
            return combo


if __name__ == "__main__":
    with open(Path(__file__).parent.joinpath("input.txt")) as puzzle_input:
        expense_report = set([int(x) for x in puzzle_input.readlines()])

    combo = find_combo_that_sum_to_value(expense_report, 2020, 2)
    print(f"Combo: {combo} Product: {math.prod(combo)}")
    # Combo: (631, 1389) Product: 876459

    combo = find_combo_that_sum_to_value(expense_report, 2020, 3)
    print(f"Combo: {combo} Product: {math.prod(combo)}")
    # Combo: (140, 1172, 708) Product: 116168640
