"""Advent of Code 2019 Day 6"""
from shared.common import get_and_transform_input

import pytest


class OrbitMap:
    def __init__(self, list_of_orbits):
        self.tree = {}
        for item in list_of_orbits:
            link = item.split(")")
            self.tree.setdefault(link[0], []).append(link[1])
            self.tree.setdefault(link[1], []).append(link[0])
        self.orbits_to_calculate = list(self.tree.keys())


if __name__ == "__main__":
    PUZZLE = get_and_transform_input("input6.txt")
    print(OrbitMap(PUZZLE).checksum())


@pytest.fixture
def orbit():
    return OrbitMap(
        ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L",]
    )


def test_calculate_distance(orbit):
    assert orbit.calculate_distance("COM", "B") == 1
    assert orbit.calculate_distance("COM", "D") == 3


def test_orbit_map(orbit):
    assert orbit.checksum() == 42
