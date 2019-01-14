"""Advent of Code 2018 Day 11"""
# pylint: disable=C0103
# x, y and k are valid names for this puzzle.
from itertools import product

from shared.common import get_puzzle_input


def calculate_fuel_cell(grid_width, serial):
    """Create the fuel cell and calculate each cell's value.

    In X,Y notation, the top-left cell is 1,1, and the top-right cell is 300,1
    """
    fuel_cell = {}
    for row, column in product(range(1, grid_width + 1), range(1, grid_width + 1)):
        fuel_cell[(column, row)] = calculate_power_level(column, row, serial)
    return fuel_cell


def calculate_power_level(x, y, serial):
    """Calculate the current cell's power level."""
    rack_id = x + 10
    power_level = ((rack_id * y) + serial) * rack_id
    try:
        hundreds = int(str(power_level)[-3])
    except IndexError:
        hundreds = 0
    return hundreds - 5


def get_largest_sub_matrix(matrix, matrix_width, k):
    """Get the largest sub matrix of size of `k`."""
    largest = -100
    location = None
    for key, _ in matrix.items():
        if key[0] >= matrix_width - 1 or key[1] >= matrix_width - 1:
            pass
        else:
            sub_sum = get_sub_matrix_sum(matrix, key, k)
            if sub_sum > largest:
                largest = sub_sum
                location = key
    return largest, location


def get_largest_sub_matrix_anysize(matrix, matrix_width):
    """Get the largest sub matrix of any size of `k`."""
    largest = -100
    location = None
    size = 0
    for k in range(1, matrix_width + 1):
        for key, _ in matrix.items():
            if key[0] >= matrix_width - k + 1 or key[1] >= matrix_width - k + 1:
                pass
            else:
                sub_sum = get_sub_matrix_sum(matrix, key, k)
                if sub_sum > largest:
                    largest = sub_sum
                    location = key
                    size = k
        print(f"Current Size: {k} Largest: {largest} @ {location}")
    return largest, location, size


def get_sub_matrix_sum(matrix, start, k):
    """Return a sub matrix with the size of `k` starting at `start`."""
    matrix_sum = 0
    for item in product(range(0 + start[0], k + start[0]), range(0 + start[1], k + start[1])):
        matrix_sum += matrix.get(item, 0)
    return matrix_sum


def main():
    """Main Puzzle Entry."""
    SERIAL_NUMBER = int(get_puzzle_input("input/input11.txt")[0])
    GRID_WIDTH = 300
    fuel_cell = calculate_fuel_cell(GRID_WIDTH, SERIAL_NUMBER)
    largest, location = get_largest_sub_matrix(fuel_cell, GRID_WIDTH, 3)
    print(f"Serial: {SERIAL_NUMBER} Top Left: {location} Largest: {largest}")
    largest, location, size = get_largest_sub_matrix_anysize(fuel_cell, GRID_WIDTH)
    print(f"Top Left: {location} Largest: {largest} Size {size}")


if __name__ == "__main__":
    main()


def test_calculate_power_level():
    """Verify that we pass the examples for calculating power levels."""
    assert calculate_power_level(3, 5, 8) == 4
    assert calculate_power_level(122, 79, 57) == -5
    assert calculate_power_level(217, 196, 39) == 0
    assert calculate_power_level(32, 45, 18) == -4


def test_calculate_fuel_cell():
    """Verify that we calculate a summed area table correctly."""
    fuel = calculate_fuel_cell(300, 18)
    assert fuel[32, 45] == -4
    assert fuel[33, 45] == 4
    assert fuel[34, 45] == 4
    assert fuel[35, 45] == 4
    assert fuel[36, 45] == -5


def test_get_sub_matrix_sum():
    """Verify that we can get the sum of a sub matrix with an upper left starting point and a width
    of k.
    """
    matrix = calculate_fuel_cell(300, 18)
    assert get_sub_matrix_sum(matrix, (33, 45), 3) == 29


def test_part_1_example1():
    """For grid serial number 18, the largest total 3x3 square has a top-left corner of 33,45
    (with a total power of 29)"""
    fuel = calculate_fuel_cell(300, 18)
    largest, location = get_largest_sub_matrix(fuel, 300, 3)
    assert location == (33, 45)
    assert largest == 29


def test_part_1_example2():
    """For grid serial number 42, the largest 3x3 square's top-left is 21,61
    (with a total power of 30)"""
    fuel = calculate_fuel_cell(300, 42)
    largest, location = get_largest_sub_matrix(fuel, 300, 3)
    assert location == (21, 61)
    assert largest == 30


# def test_part_2_example():
#     """For grid serial number 18, the largest total square (with a total power of 113) is 16x16 and
#     has a top-left corner of 90,269, so its identifier is 90,269,16.
#     """
#     fuel = calculate_fuel_cell(300, 18)
#     largest, location, size = get_largest_sub_matrix_anysize(fuel, 300)
#     assert location == (90, 269)
#     assert largest == 113
#     fuel = calculate_fuel_cell(300, 9995)
#     largest, location, size = get_largest_sub_matrix_anysize(fuel, 300)
#     print(f"Top Left: {location} Largest: {largest} Size {size}")
