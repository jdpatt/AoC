"""Puzzle Day 6"""
from pathlib import Path

import pytest


def get_common_in_group(group):
    results = set(group[0])
    for passenger in group[1:]:
        results.intersection_update(passenger)
    return results


if __name__ == "__main__":
    with open(Path(__file__).parent.joinpath("input.txt")) as puzzle_input:
        passenger_groups = [
            [passengers for passengers in group.split("\n") if passengers]
            for group in puzzle_input.read().split("\n\n")
        ]

    # Spliting with "\n\n" is going to add an empty element at the end.
    anyone_answered_yes = [
        len(set("".join(passengers))) for passengers in passenger_groups
    ]

    print(
        f"Sum of yes for anyone in passenger groups: {sum(anyone_answered_yes)}"
    )  # 6259

    group_answered_yes = list()
    for group in passenger_groups:
        group_answered_yes.append(len(get_common_in_group(group)))

    print(
        f"Sum of yes for everyone in passenger groups: {sum(group_answered_yes)}"
    )  # 3178


@pytest.mark.parametrize(
    "test,expected",
    [
        (["abc"], 3),
        (["a", "b", "c"], 0),
        (["ab", "ac"], 1),
        (["a", "a", "a", "a"], 1),
        (["b"], 1),
    ],
)
def test_get_common_in_group(test, expected):
    assert len(get_common_in_group(test)) == expected
