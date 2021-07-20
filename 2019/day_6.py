"""Advent of Code 2019 Day 6"""
import pytest
from shared.common import get_and_transform_input


def path(orbit_map, item):
    path = []
    current_item = item
    while current_item != "COM":
        current_item = orbit_map.get(current_item, "COM")
        path.append(current_item)
    return path


if __name__ == "__main__":
    PUZZLE = get_and_transform_input("input6.txt")
    orbit_map = dict(reversed(item.split(")")) for item in PUZZLE)
    print(
        f"Part 1: Checksum: {sum(len(path(orbit_map, key)) for key in orbit_map.keys())}"
    )

    you = path(orbit_map, "YOU")
    santa = path(orbit_map, "SAN")
    orbits_between = len(set(you) - set(santa)) + len(set(santa) - set(you))
    print(f"Part 2: Distance between SAN and YOU: {orbits_between}")


@pytest.fixture
def orbits():
    return dict(
        reversed(item.split(")"))
        for item in [
            "COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L",
        ]
    )


def test_distance(orbits):
    assert len(path(orbits, "B")) == 1
    assert len(path(orbits, "D")) == 3


def test_orbit_map(orbits):
    assert orbits == {
        "G": "B",
        "D": "C",
        "B": "COM",
        "I": "D",
        "J": "E",
        "H": "G",
        "K": "J",
        "L": "K",
        "C": "B",
        "E": "D",
        "F": "E",
    }


def test_find_santa():
    orbits = dict(
        reversed(item.split(")"))
        for item in [
            "COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L",
            "K)YOU",
            "I)SAN",
        ]
    )
    assert path(orbits, "YOU") == ["K", "J", "E", "D", "C", "B", "COM"]
    assert path(orbits, "SAN") == ["I", "D", "C", "B", "COM"]
    you = path(orbits, "YOU")
    santa = path(orbits, "SAN")
    you_unique = set(you) - set(santa)
    santa_unique = set(santa) - set(you)
    assert len(you_unique) + len(santa_unique) == 4
