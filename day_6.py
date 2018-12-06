"""Advent of Code 2018 Day 6"""
from common import get_puzzle_input


def manhattan_distance(point_1, point_2):
    """Return the Manhattan distance between two Cartesian coordinates."""
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


if __name__ == "__main__":
    COORDINATES = [
        (int(x[0]), int(x[1]))
        for x in (x.split(",") for x in get_puzzle_input("input6.txt"))
    ]


def test_manhattan_distance():
    assert manhattan_distance((1, 1), (2, 2)) == 2
