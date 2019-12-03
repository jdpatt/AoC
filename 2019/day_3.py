"""Advent of Code 2019 Day 3"""
from shared.common import get_and_transform_input


def generate_path(instructions: list):
    path = []
    x = 0
    y = 0
    for instruction in instructions:
        direction = instruction[0]
        count = instruction[1:]
        for _ in range(1, int(count) + 1):
            x, y = get_next_corridnate(direction, x, y)
            path.append((x, y))
    return path

def manhattan_distance(from_point, to_point):
    return abs(from_point[0] - to_point[0]) + abs(from_point[1] -  to_point[1])

def get_next_corridnate(direction, x, y):
    if direction == "U":
        return (x, y + 1)
    elif direction == "D":
        return (x, y - 1)
    elif direction == "L":
        return (x - 1, y)
    elif direction == "R":
        return (x + 1, y)
    else:
        raise ValueError


def get_closest_crossing(path_one, path_two):
    crossings = set(path_one).intersection(set(path_two))
    distances = [manhattan_distance((0, 0), crossing) for crossing in crossings]
    return min(distances)


if __name__ == "__main__":
    PUZZLE = get_and_transform_input("input3.txt")
    line_one = PUZZLE[0].split(",")
    line_two = PUZZLE[1].split(",")
    closest = get_closest_crossing(generate_path(line_one), generate_path(line_two))
    print(f"The Manhattan distance from the central port to the closest intersection: {closest}")


def test_generate_path():
    assert generate_path(["U3"]) == [(0, 1), (0, 2), (0, 3)]


def test_get_next_corridnate():
    assert get_next_corridnate("U", 0, 0) == (0, 1)

def test_manhattan_distance():
    assert manhattan_distance((0, 0), (3, 3)) == 6

def test_get_closest_crossing():
    assert (
        get_closest_crossing(
            generate_path(
                ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
            ),
            generate_path(["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]),
        )
        == 159
    )
