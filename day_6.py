"""Advent of Code 2018 Day 6"""
from itertools import chain
from collections import Counter

from common import get_puzzle_input


def manhattan_distance(point_1, point_2):
    """Return the Manhattan distance between two Cartesian coordinates."""
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


def get_upper_boundary(points):
    """Given a list of Cartesian points, find a bounding box"""
    upper_x = max(x[0] for x in points)
    upper_y = max(y[1] for y in points)
    return (upper_x, upper_y)


def get_largest(grid, points):
    """Count all the valid points and find the largest one."""
    return Counter(i for i in list(chain.from_iterable(grid)) if i in points)


def get_nearest_point(location, points):
    """Find out who is closest.

       If the distance is zero; we are at a point.  If it equals someone else, it's disqualified.
    """
    distance = 10000
    closest = "X"
    for key, value in points.items():
        man = manhattan_distance(location, value)
        if man == 0:  # We are at the point.
            return key
        elif man == distance:  # We had a tie, invalidate the tile.
            return "X"
        elif man < distance:  # This point was closer than the last, so make it the closest
            distance = man
            closest = key
    return closest


def generate_and_fill_grid(upper, points):
    """Loop over every point and find the nearest neighbor."""
    grid = [[0] * upper[0]] * upper[1]
    infinite_points = set()
    infinite_points.add("X")
    for row in range(0, upper[1]):
        for column in range(0, upper[0]):
            closest_point = get_nearest_point((row, column), points)
            if (
                row == 0 or row == upper[0] or  # 357
                column == 0 or column == upper[1]  # 356
            ):
                infinite_points.add(closest_point)
            grid[row][column] = closest_point
    return grid, {p: v for p, v in points.items() if p not in infinite_points}


if __name__ == "__main__":
    COORDINATES = [
        (int(x[0]), int(x[1]))
        for x in (x.split(",") for x in get_puzzle_input("input6.txt"))
    ]
    upper = get_upper_boundary(COORDINATES)
    NEW_COORDINATES = {key: value for key, value in enumerate(COORDINATES)}
    grid, valid_points = generate_and_fill_grid(upper, NEW_COORDINATES)
    areas = get_largest(grid, valid_points)
    print(areas)
    largest = areas.most_common(1)[0]
    print(f"Largest Area: {valid_points[largest[0]]} Size: {largest[1]}")


def test_manhattan_distance():
    assert manhattan_distance((1, 1), (2, 2)) == 2
