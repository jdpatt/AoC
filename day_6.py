"""Advent of Code 2018 Day 6"""
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


def get_nearest_point(location, points):
    """Find out who is closest.

       If the distance is zero; we are at a point.  If it equals someone else, it's disqualified.
    """
    distance = 0
    closest = "X"
    for key, value in points.items():
        man = manhattan_distance(location, value)
        if man == 0:
            return {key: 0}
        elif man < distance:
            distance = man
            closest = key
        elif man == distance:
            return "X"
        else:
            distance = man
            closest = key
    return {closest: distance}


def generate_grid(lower, upper):
    """Generate a list to fit the bounding points."""
    return [[[]] * (upper[0] - lower[0])] * (upper[1] - lower[1])


def fill_grid(grid, lower, upper, points):
    """Loop over every point and find the nearest neighbor."""
    points_id = {index: value for index, value in enumerate(points)}
    for row in range(upper[1] - lower[1]):
        for column in range(upper[0] - lower[0]):
            grid[row][column] = get_nearest_point((row + lower[0], column + lower[1]), points_id)
    return grid


if __name__ == "__main__":
    COORDINATES = [
        (int(x[0]), int(x[1]))
        for x in (x.split(",") for x in get_puzzle_input("input6.txt"))
    ]
    lower, upper = get_bounding_area(COORDINATES)
    grid = generate_grid(lower, upper)
    filled_grid = fill_grid(grid, lower, upper, COORDINATES)
    print(filled_grid)


def test_manhattan_distance():
    assert manhattan_distance((1, 1), (2, 2)) == 2


def test_generate_grid():
    grid = generate_grid((41, 42), (357, 356))
    assert len(grid) == (356 - 42)
    for x in range(0, 356 - 42):
        assert len(grid[x]) == (357 - 41)
