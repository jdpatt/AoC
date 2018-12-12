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
    return {"x": upper_x, "y": upper_y}


def get_largest(grid, points):
    """Count all the valid points and find the largest one."""
    return Counter(i for i in list(chain.from_iterable(grid)) if i in points)


def get_nearest_point(location, points):
    """Find out who is closest.

       If the distance is zero; we are at a point.  If it equals someone else, it's disqualified.
    """
    distance = 10000
    total_distance = 0
    closest = "X"
    for key, value in points.items():
        man = manhattan_distance(location, value)
        total_distance += man
        if man == 0:  # We are at the point.
            closest = key
            distance = 0
        elif man == distance:  # We had a tie, invalidate the tile.
            closest = "X"
            distance = 1
        elif man < distance:  # This point was closer than the last
            distance = man
            closest = key
    return closest, total_distance


def generate_and_fill_grid(upper, points):
    """Loop over every point and find the nearest neighbor."""
    # pylint: disable=C0103
    grid = [["x"] * upper["y"] for i in range(upper["x"])]
    infinite_points = set()
    infinite_points.add("X")
    safe_regions = []
    count = 0
    for y in range(0, upper["y"]):
        for x in range(0, upper["x"]):
            count += 1
            closest_point, total_distance = get_nearest_point((x, y), points)
            if y == 0 or y == (upper["y"] - 1) or x == 0 or x == (upper["x"] - 1):
                infinite_points.add(closest_point)
            if total_distance < 10000:
                safe_regions.append((x, y))
            grid[x][y] = closest_point
    print(f"Safe Region Size: {len(safe_regions)}")
    return grid, {p: v for p, v in points.items() if p not in infinite_points}


if __name__ == "__main__":
    COORDINATES = [
        (int(x[0]), int(x[1]))
        for x in (x.split(",") for x in get_puzzle_input("input6.txt"))
    ]
    UPPER = get_upper_boundary(COORDINATES)
    NEW_COORDINATES = {key: value for key, value in enumerate(COORDINATES)}
    GRID, VALID_POINTS = generate_and_fill_grid(UPPER, NEW_COORDINATES)
    AREAS = get_largest(GRID, VALID_POINTS)
    LARGEST = AREAS.most_common(1)[0]
    print(f"Largest Area: {VALID_POINTS[LARGEST[0]]} Size: {LARGEST[1]}")


def test_manhattan_distance():
    """Make sure that the rise/run is being calculated correctly."""
    assert manhattan_distance((1, 1), (2, 2)) == 2
    assert manhattan_distance((1, 2), (2, 2)) == 1
    assert manhattan_distance((1, 3), (2, 2)) == 2


def test_get_upper_boundary():
    """Verify that the grid will be large enough for the points."""
    points = [(1, 2), (1, 3), (4, 5), (10, 4), (8, 10)]
    assert get_upper_boundary(points) == {"x": 10, "y": 10}


def test_get_nearest_point():
    """Should return the nearest point and the total distance."""
    points = {0: (1, 2), 1: (1, 3), 2: (4, 5), 3: (10, 4), 4: (8, 10)}
    assert get_nearest_point((1, 1), points) == (0, 38)
    assert get_nearest_point((2, 3), points) == (1, 29)
    assert get_nearest_point((1, 3), points) == (1, 30)


def test_generate_and_fill_grid():
    """Verify that the grid fills with a sample set of data."""
    grid, points = generate_and_fill_grid(
        {"x": 5, "y": 5}, {0: (0, 0), 1: (4, 4), 2: (2, 2)}
    )
    assert points == {2: (2, 2)}
    assert grid == [
        [0, 0, "X", "X", "X"],
        [0, "X", 2, "X", "X"],
        ["X", 2, 2, 2, "X"],
        ["X", "X", 2, "X", 1],
        ["X", "X", "X", 1, 1],
    ]
    assert generate_and_fill_grid({"x": 2, "y": 2}, {0: (1, 1)}) == (
        [[0, 0], [0, 0]],
        {},
    )
