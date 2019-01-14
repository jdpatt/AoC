"""Advent of Code 2018 Day 10"""
# pylint: disable=C0103
from collections import namedtuple
from re import search

from shared.common import get_puzzle_input

Point = namedtuple("Point", ["x", "y"])
Velocity = namedtuple("Velocity", ["x", "y"])


class Location:
    """A location on the map."""

    def __init__(self, current_location, velocity):
        self.point = {"x": current_location.x, "y": current_location.y}
        self.velocity = velocity

    def advance(self, steps=1):
        """Advance the point by `steps`."""
        self.point["x"] = self.point["x"] + self.velocity.x * steps
        self.point["y"] = self.point["y"] + self.velocity.y * steps

    def __str__(self):
        print(f"Location: {self.point} Velocity: {self.velocity}")


def get_x_boundary(locations):
    """Return the smallest and largest coordinate."""
    return (
        min([x.point["x"] for x in locations]),
        max([x.point["x"] for x in locations]),
    )


def get_y_boundary(locations):
    """Return the smallest and largest coordinate."""
    return (
        min([x.point["y"] for x in locations]),
        max([x.point["y"] for x in locations]),
    )


def get_points_from_input(text):
    """Create a list of the points from the input file."""
    locations = []
    for line in text:
        regex = search(r"position=<(.+), (.+)> velocity=<(.+), (.+)>", line)
        if regex:
            locations.append(
                Location(
                    Point(int(regex.group(1)), int(regex.group(2))),
                    Velocity(int(regex.group(3)), int(regex.group(4))),
                )
            )
    return locations


def location_exists_at_points(points, x, y):
    """See if a location exists at the given x y coordinates."""
    for location in points:
        if location.point["x"] == x and location.point["y"] == y:
            return True
    return False


def print_grid(points):
    """Print the grid of points using the smallest and largest points as the bounding box."""
    x_bound = get_x_boundary(points)
    y_bound = get_y_boundary(points)
    for row in range(y_bound[0], y_bound[1] + 1):
        for column in range(x_bound[0], x_bound[1] + 1):
            if location_exists_at_points(points, column, row):
                print("#", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    PUZZLE = get_puzzle_input("input/input10.txt")
    POINTS = get_points_from_input(PUZZLE)
    for point in POINTS:
        point.advance(10086)
    print_grid(POINTS)


def test_location():
    """Verify that we can advance n steps correctly."""
    location = Location(Point(0, 0), Velocity(1, -1))
    location.advance(1)
    assert location.point == {"x": 1, "y": -1}
    location.advance(2)
    assert location.point == {"x": 3, "y": -3}


def test_exists_at_points():
    """Verify that we can see if points exist."""
    points = [Location(Point(1, 2), 0), Location(Point(1, 1), 0)]
    assert location_exists_at_points(points, 1, 1)
    assert not location_exists_at_points(points, 2, 2)
