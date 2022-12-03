"""Day 3 AoC 2022"""
import string

import pytest

PRIORITY = string.ascii_lowercase + string.ascii_uppercase


def equipment_priority(equipment_type):
    """Return the priority of the equipment type."""
    return PRIORITY.index(str(equipment_type)) + 1


def find_duplicated_equipment(*args):
    """Return a set of all characters that show up in both.

    This could be more than one but the examples only have one.
    """
    if len(args) <= 1:
        raise ValueError("Not enough elements.")
    first = set(args[0])
    others = (set(item) for item in args[1:])
    return list(first.intersection(*others))[0]  # Should always be just one.


if __name__ == "__main__":

    #! Open and read in the puzzle. ----------------------------------------------
    with open("./2022/day_03_input.txt") as puzzle_input:
        inventory = [line.strip() for line in puzzle_input]

    # ? Part 1  ----------------------------------------------
    duplicated = [
        find_duplicated_equipment(line[: len(line) // 2], line[len(line) // 2 :])
        for line in inventory
    ]
    priorities = [equipment_priority(item) for item in duplicated]
    print(f"Sum of priorities {sum(priorities)}")

    # * Part 2  ----------------------------------------------
    groups_of_elves = zip(*(iter(inventory),) * 3)
    badge_types = [find_duplicated_equipment(*group) for group in groups_of_elves]
    badge_priorities = [equipment_priority(item) for item in badge_types]
    print(f"Sum of priorities based on badge type: {sum(badge_priorities)}")


@pytest.mark.parametrize("letter, score", (("A", 27), ("a", 1)))
def test_priority_score(letter, score):
    assert equipment_priority(letter) == score
