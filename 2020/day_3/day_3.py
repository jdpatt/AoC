"""Puzzle Day 3"""
import math
from pathlib import Path
from typing import List, Tuple


def read_in_map_slice():
    """The map is represented by '#' which are trees and '.' which are open spaces."""
    with open(Path(__file__).parent.joinpath("input.txt")) as puzzle_input:
        return [
            [character for character in line]
            for line in puzzle_input.read().splitlines()
        ]


def update_position(position, map_width, map_length, slope):
    """Update the current position based off the slope, wrap when at the edge of the map."""
    if position["x"] + slope[0] > map_width:
        position["x"] = (position["x"] + slope[0]) - map_width - 1
    else:
        position["x"] = position["x"] + slope[0]
    if position["y"] + slope[1] > map_length:
        position["y"] = map_length - 1
    else:
        position["y"] = position["y"] + slope[1]
    return position


def navigate_terrain(slope: Tuple[int, int], terrain_map: List[List[str]]) -> int:
    """Until we reach the bottom of the map, count the trees as we go."""
    num_of_trees = 0
    MAP_LENGTH = len(terrain_map) - 1
    MAP_WIDTH = len(terrain_map[0]) - 1
    position = {"x": 0, "y": 0}  # The upper left most corner.
    while position["y"] < MAP_LENGTH:
        position = update_position(position, MAP_WIDTH, MAP_LENGTH, slope)
        if terrain_map[position["y"]][position["x"]] == "#":
            num_of_trees += 1
    return num_of_trees


if __name__ == "__main__":
    terrain_map = read_in_map_slice()

    print(f"Part 1 Number of Trees: {navigate_terrain((3,1), terrain_map)}")
    # Part 1 Number of Trees: 289
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [navigate_terrain(slope, terrain_map) for slope in slopes]
    print(f"Part 2 Number of Trees: {math.prod(trees)}")
    # Part 2 Number of Trees: 5522401584
