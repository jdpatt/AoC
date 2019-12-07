"""Advent of Code 2019 Day 3"""
from shared.common import get_and_transform_input


def generate_path_and_steps(instructions: list):
    """Generate a list of corridnates while keeping track of the number of steps."""
    path = {}
    x = 0
    y = 0
    steps = 0
    for instruction in instructions:
        direction = instruction[0]
        count = instruction[1:]
        for _ in range(1, int(count) + 1):
            steps += 1
            x, y = next_corridnate(direction, x, y)
            path.update({(x, y): steps})
    return path


def manhattan_distance(from_point, to_point):
    """Return the manhattan distance between two points."""
    return abs(from_point[0] - to_point[0]) + abs(from_point[1] - to_point[1])


def next_corridnate(direction, x, y):
    """Return the next corridnate given a direction."""
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


def corridnates(path):
    """From the list of steps/locations, return just the corridnates."""
    return list(path.keys())


def get_crossings(path_one, path_two):
    return set(corridnates(path_one)).intersection(set(corridnates(path_two)))


def closest_crossing(crossings):
    """Find the intersection with the smallest manhattan distance."""
    distances = [manhattan_distance((0, 0), crossing) for crossing in crossings]
    return min(distances)


def fewest_step_intersection(crossings, path_one, path_two):
    """For part 2, we want the intersection with the fewest steps instead of smallest distance."""
    steps = 10000
    for crossing in crossings:
        crossing_steps = path_one[crossing] + path_two[crossing]
        if crossing_steps < steps:
            steps = crossing_steps
    return steps


if __name__ == "__main__":
    PUZZLE = get_and_transform_input("input3.txt")
    line_one = generate_path_and_steps(PUZZLE[0].split(","))
    line_two = generate_path_and_steps(PUZZLE[1].split(","))
    crossings = get_crossings(line_one, line_two)
    print(
        f"Part 1: Manhattan distance from the central port to the closest intersection: {closest_crossing(crossings)}"
    )
    print(
        f"Part 2: Intersection with the fewest combined steps: {fewest_step_intersection(crossings, line_one, line_two)}"
    )


def test_generate_path_and_steps():
    assert generate_path_and_steps(["U3"]) == {(0, 1): 1, (0, 2): 2, (0, 3): 3}


def test_next_corridnate():
    assert next_corridnate("U", 0, 0) == (0, 1)


def test_corridnates():
    assert corridnates({(0, 1): 1, (0, 2): 2, (0, 3): 3}) == [(0, 1), (0, 2), (0, 3)]


def test_manhattan_distance():
    assert manhattan_distance((0, 0), (3, 3)) == 6


def test_closest_crossing():
    assert (
        closest_crossing(
            get_crossings(
                generate_path_and_steps(
                    ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
                ),
                generate_path_and_steps(
                    ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
                ),
            )
        )
        == 159
    )


def test_fewest_step_intersection():
    line_one = generate_path_and_steps(
        ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
    )
    line_two = generate_path_and_steps(
        ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
    )
    crossings = get_crossings(line_one, line_two)
    assert fewest_step_intersection(crossings, line_one, line_two) == 610
