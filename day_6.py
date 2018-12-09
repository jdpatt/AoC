"""Advent of Code 2018 Day 6"""
from itertools import chain
from collections import Counter

from common import get_puzzle_input


def manhattan_distance(point_1, point_2):
    """Return the Manhattan distance between two Cartesian coordinates."""
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


def get_bounding_area(points):
    """Given a list of Cartesian points, find a bounding box"""

    # New Origin
    lower_x = min(x[0] for x in points)
    lower_y = min(y[1] for y in points)

    # Outer Extreme
    upper_x = max(x[0] for x in points)
    upper_y = max(y[1] for y in points)
    return (lower_x, lower_y), (upper_x, upper_y)


def get_largest(grid, points):
    """Count all the valid points and find the largest one."""
    return Counter(i for i in list(chain.from_iterable(grid)))


def get_nearest_point(location, points):
    """Find out who is closest.

       If the distance is zero; we are at a point.  If it equals someone else, it's disqualified.
    """
    distance = 1000
    closest = "X"
    for key, value in points.items():
        man = manhattan_distance(location, value)
        if man == 0:
            return key
        elif man < distance:
            distance = man
            closest = key
        elif man == distance:
            return "X"
    return closest


def generate_grid(lower, upper):
    """Generate a list to fit the bounding points."""
    return [[{}] * (upper[0] - lower[0])] * (upper[1] - lower[1])


def fill_grid(grid, lower, upper, points):
    """Loop over every point and find the nearest neighbor."""
    infinite_points = set()
    for row in range(upper[1] - lower[1]):
        row_offset = row + lower[0]
        for column in range(upper[0] - lower[0]):
            column_offset = column + lower[1]
            closest_point = get_nearest_point((row_offset, column_offset), points)
            if (
                row_offset == lower[1] or
                row_offset == upper[1] or
                column_offset == lower[0] or
                column_offset == upper[0]
            ):
                infinite_points.add(closest_point)
                grid[row][column] = "-"
            else:
                grid[row][column] = closest_point
    return grid, infinite_points


if __name__ == "__main__":
    COORDINATES = [
        (int(x[0]), int(x[1]))
        for x in (x.split(",") for x in get_puzzle_input("input6.txt"))
    ]
    lower, upper = get_bounding_area(COORDINATES)
    grid = generate_grid(lower, upper)

    NEW_COORDINATES = {key: value for key, value in enumerate(COORDINATES)}
    grid, infinite_points = fill_grid(grid, lower, upper, NEW_COORDINATES)
    valid_coordinates = {p: v for p, v in NEW_COORDINATES.items() if p not in infinite_points}
    areas = get_largest(grid, valid_coordinates)
    print(areas)
    largest = areas.most_common(1)[0]
    print(f"Largest Area: {NEW_COORDINATES[largest[0]]} Size: {largest[1]}")


def test_manhattan_distance():
    assert manhattan_distance((1, 1), (2, 2)) == 2


def test_generate_grid():
    grid = generate_grid((41, 42), (357, 356))
    assert len(grid) == (356 - 42)
    for x in range(0, 356 - 42):
        assert len(grid[x]) == (357 - 41)
